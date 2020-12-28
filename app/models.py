from flask_sqlalchemy import Model, SQLAlchemy
from datetime import datetime
from .main import db

class MyModel(db.Model):
    __tablename__ = 'mymodel name'

    id = db.Column(db.Integer(), primary_key=True)

    def __repr__(self):
	    return "<{}:{}>".format(self.id,  self.name)