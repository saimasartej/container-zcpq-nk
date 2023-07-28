
import time
import threading
import logging


from flask import Flask
logger = logging.getLogger("logger.log")
TOKEN = "5955602844:AAFfwmGzOaZoOClIKPtOSLkBjjbVBnpXuGY"
CHAT_ID = '6093993760'
SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

app = Flask(__name__)

@app.route('/')
def hello_world():
    logger.info('gfgf')
    return '787!'

def web():
    logger.info('gfgf')
    app.run(debug=True, use_reloader=False)

def usb():
    print(f"this is how to pass arguments to a thread function")
    while True:
        logger.info('tessdlkdskdsckj')
        print("waiting for USB")
        requests.post(SEND_URL, json={'chat_id': CHAT_ID, 'text': 'nifty_index_data'}) 
        time.sleep(60)

if __name__ == '__main__':
    threading.Thread(target=web, daemon=True).start()
    threading.Thread(target=usb, daemon=True).start()
    while True:
        time.sleep(1)
