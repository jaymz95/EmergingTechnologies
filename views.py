from flask import Flask, Blueprint, render_template, request
#from flask_bootstrap import Bootstrap

#from scipy.misc import imsave, imread, imresize (outdated)
import cv2
from imageio import imread, imwrite
from skimage.transform import resize, rescale
import numpy as np
#import keras.models
import re
import sys
import os
#sys.path.append(os.path.abspath('./model'))
#from loadModel import *
from flask_cors import CORS, cross_origin
import base64


from .loadModel import init

#import loadModel
import tensorflow.keras.models

#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
#from tensorflow import keras
from tensorflow.keras import backend as be

import matplotlib.pyplot as plt

def convertImage(imgData1):
    imgstr = re.search(b'base64,(.*)',imgData1).group(1)
    with open('output.png','wb') as output:
        output.write(base64.b64decode(imgstr))

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return  render_template('index.html')

@main.route('/predict', methods=['GET', 'POST'])
def predict():
    imgData = request.get_data()
    convertImage(imgData)
    x = imread('output.png')
    
    # Gets the last layer on the canvas becasue it returns 3D array
    # this gets the final element in the array
    x = np.transpose(x, axes=[2, 0, 1])
    x = x[3]

    x = np.invert(x)
    x = resize(x, (28, 28))
    
    print(x.ndim)
    print(x.shape)
    #x = x.transpose(2,0,1).reshape(-1,x.shape[1])
    x = resize(x, (28, 28))
    #plt.imshow(x)
    #plt.show()
    print(len(x))
    x = x.reshape(1, 28, 28, 1)
    
    print(x.ndim)
    print(x.shape)
    print(x)

    global model, graph
    model, graph = init()
    model._make_predict_function()
    with graph.as_default():
        #perform the prediction
        out = model.predict(x)
        response = np.array_str(np.argmax(out,axis=1))
        return response	