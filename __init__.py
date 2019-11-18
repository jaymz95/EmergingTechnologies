from flask import Flask
from flask_bootstrap import Bootstrap
#from scipy.misc import imsave, imread, imresize

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    from .views import main 
    app.register_blueprint(main)

    return app