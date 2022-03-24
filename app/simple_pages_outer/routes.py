from flask import Blueprint, render_template, redirect, url_for, send_file

blueprint = Blueprint('simple_pages_outer', __name__)

@blueprint.route('/')
def index(): 
    return render_template('simple_pages/index.html')

""" NAV BAR """

@blueprint.route('/about')
def about(): 
    return render_template('/simple_pages/about.html')

@blueprint.route('/contact')
def contact(): 
    return render_template('/simple_pages/contact.html')

@blueprint.route('/glossary')
def glossary(): 
    return render_template('/simple_pages/glossary.html')

@blueprint.route('/use-cases')
def use_cases(): 
    return render_template('/simple_pages/use-cases.html')

