from flask import Blueprint, render_template
#from flask_bootstrap import Bootstrap
#from .models import Comment

main = Blueprint('main', __name__)


@main.route('/')
def index():
    #comments = Comment.query.all()
    return  render_template('index.html')
    # '<h2>Hello</h2>'
