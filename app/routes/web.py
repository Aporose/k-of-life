# app/routes/web.py
from flask import Blueprint, render_template, request

bp = Blueprint('web', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/result')
def result():
    return render_template('result.html')
