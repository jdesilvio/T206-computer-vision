import cv2
import h5py
import boto3
import imp
import os, sys, inspect

currentPath = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
rootPath = "/".join(currentPath.split('/')[0:-1])
modulePath = "/".join([rootPath, "cardsearch"])
if modulePath not in sys.path:
    sys.path.insert(0, modulePath)

from descriptor import CardDescriptor
from matcher import CardMatcher


# METHOD #1: OpenCV, NumPy, and urllib
import numpy as np
import urllib

def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

session = boto3.Session(
                        aws_access_key_id=os.environ["ACCESS_KEY"],
                        aws_secret_access_key=os.environ["SECRET_KEY"]
                       )

s3 = session.resource('s3')
t206bucket = s3.Bucket('t206')

bucketPath = "https://s3.amazonaws.com/t206/"

images = []
for object in t206bucket.objects.filter(Prefix='images/loc/fronts'):
    images.append(object.key)
images = images[1:100]
cd = CardDescriptor()
cv = CardMatcher(cd)

db = []
h5save = []
for file in images:
    filename = file.split("/")[-1]
    print filename
    image = url_to_image("".join([bucketPath, file]))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kps, descs = cd.describe(gray)

    db.append({"file": filename, "desc": (kps, descs)})
    h5save.append({"name": filename, "kps": kps, "descs": descs})

# Write data to HDF5
with h5py.File('testData/data.h5', 'w') as hf:
    h5kps = hf.create_group('kps')
    h5descs = hf.create_group('descs')
    for i in h5save:
        # Save keypoints
        h5kps.create_dataset(i["name"], data=i["kps"])
        h5kps[i["name"]].attrs["name"] = i["name"]
        # Save descriptors
        h5descs.create_dataset(i["name"], data=i["descs"])
        h5descs[i["name"]].attrs["name"] = i["name"]
