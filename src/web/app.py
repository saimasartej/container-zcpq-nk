
import random
from decimal import Decimal
# Import flask library.
from flask import *

app = Flask(__name__)


x=2

def go():



    while True:
        global x

        x=random.uniform(20.20, 30.00)
        x=Decimal(x)
        x=round(x,2)
	print x
        time.sleep(2)
        


@app.route('/')
def root():
	return render_template('index.html')


@app.route('/_add')
def add_numbers():
    a = ["27-04-2017 20:43:11",1,1,7,72.64,49.64,72.12,35.32,28.74,36.18,84.65,19.35,76.15,"0:48:13","141:41:45","72:16:42","0:15:42"]

    a[6]=x
    return jsonify(a)


if __name__ == '__main__':

	
	thread.start_new_thread(go, ())
	app.run(host='0.0.0.0', debug=True, threaded=True)
