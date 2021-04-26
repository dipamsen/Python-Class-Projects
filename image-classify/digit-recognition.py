import cv2
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image
import PIL.ImageOps
import os
import ssl
import time
import pandas as pd

if (not os.environ.get("PYTHONHTTPSVERIFY", "") and getattr(ssl, "_create_unverified_context", None)):
  ssl._create_default_https_context = ssl._create_unverified_context

X, y = fetch_openml("mnist_784", version=1, return_X_y=True)
print(pd.Series(y).value_counts())
classes = ["0", "1", "2", "3", "4", "5", "6", "7",
           "8", "9"]  # [str(i) for i in range(0, 10, 1)]
n_classes = len(classes)

xtrain, xtest, ytrain, ytest = train_test_split(
    X, y, random_state=9, train_size=7500, test_size=2500)

xtrain_scaled = xtrain / 255.0
xtest_scaled = xtest / 255.0

clf = LogisticRegression(
    solver="saga", multi_class="multinomial").fit(xtrain_scaled, ytrain)
ypred = clf.predict(xtest_scaled)
acc = accuracy_score(ytest, ypred)

print(acc)

# start cam
cap = cv2.VideoCapture(0)
while True:
  try:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape
    upper_left = (int(width / 2 - 50), int(height / 2 - 50))
    bottom_right = (int(width / 2 + 50), int(height / 2 + 50))
    cv2.rectangle(gray, upper_left, bottom_right, (0, 255, 0), 2)
    ri = gray[upper_left[1]:bottom_right[1], upper_left[0]:bottom_right[0]]
    img = Image.fromarray(ri)
    img_btwn = img.convert("L")
    img_btwn_res = img_btwn.resize((28, 28), Image.ANTIALIAS)
    img_res_inv = PIL.ImageOps.invert(img_btwn_res)
    pixel_filter = 20
    min_pixel = np.percentile(img_res_inv, pixel_filter)
    img_scl = np.clip(img_res_inv - min_pixel, 0, 255)
    max_pixel = np.max(img_res_inv)
    img_scl = np.asarray(img_scl) / max_pixel
    test_sample = np.array(img_scl).reshape(1, 784)
    test_pred = clf.predict(test_sample)
    print("Predicted Classes: ", test_pred)

    cv2.imshow("Frame", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break
  except Exception as e:
    pass

cap.release()
cv2.destroyAllWindows()
