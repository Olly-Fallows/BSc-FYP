# This file is a collection of functions used on images, mainly converting them
# to matrixes, loading from files and converting a matrix into an image.

from model import matrix

from PIL import Image
import numpy as np

# Function to open an image file, crop it, resize it, and return it as a matrix
def load_image(path):
    # Use PILLOW to open the image
    img = Image.open(path)
    # Figure with side is longer and thus which one to crop to make the image square
    if img.size[0] > img.size[1]:
        # Set the size to the size of the smaller side
        size = img.size[1]
        # Check if the size is even
        if size%2 == 0:
            # If it isn't make it even
            size -= 1
        # Find the diffence in the length of the image long and short side
        dif = int((img.size[0]-size)/2)
        left = dif
        top = 0
        right = size+dif
        bottom = size
        # Crop the image to square with lenght of size
        img = img.crop((left, top, right, bottom))
    # The ELIF is a repeat of the IF
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
    # Resize the image down to 512x512 to allow for quicker exicution
    img = img.resize((512, 512))
    # Get the value of the image as a 1d array
    i = np.asarray(img)
    # Close the image to free up memory
    img.close()
    # Return the value of the array reshaped to a 3d array
    return matrix.matrix(i.reshape(3, i.shape[0], i.shape[1]).tolist())
