from threading import Thread
from flask import current_app
from flask_mail import Message
from app.ext.mail import mail
import os 
from flask import render_template
from app.ext.auth import models




def send_password_reset_email(user):
    print('Exec send_password_reset_email, l.11')
    token = user.get_reset_password_token()
    print('linha 14 token >>', token)
    print('linha 15 admin>', os.environ.get('ADMINS'))
    print('user.email', user.email)
    
    send_email('[ECONOVOLT] Crie uma nova senha',
        sender=os.environ.get('ADMINS'), recipients=[user.email], text_body=render_template('email/reset_password.txt',
        user=user, token=token), html_body=render_template('email/reset_password.html', user=user, 
        token=token))
    


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app, msg)).start()
    print('linha 35 -msg.body>>',msg.body)
