from flask import Blueprint, render_template, redirect, url_for, send_file
import time

blueprint = Blueprint('simple_pages_outer', __name__)

""" FIRST AR  """

@blueprint.route('/')
def index(): 
    return render_template('simple_pages/index.html')

""" SECOND AR  """

@blueprint.route('/second')
def second(): 
    return render_template('/simple_pages/second.html')

""" THIRD AR  """

@blueprint.route('/third')
def third(): 
    return render_template('/simple_pages/third.html')

