#import numpy as np
#import keras.models
#from keras.models import model_from_json

import numpy as np
#import tensorflow_core as tf

from tensorflow_core.keras import models
#from tensorflow.keras import models

#import tensorflow as tf
#from tensorflow.python.keras import backend as tf
#from tensorflow.keras import backend as tf

from tensorflow.python.framework import ops
#import tensorflow as tf
#import keras.models
from tensorflow_core.keras.models import model_from_json
#import tensorflow as tf
#import keras.models
#from keras.models import model_from_json
#from scipy.misc import imread, imresize,imshow


from imageio import imread, imwrite
from skimage.transform import resize
#import tensorflow as tf

def init(): 
  json_file = open('EmergingTechProject/model.json','r')
  loaded_model_json = json_file.read()
  json_file.close()
  loaded_model = model_from_json(loaded_model_json)
	#load weights into new model
  loaded_model.load_weights("EmergingTechProject/model.h5")
	#loaded_model.load_weights("model.h5")
  #loaded_model = load_model('model')
  print("Loaded Model from disk")

	#compile and evaluate loaded model
  loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
  graph = ops.get_default_graph()
  return loaded_model,graph