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

    def __repr__(self):
        return "<Movie id=%s> %s %s" % (self.id, self.title, self.url)

    @validates(
        "genre",
        "date_of_scraping",
        "director",
        "rating",
        "release_year",
        "title",
        "top_cast",
        "url",
        "image_urls",
        "images",
    )
    def validates_fields(self, keys, values):
        # ipdb.set_trace()
        if keys == "title":
            assert values != "", "Title is missing"
        if keys == "genre":
            assert values != "", "Category is required"
        if keys == "date_of_scraping":
            assert values != "", "DateTime is required"
        if keys == "director":
            assert values != "", "Director name is required"
        if keys == "rating":
            assert values != "", "Raiting is required"
        if keys == "release_year":
            assert values.isdigit() and len(values) == 4, "Year is required. ie(2022)"
        if keys == "top_cast":
            assert values != "", "Top Case data is required"
        if keys == "url":
            assert values != "", "Url is required"
        if keys == "image_urls":
            assert values != "", "Image URL is required"
        if keys == "images":
            assert values.endswith('.jpg"'), "JPG file is required"

        return values

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
