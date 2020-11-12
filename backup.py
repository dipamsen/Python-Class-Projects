# Backing Up files
import os
import shutil
source = input("Enter src folder: ")
dest = input("Enter dest folder: ")
listoffiles = os.listdir(source)

for file in listoffiles:
    shutil.copy((source+'/'+file), dest)
