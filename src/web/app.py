

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

if __name__ == '__main__':

	
	#thread.start_new_thread(go, ())
      #  app.run(host='0.0.0.0', debug=True, threaded=True)
         app.run()
