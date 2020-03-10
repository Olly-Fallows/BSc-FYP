# This file is a collection of functions used on images, mainly converting them
# to matrixes, loading from files and converting a matrix into an image.

from model import matrix

from PIL import Image
import numpy as np

def load_image(path):
    img = Image.open(path)
    if img.size[0] > img.size[1]:
        size = img.size[1]
        if size%2 == 0:
            size -= 1
        dif = int((img.size[0]-size)/2)
        left = dif
        top = 0
        right = size+dif
        bottom = size
        img = img.crop((left, top, right, bottom))
    elif img.size[0] < img.size[1]:
        size = img.size[0]
        if size%2 == 0:
            size -= 1
        dif = int((img.size[1]-size)/2)
        left = 0
        top = dif
        right = size
        bottom = size+dif
        img = img.crop((left, top, right, bottom))
    img = img.resize((512, 512))
    i = np.asarray(img)
    img.close()
    return matrix.matrix(i.reshape(3, i.shape[0], i.shape[1]).tolist())
