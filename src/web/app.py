
from threading import Thread
from flask import *

app = Flask(__name__)

x=2

def go():
	while True:
		print("8")

@app.route('/')
def root():
	return 'index.'

if __name__ == '__main__':

	
	  thread = Thread(target=go, ())
	  thread.start()
	  thread.start()
         #app.run(debug=True, threaded=True)
          app.run(debug=True,threaded=True)
