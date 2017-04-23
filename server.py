import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
conn = sqlite3.connect("duke/duke.db")
db = conn.cursor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/family/")
def get_families():
    return render_template("family.html",
                           title="Families",
                           results=db.execute('''
                           SELECT family, COUNT(family)
                           FROM fgs GROUP BY family
                           ''').fetchall())

# Add bootstrap, split into 4
# Create a template for the table
# Add routes for family to species
# Pickle objects for this
