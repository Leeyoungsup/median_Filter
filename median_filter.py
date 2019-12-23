import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter.filedialog as tkfile
from PIL import ImageTk, Image
def median_filter(image):
    Mask = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    height = image.shape[0]
    width = image.shape[1]
    imageValue = np.zeros([height + 2, width + 2])
    imageValue1 = np.zeros([height + 2, width + 2])
    x = np.arange(width)
    y = np.arange(height)
    x, y = np.meshgrid(x, y)
    imageValue[y + 1, x] = image[y, x]
    imageValue[y + 1, x + 2] = image[y, x]
    imageValue[0] = imageValue[1]
    imageValue[-1] = imageValue[-2]
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            value = Mask * imageValue[i - 1:i + 2, j - 1:j + 2]
            imageValue1[i, j] = np.sort(value.reshape(9))[5]
    imageValue1 = np.delete(imageValue1, width + 1, axis=1)
    imageValue1 = np.delete(imageValue1, height + 1, axis=0)
    imageValue1 = np.delete(imageValue1, 0, axis=1)
    imageValue1 = np.delete(imageValue1, 0, axis=0)
    return imageValue1
window = Tk()
filename=tkfile.askopenfilenames(title = "Select file",parent = window, filetypes = (("jpg files","*.jpg"),("all files","*.*")))
pfile=np.array(filename)
imsi = np.array(Image.open(pfile[0])).astype(np.float32)
imsi1 = median_filter(imsi)
plt.imshow(imsi1,'gray')
plt.show()
