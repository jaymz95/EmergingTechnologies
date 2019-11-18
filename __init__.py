from flask import Flask
from flask_bootstrap import Bootstrap

import sys
import os
#sys.path.append(os.path.abspath('./'))
#from .loadModel import *
#from scipy.misc import imsave, imread, imresize

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    from .views import main 
    app.register_blueprint(main)

    return app