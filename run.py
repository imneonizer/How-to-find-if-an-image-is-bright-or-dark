import os
import glob
import cv2
import numpy as np

def isbright(image, dim=10, thresh=0.5):
    # Resize image to 10x10
    image = cv2.resize(image, (dim, dim))
    # Convert color space to LAB format and extract L channel
    L, A, B = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2LAB))
    # Normalize L channel by dividing all pixel values with maximum pixel value
    L = L/np.max(L)
    # Return True if mean is greater than thresh else False
    return np.mean(L) > thresh

# create output directories if not exists
os.makedirs("output/bright", exist_ok=True)
os.makedirs("output/dark", exist_ok=True)

# iterate through images directory
for i, path in enumerate(glob.glob("images/*")):
    # load image from path
    image = cv2.imread(path)

    # find if image is bright or dark
    path = os.path.basename(path)
    text = "bright" if isbright(image) else "dark"

    # save image to disk
    cv2.imwrite("output/{}/{}".format(text, path), image)
    print(path, "=>", text)