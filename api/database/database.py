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
        return '<People %r>' % self.id

    def add_user(self):
        newPeople = People(name=self['name'], last_name=self['last_name'], age=self['age'], picture_url=self['picture_url'])
        db.session.add(newPeople)
        db.session.commit()
        db.session.flush()
        return self

    def get_users():
        result = []
        for people in People.query.all():
            print(str(people))
            result.append(people.__dict__)
        return result

    def get_users_by_id(id):
        return People.query.filter(People.id == id).first()

    def update_users_by_id(id):
        newPeople = People(name=self['name'], last_name=self['last_name'], age=self['age'], picture_url=self['picture_url'])
        db.session.add(newPeople)
        db.session.commit()
        db.session.flush()
        return self

    def delete_users_by_id(id):
        return People.query.filter(People.id == id).delete(synchronize_session=False)
