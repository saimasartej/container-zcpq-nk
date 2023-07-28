

from flask import *

app = Flask(__name__)

x=2

def go():
	return 0
@app.route('/')
def root():
	return 'index.html'

if __name__ == '__main__':

	
	#thread.start_new_thread(go, ())
      #  app.run(host='0.0.0.0', debug=True, threaded=True)
         app.run()
