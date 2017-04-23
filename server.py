from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/family/")
def get_families():
    return render_template("family.html",
                           title="Families",
                           results=["first", "second", "third"])

# Add bootstrap, split into 4
# Create a template for the table
# Add routes for family to species
# Pickle objects for this
