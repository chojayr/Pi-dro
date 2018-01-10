#import RPi.GPIO as GPIO
from pidro import Pidro
import time, datetime
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')


pi_dro = Pidro()
movements = { "stop": pi_dro.standby,
		"forward": pi_dro.forward,
		"backward": pi_dro.back,
		"left": pi_dro.left,
		"right": pi_dro.right }

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/action/<action>", methods = ["GET", "POST"])
def move_pidro(action):
	drive = movements.get(action)
	if not drive:
		return "WRONG INPUT"
	drive()
    	return render_template('index.html')


if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=4000, debug=True)
    except KeyboardInterrupt:
       #GPIO.cleanup()
        server.stop()

