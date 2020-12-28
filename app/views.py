from app.main import app, db, mail
# from app.models import models

import os
import json
import uuid

from flask_mail import Message
from flask import Flask, request, flash, redirect, url_for, jsonify, make_response, abort, render_template


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization, multipart/form-data, boundary'
    return response


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        pass
    
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Page not found'}), 404)