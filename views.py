from flask import Flask, Blueprint, render_template, request
#from flask_bootstrap import Bootstrap

#from scipy.misc import imsave, imread, imresize (outdated)

from imageio import imread, imwrite
from skimage.transform import resize
import numpy as np
#import keras.models
#import re

#import tensorflow as tf
#from tensorflow import keras

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return  render_template('index.html')

