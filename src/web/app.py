

from flask import *

app = Flask(__name__)

x=2

def go():
	while True:
		print("8")

@app.route('/')
def root():
	return 'index.hhhtml'

if __name__ == '__main__':

	
	#thread.start_new_thread(go, ())
      #  app.run(host='0.0.0.0', debug=True, threaded=True)
         app.run()
