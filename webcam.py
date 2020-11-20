import cv2
import random
import dropbox
import time


def capture_image():
    num = random.randint(0, 100)
    vc = cv2.VideoCapture(0)
    res = True
    while(res):
        ret, frame = vc.read()
        filename = "image" + str(num) + ".png"
        cv2.imwrite(filename, frame)
        result = False
        return filename
    vc.release()
    print("Snapshot taken at " + str(current_time))
    cv2.destroyAllWindows()


def upload_file(filename):
    access_token = "sl.Al6Bsc8e7_aP__UiIqRB-vS194RAx5uiueZemQJ4h5mgKDLdwfVYQ7h_YLmFcTo6b2dEVrBlzO4kRm8FNrn8gYo9Ks-OKw6QwXI3goU23WjIQvgTsy2ikHaNaxLDVEhOiyS7Zz0"
    dbx = dropbox.Dropbox(access_token)
    file_from = "./" + filename
    file_to = "/webcam/" + filename
    image = open(file_from, "rb")
    dbx.files_upload(image.read(), file_to,
                     mode=dropbox.files.WriteMode.overwrite)
    print("Uploaded file to Dropbox")


def main():
    last_time = 0
    while(True):
        current_time = time.time()
        time_difference = current_time - last_time
        if(time_difference > 20):
            fn = capture_image()
            upload_file(fn)
            last_time = current_time


main()
