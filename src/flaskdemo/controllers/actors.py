from flask import Flask, Blueprint, jsonify, render_template, url_for, request, redirect, flash
import ipdb

actors_blueprint = Blueprint("actors", __name__)

from flaskdemo.app import app, db
from flaskdemo.models.actors import Actor


@actors_blueprint.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@actors_blueprint.route("/actors/", defaults={"page_nr": 1})
@actors_blueprint.route("/actors/page=<int:page_nr>&items=<int:item_nr>", methods=["GET", "POST"])
def actors(page_nr):
    # get all entrance from DB
    all_actors = Actor.query.order_by(Actor.id).all()
    per_page = request.args.get("items", 5, type=int)
    current_page = request.args.get("page", 1, type=int)

    actor_count = len(all_actors)

    # Calculate how many items to be dispalyed on the page
    start = per_page * (current_page - 1)
    end = min(start + per_page, actor_count)
    actors = all_actors[start:end]
    mess = ""
    if len(actors) == 0:
        mess = "Warning message: no more actors"

    return render_template("actors/items.html", actors=actors, current_page=current_page, per_page=per_page, mess=mess)


def to_list(dbstring):
    dbstring = dbstring.strip("'][")
    li = dbstring.split(", ")
    result = []
    for item in li:
        result.append((item[1:-1]))
    return result


@actors_blueprint.route("/actors/<int:id>")
def show(id):
    item = Actor.query.get(id)
    filmography_name = item.filmography_movie_name
    filmography_url = item.filmography_url
    filmography = [x for x in zip(to_list(filmography_name), to_list(filmography_url))]
    return render_template("/actors/show.html", actor={"name": item.name, "filmography": filmography})
