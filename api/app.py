import logs
import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv
from people.people import people
from database.database import db
from datetime import timedelta

app = Flask(__name__)
load_dotenv(find_dotenv())
logs.get_logger()
app.register_blueprint(people, url_prefix=os.getenv('URL_PREFIX')+'/people')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'),
    host=os.getenv('HOST'), port=os.getenv('PORT'))
