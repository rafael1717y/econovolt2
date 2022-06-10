import os
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app.ext.auth import models
from app.ext.mail import mail


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    print(">> admin: ", os.environ.get("ADMINS"))
    print(">> user.email: ", user.email)

    send_email(
        "[ECONOVOLT] Crie uma nova senha",
        sender=os.environ.get("ADMINS"),
        recipients=[user.email],
        text_body=render_template("email/reset_password.txt", user=user, token=token),
        html_body=render_template("email/reset_password.html", user=user, token=token),
    )


# TODO: envio de emails async (app_context error)
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # Thread(target=send_async_email, args=(app, msg)).start()
    mail.send(msg)
