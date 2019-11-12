from flask import Blueprint, render_template
#from flask_bootstrap import Bootstrap

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return  render_template('index.html')

