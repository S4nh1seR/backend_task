from flask_mail import Message
from flask import render_template, flash, redirect, url_for, request
import pika

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])
    
def send_email(to, subject, template):
    msg = Message(subject, recipients=[to], html=template, sender=app.config['MAIL_USERNAME'])
    mail.send(msg)

def callback(ch, method, properties, body):
	email = body
	token = generate_confirmation_token(email)
	confirm_url = url_for('confirm_email', token=token, _external=True)
	html = render_template('activate.html', confirm_url=confirm_url)
	subject = "Please confirm your email"
	send_email(user.email, subject, html)


conn_params = pika.ConnectionParameters(host='rabbit', port=5672)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
channel.queue_declare(queue='rabbit-queue')
channel.basic_consume(callback, queue='rabbit-queue', no_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    connection.close()