from flask import Flask, render_template
from db import get_db, close_db
import sqlalchemy
from logger import log

app = Flask(__name__)
app.teardown_appcontext(close_db)


@app.route("/")
def index():
    return "55"


