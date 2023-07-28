
import time
import threading

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'World!'

def web():
    app.run(debug=True, use_reloader=False)

def usb():
    print(f"this is how to pass arguments to a thread function")
    while True:
        print("waiting for USB")
        time.sleep(2)

if __name__ == '__main__':
    threading.Thread(target=web, daemon=True).start()
    threading.Thread(target=usb, daemon=True).start()
    while True:
        time.sleep(1)
