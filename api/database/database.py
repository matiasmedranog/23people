import os
import json
from flask import jsonify, current_app as app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}

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
        db.session.add(People(self['name'], self['last_name'], self['age'], self['picture_url']))
        db.session.commit()
        db.session.flush()
        return self

    def get_users():
        result = []
        for people in People.query.all():
            pdict = row2dict(people)
            pdict.pop('_sa_instance_state', None)
            result.append(pdict)
        return jsonify(result)

    def get_users_by_id(id):
        if(People.query.get(id)):
            return row2dict(People.query.get(id))
        else:
            return None

    def update_users_by_id(id, self):
        if(db.session.query(People).filter(People.id==id).update(self, synchronize_session=False)):
            db.session.query(People).filter(People.id==id).update(self, synchronize_session=False)
            db.session.commit()
            db.session.flush()
            return 200
        else:
            return None

    def delete_users_by_id(id):
        if(db.session.query(People).filter(People.id==id).delete(synchronize_session=False)):
            db.session.query(People).filter(People.id==id).delete(synchronize_session=False)
            db.session.commit()
            db.session.flush()
            return 200
        else:
            return None
