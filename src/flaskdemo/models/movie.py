from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from flaskdemo.app import db
import datetime


class Movie(db.Model):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    genre = Column(String(255), nullable=False)
    date_of_scraping = Column(String(255), nullable=False)
    director = Column(String(255), nullable=False)
    rating = Column(String(20), nullable=False)
    release_year = Column(String(20), nullable=False)
    title = Column(String(255), nullable=False)
    top_cast = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    image_urls = Column(String(255), nullable=False)
    images = Column(String(100), nullable=False)

    def __repr__(self):
        return "<Movie id=%s> %s %s" % (self.id, self.title, self.url)
