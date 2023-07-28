

from flask import *

app = Flask(__name__)

x=2

def go():
	while True:
		print("8")

@app.route('/')
def root():
	return 'index.hhhtmlyyyyrtrtrtr'

if __name__ == '__main__':

	
	  thread.start_new_thread(go, ())
         #app.run(debug=True, threaded=True)
          app.run(debug=True,threaded=True)
