from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect, flash
import ipdb

movies_blueprint = Blueprint("movies", __name__)

from flaskdemo.app import app, db
from flaskdemo.models.movie import Movie

movies_blueprint = Blueprint("movies", __name__)


@movies_blueprint.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@movies_blueprint.route("/movies/", defaults={"page_nr": 1})
@movies_blueprint.route("/movies/page=<int:page_nr>&items=<int:item_nr>", methods=["GET", "POST"])
def movies(page_nr):
    # get all entrance from DB
    all_movies = Movie.query.all()
    items_per_page = request.args.get("items", 5, type=int)
    current_page = request.args.get("page", 1, type=int)
    page_nr = current_page

    if page_nr == 1:
        page_possition = 0
    elif page_nr > 1 and page_nr <= len(all_movies) // items_per_page:
        page_possition = items_per_page * (page_nr - 1)
    else:
        page_possition = 0

    return render_template(
        "movies/items.html",
        movies=all_movies[page_possition : page_possition + items_per_page],
        current_page=current_page,
        items_per_page=items_per_page,
    )


@movies_blueprint.route("/movies/new", methods=["GET", "POST"])
def new_item():
    movie = Movie()
    if request.method == "POST":
        title = request.form.get("title")
        genre = request.form.get("genre")
        rating = request.form.get("rating")
        url = request.form.get("url")

        messg = ""
        if not title:
            messg = "Title is required!"
        elif not genre:
            messg = "Category type is required!"
        elif not rating:
            messg = "Rating is required!"
        elif not url:
            messg = "Movie url is required!"
        else:
            movie.title = title
            movie.genre = genre
            movie.rating = rating
            movie.url = url
        # ipdb.set_trace()
        return render_template("index.html", messg=messg)

        # db.session.add(movie)
        # db.session.commit()

    return render_template("movies/new.html", new_movie=movie)


@movies_blueprint.route("/movies/<int:id>")
def show(id):
    item = Movie.query.get(id)
    return render_template("/movies/show.html", movies=item)


@movies_blueprint.route("/movies/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    item = Movie.query.get(id)
    if request.method == "POST":
        title = request.form.get("title")
        genre = request.form.get("genre")
        rating = request.form.get("rating")
        url = request.form.get("url")

        messg = ""
        if not title:
            messg = "Title is required!"
        elif not genre:
            messg = "Category type is required!"
        elif not rating:
            messg = "Rating is required!"
        elif not url:
            messg = "Movie url is required!"
        else:
            item.title = title
            item.genre = genre
            item.rating = rating
            item.url = url
        # ipdb.set_trace()
        return render_template("index.html", messg=messg)

        # db.session.add(movie)
        # db.session.commit()
    return render_template("/movies/edit.html", movie=item)
