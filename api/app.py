import logs
import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)

load_dotenv(find_dotenv())

logs.get_logger()

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'),
    host=os.getenv('HOST'), port=os.getenv('PORT'))
