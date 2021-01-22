from app.main import app, mail
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
        question = request.form.get("question", None)
        phone_or_email = request.form.get("phone_or_email", None)
        if question is not None and phone_or_email is not None:
            msg = Message("Задают вопрос: ", recipients=[app.config['MAIL_USERNAME']])
            msg.body = "У вас новое сообщение от {} \n\n {}.".format(phone_or_email, question)
            mail.send(msg)
            flash("Вопрос успешно отправлен :) В ближайшее время мы свяжемся с Вами. \n\n Во благо!")
        else:
            flash('Ошибка отправления. \n\nДанные не введены.')
        return redirect("/")
    
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Page not found'}), 404)