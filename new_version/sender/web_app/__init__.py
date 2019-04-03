from flask import Flask, render_template, flash, redirect, url_for, request
from config import Config
from flask_mail import Mail, Message
import pika
import json
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])
    
def send_email(to, subject, template):
    msg = Message(subject, recipients=[to], html=template, sender=app.config['MAIL_USERNAME'])
    mail.send(msg)

def callback(ch, method, properties, body):
        map_ = json.loads(body)
        with app.app_context():
                html = render_template('activate.html', confirm_url=map_["confirm_url"])
                subject = "Please confirm your email"
                send_email(map_["email"], subject, html)


conn_params = pika.ConnectionParameters(host='localhost', port=5672)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel()
channel.queue_declare(queue='rabbit-queue')
channel.basic_consume(callback, queue='rabbit-queue', no_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    connection.close()

