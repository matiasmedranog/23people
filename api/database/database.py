import os
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    picture_url = db.Column(db.String(300))

    def create(self):
      with app.app_context():
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self,name,last_name,age,picture_url):
      with app.app_context():
        db.session.add(self)
        self.name = name 
        self.last_name = last_name 
        self.age = age
        self.picture_url = picture_url

    def __repr__(self):
        return '' % self.id
