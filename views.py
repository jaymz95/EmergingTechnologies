from flask import Flask, Blueprint, render_template, request
#from flask_bootstrap import Bootstrap

#from scipy.misc import imsave, imread, imresize (outdated)

from imageio import imread, imwrite
from skimage.transform import resize
import numpy as np
#import keras.models
import re
import sys
import os
#sys.path.append(os.path.abspath('./model'))
#from loadModel import *


from .loadModel import *

#import loadModel
#import tensorflow.keras.models

#import tensorflow as tf
#from tensorflow import keras

#global model, graph
#model, graph = init()

def convertImage(imgData):
    imgstr = re.search(r'base64,(.*'.imagData1).group(1)
    with open('output.png', 'wb') as output:
        output.write(imgstr.decode('base64'))

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return  render_template('index.html')


@main.route('/predict', methods=['GET', 'POST'])
def predict():
    imgData = request.get_data()
    convertImage(imgData)
    x = imread('out.png', mode = 'L')
    x = np.invert(x)
    x = resize(x, 28, 28)
    x = x.reshape(1, 28, 28, 1)
    with graph.as_default():
        out = model.predict(x)
        response = np.array_str(np.argmax(out.png))
        return response
