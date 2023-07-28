
import time
import threading
import logging


from flask import Flask
logger = logging.getLogger("logger.log")

app = Flask(__name__)

@app.route('/')
def hello_world():
    logger.info('gfgf')
    return '9999!'

def web():
    logger.info('gfgf')
    app.run(debug=True, use_reloader=False)

def usb():
    print(f"this is how to pass arguments to a thread function")
    while True:
        logger.info('tessdlkdskdsckj')
        print("waiting for USB")
        time.sleep(2)

if __name__ == '__main__':
    threading.Thread(target=web, daemon=True).start()
    threading.Thread(target=usb, daemon=True).start()
    while True:
        time.sleep(1)
