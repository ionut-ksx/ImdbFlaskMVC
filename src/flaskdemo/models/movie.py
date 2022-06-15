from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship, validates
from flaskdemo.app import db
import ipdb
import datetime


class Movie(db.Model):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    genre = Column(String(255), nullable=True)
    date_of_scraping = Column(String(255), nullable=True)
    director = Column(String(255), nullable=True)
    rating = Column(String(20), nullable=True)
    release_year = Column(String(20), nullable=True)
    title = Column(String(255), nullable=False)
    top_cast = Column(String(255), nullable=True)
    url = Column(String(255), nullable=True)
    image_urls = Column(String(255), nullable=True)
    images = Column(String(100), nullable=True)

    # def __init__(
    #     self, genre, date_of_scraping, director, rating, release_year, title, top_cast, url, image_urls, images
    # ):
    #     self._genre = genre
    #     self._date_of_scraping = date_of_scraping
    #     self._date_of_scraping = director
    #     self._rating = rating
    #     self._release_year = release_year
    #     self._title = title
    #     if top_cast == None:
    #         self._top_cast = []
    #     else:
    #         self._top_cast = top_cast
    #     self.url = url
    #     self.image_urls = image_urls
    #     self.images = images
    #     super(Movie, self).__init__()
    #     self.errors = []

    # def set_movie(self, *args):
    #     pass

    def __repr__(self):
        return "<Movie id=%s> %s %s" % (self.id, self.title, self.url)

    @validates("title")
    def validate_title(self, key, title):
        assert title, "Title is missing"
        return title

        # if not title:
        #     self.errors.append("Title is missing")
        # return title
