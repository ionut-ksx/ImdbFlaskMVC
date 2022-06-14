from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from flaskdemo.app import db
import datetime


class Actor(db.Model):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    filmography_movie_name = Column(String(255), nullable=True)
    filmography_url = Column(String(255), nullable=True)

    def __repr__(self):
        return "<Actor id=%s> %s %s" % (self.id, self.name, self.url)
