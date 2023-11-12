from os.path import exists
import zipfile
import time
import os, json, subprocess
import kaggle
import splitfolders
from pathlib import Path
import shutil
import glob

os.mkdir("download/Malaria_unzipped")

os.mkdir("download/Malaria_categorised")

#loop checks for file in download location. If not there it sleeps for 30 seconds
#30 minutes is maximum wait time of this file
for i in range(60):
    if os.path.isfile(r"download/archive.zip")==True:
        print("Unzipping")
        with zipfile.ZipFile("download/archive.zip","r") as zip_ref: zip_ref.extractall(r"download/Malaria_unzipped")
        print("File unzipped")

        splitfolders.ratio(r"download/Malaria_unzipped/cell_images/cell_images", output=r"download/Malaria_categorised",seed=1337, ratio=(.8, .1, .1), group_prefix=None, move=False)
        break
    else:
        time.sleep(30)
