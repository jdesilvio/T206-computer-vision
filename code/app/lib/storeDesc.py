from descriptor import CoverDescriptor
from matcher import CoverMatcher
import argparse
import glob
import csv
import cv2
import numpy as np
import h5py

ap = argparse.ArgumentParser()

ap.add_argument("-d", "--dataset", required=True, \
help="path to the image dataset")

args = vars(ap.parse_args())

cd = CoverDescriptor()
cv = CoverMatcher(cd, glob.glob(args["dataset"] + "/*.jpg"))

db = []
h5save = []
for image in glob.glob(args["dataset"] + "/*.jpg"):
    filename = image.split("/")[-1]
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kps, descs = cd.describe(gray)

    db.append({ "file": filename, "desc": (kps, descs) })
    h5save.append({ "name": filename, "kps": kps, "descs": descs })

# Write data to HDF5
with h5py.File('data/data.h5', 'w') as hf:
    h5kps = hf.create_group('kps')
    h5descs = hf.create_group('descs')
    for i in h5save:
        # Save keypoints
        h5kps.create_dataset(i["name"], data=i["kps"])
        h5kps[i["name"]].attrs["name"] = i["name"]
        # Save descriptors
        h5descs.create_dataset(i["name"], data=i["descs"])
        h5descs[i["name"]].attrs["name"] = i["name"]
