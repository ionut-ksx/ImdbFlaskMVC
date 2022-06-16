from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect, flash
import ipdb

movies_blueprint = Blueprint("movies", __name__)

from flaskdemo.app import app, db
from flaskdemo.models.movie import Movie

movies_blueprint = Blueprint("movies", __name__)


@movies_blueprint.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@movies_blueprint.route("/movies/")
# @movies_blueprint.route("/movies/page=<int:page_nr>&items=<int:item_nr>", methods=["GET", "POST"]) -- for me
def movies():
    # get all entrance from DB
    all_movies = Movie.query.order_by(Movie.id).all()

    per_page = request.args.get("items", 5, type=int)
    current_page = request.args.get("page", 1, type=int)

    movie_count = len(all_movies)

    # if current_page == 1:
    #     position = 0
    # elif current_page > 1 and current_page <= len(all_movies) // per_page:
    #     position = per_page * (current_page - 1)
    # else:
    #     position = 0

    start = per_page * (current_page - 1)
    end = min(start + per_page, movie_count)
    movies = all_movies[start:end]
    mess = ""
    if len(movies) == 0:
        mess = "Error message, no more items"

    return render_template(
        "movies/items.html", movies=movies, current_page=current_page, items_per_page=per_page, mess=mess
    )


@movies_blueprint.route("/movies/new", methods=["GET", "POST"])
def new_item():
    movie = Movie()

    if request.method == "POST":
        try:
            title = request.form.get("title")
            genre = request.form.get("genre")
            rating = request.form.get("rating")
            url = request.form.get("url")
            date_of_scraping = request.form.get("date_of_scraping")
            director = request.form.get("director")
            release_year = request.form.get("release_year")
            top_cast = request.form.get("top_cast")
            image_urls = request.form.get("image_urls")
            images = request.form.get("images")

            movie.title = title
            movie.genre = genre
            movie.rating = rating
            movie.url = url
            movie.date_of_scraping = date_of_scraping
            movie.director = director
            movie.release_year = release_year
            movie.top_cast = top_cast
            movie.image_urls = image_urls
            movie.images = images
        except AssertionError as err:
            return render_template("/movies/new.html", err=err)
        else:
            db.session.add(movie)
            db.session.flush()
            db.session.commit()
            return render_template("index.html")

    return render_template("movies/new.html", new_movie=movie)


@movies_blueprint.route("/movies/<int:id>")
def show(id):
    item = Movie.query.get(id)
    return render_template("/movies/show.html", movies=item)


@movies_blueprint.route("/movies/<int:id>", methods=["POST"])
def update(id):
    item = Movie.query.get(id)
    try:
        title = request.form.get("title")
        genre = request.form.get("genre")
        rating = request.form.get("rating")
        url = request.form.get("url")
        date_of_scraping = request.form.get("date_of_scraping")
        director = request.form.get("director")
        release_year = request.form.get("release_year")
        top_cast = request.form.get("top_cast")
        image_urls = request.form.get("image_urls")
        images = request.form.get("images")

        item.title = title
        item.genre = genre
        item.rating = rating
        item.url = url
        item.date_of_scraping = date_of_scraping
        item.director = director
        item.release_year = release_year
        item.top_cast = top_cast
        item.image_urls = image_urls
        item.images = images
    except AssertionError as err:
        return render_template("/movies/edit.html", movie=item, err=err)
        # return redirect(url_for("movies.edit", id=item.id, err=err))
    else:
        db.session.flush()
        db.session.commit()

        return redirect(url_for("movies.show", id=item.id))
    # movie_url = "/movies/" + str(id) + "show.html"
    # return redirect(url_for("movies.edit", id=item.id))


@movies_blueprint.route("/movies/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    item = Movie.query.get(id)
    return render_template("/movies/edit.html", movie=item)
