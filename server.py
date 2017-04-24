import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
conn = sqlite3.connect("duke/duke.db")
db = conn.cursor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/taxons/")
def get_families(**kwargs):
    base = {"title": "Family",
            "families": db.execute('''
            SELECT family, COUNT (DISTINCT genus)
            FROM fgs GROUP BY family
            ''').fetchall(),
            "f": "",
            "genera": [],
            "g": "",
            "species": [],
            "s": "",
            "summary": ""}
    base.update(kwargs)
    return render_template("display.html", **base)


@app.route("/taxons/<family>/")
def get_family_genera(family, **kwargs):
    base = {"title": "Genus",
            "f": family,
            "genera": db.execute('''
            SELECT genus, COUNT(genus)
            FROM fgs
            WHERE family=="%s"
            GROUP BY genus
            ''' % family).fetchall(),
            "summary": family}
    base.update(kwargs)
    return get_families(**base)


@app.route("/taxons/<family>/<genus>/")
def get_family_genera_species(family, genus, **kwargs):
    base = {"title": "Species",
            "g": genus,
            "species": db.execute('''
            SELECT species
            FROM fgs
            WHERE family=="%s" and genus=="%s"
            ''' % (family, genus)).fetchall(),
            "summary": genus}
    base.update(kwargs)
    return get_family_genera(family, **base)


@app.route("/taxons/<family>/<genus>/<species>/")
def selected_species(family, genus, species):
    return get_family_genera_species(family=family,
                                     genus=genus,
                                     s=species,
                                     summary=species)
