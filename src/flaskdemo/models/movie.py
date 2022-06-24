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
    def validates_fields(self, key, value):
        if not getattr(self, "errors", None):
            self.errors = []

        if not value:
            self.errors.append(f"{key} is missing")

        return value

    def __repr__(self):
        return f"""
            "id": {self.id},
            "title": {self.title},
            "url": {self.url},
            "rating": {self.rating},
            "genre": {self.genre},
            "date_of_scraping": {self.date_of_scraping},
            "release_year": {self.release_year},
            "top_cast": {self.top_cast},
        """


# def __init__(
#     self,
#     genre=None,
#     date_of_scraping=None,
#     director=None,
#     rating=None,
#     release_year=None,
#     title=None,
#     top_cast=None,
#     url=None,
#     image_urls=None,
#     images=None,
# ):
#     self.genre = genre
#     self.date_of_scraping = date_of_scraping
#     self.director = director
#     self.rating = rating
#     self.release_year = release_year
#     self.title = title
#     if top_cast == None:
#         self.top_cast = []
#     else:
#         self.top_cast = top_cast
#     self.url = url
#     self.image_urls = image_urls
#     self.images = images

# def __setitem__(self, key, value):
#     setattr(self, key, value)

# def __getitem__(self, key):
#     return getattr(self, key)


# @services_blueprint.route("/results/")
# def search():
#     search_string = request.args.get("q")
#     count = 0
#     movies = []
#     actors = []
#     for item in (Movie, Actor):
#         if item == Movie:
#             movies.extend(Movie.query.filter(Movie.title.like("%" + search_string + "%")).all())
#             count += len(movies)

#         if item == Actor:
#             actors.extend(Actor.query.filter(Actor.name.like("%" + search_string + "%")).all())
#             count += len(actors)

#     per_page = request.args.get("items", 5, type=int)
#     current_page = request.args.get("page", 1, type=int)
#     # count = len(movies) + len(actors)
#     start = per_page * (current_page - 1)
#     end = min(start + per_page, count)
#     movies = movies[start:end]
#     actors = actors[start:end]
#     mess = ""
#     results = {
#         "movies": movies,
#         "actors": actors,
#     }
#     if count == 0:
#         mess = "Error message, no more items"
#     return render_template(
#         "services/search_results.html",
#         results=results,
#         current_page=current_page,
#         items_per_page=per_page,
#         mess=mess,
#         search_string=search_string,
#     )
