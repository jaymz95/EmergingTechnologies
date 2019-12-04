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
    #("yesssss: ")
    #print(imgData1)
    imgstr = re.search(b'base64,(.*)',imgData1).group(1)
    #print("Hello: ")
    #print(imgstr)
    with open('output.png','wb') as output:
        output.write(base64.b64decode(imgstr))

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return  render_template('index.html')

@main.route('/predict', methods=['GET', 'POST'])
def predict():
    imgData = request.get_data()
    #print(imgData.ndim)
    #print(imgData.shape)
    
    
    convertImage(imgData)
    x = imread('output.png')
    
    print(x.ndim)
    print(x.shape)
    x = np.transpose(x, axes=[2, 0, 1])
    x = x[3]
    
    #x = x.convert('1')
    #for i in range(x.shape[0]):
    #    print(x[i].shape)
    #    x = x[i]

    #x1 = x[0]
    #plt.imshow(x, cmap= plt.cm.binary)
    #plt.show()
    #plt.imshow(x[1])
    #plt.show()
    x = np.invert(x)
    print(x.ndim)
    print(x.shape)
    x = resize(x, (28, 28))
    #x = rescale(x, 0.5).shape

    #x = x.transpose(2,0,1).reshape(3,-1)
    #cv2.imshow("hiya", x)
    #x = x.reshape(1, 28, 28, 1)
    print("TEST")
    
    print(x.ndim)
    print(x.shape)
    #x = x.transpose(2,0,1).reshape(-1,x.shape[1])
    print(x.ndim)
    print(x.shape)
    print("TEST2")

    #x = cv2.resize(x, dsize=(28, 28))
    x = resize(x, (28, 28))
    #plt.imshow(x)
    #plt.show()
    #x = resize(x, (28, 28))
    print("what: ")
    print(len(x))
    
    #plt.imshow(x)
    #plt.show()
    x = x.reshape(1, 28, 28, 1)
    
    print(x.ndim)
    print(x.shape)
    print(x)

    global model, graph
    model, graph = init()
    model._make_predict_function()
    #model._make_predict_function()
    with graph.as_default():
        #perform the prediction
        #be.clear_session() 
        
        out = model.predict(x)
        #out = model._make_predict_function()
        
        #out = resnet_vgg.predict(x)
        #print(out)
        #print(np.argmax(out,axis=1))
        #convert the response to a string
        response = np.array_str(np.argmax(out,axis=1))

        return response	

    #in our computation graph

    #return  render_template('index.html')
