from flask import Flask, render_template
from db import get_db, close_db
import sqlalchemy
from logger import log
from requests import Session
import time

TOKEN = "5955602844:AAFfwmGzOaZoOClIKPtOSLkBjjbVBnpXuGY"
CHAT_ID = '6093993760'
SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
app = Flask(__name__)



@app.route("/")
def index():


    while True:
        time.sleep(60)
        requests.post(SEND_URL, json={'chat_id': CHAT_ID, 'text': 'nifty_kjhindex_data'})  
    
    return "thgrr"
