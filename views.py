from flask import Flask, Blueprint, render_template, request
#from flask_bootstrap import Bootstrap

#from scipy.misc import imsave, imread, imresize (outdated)
import cv2
from imageio import imread, imwrite
from skimage.transform import resize
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
    convertImage(imgData)
    x = cv2.imread('output.png')
    x = np.invert(x)
    x = cv2.resize(x, dsize=(28, 28))
    #x = x.transpose(2,0,1).reshape(3,-1)
    #cv2.imshow("hiya", x)
    #x = x.reshape(1, 28, 28, 1)
    print("TEST")
    
    print(x)
    x = x.transpose(2,0,1).reshape(-1,x.shape[1])
    x = cv2.resize(x, dsize=(28, 28))
    print("what: ")
    print(len(x))
    x = x.reshape(1, 28, 28, 1)
    
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
