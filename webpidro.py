import RPi.GPIO as GPIO
from pidro import Pidro
import time, datetime
import picamera
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')


pi_dro = Pidro()
movements = { "stop": pi_dro.standby,
		"forward": pi_dro.forward,
		"backward": pi_dro.back,
		"left": pi_dro.left,
		"right": pi_dro.right }


def capture():
	camera = picamera.PiCamera()
        camera.resolution = (1024, 768)
        time.sleep(3)
        camera.capture('/home/pi/pidro/static/img/capture.jpg')
	camera.close()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/camera")
def cam():
    return render_template('camera.html')

@app.route("/action/<action>", methods = ["GET", "POST"])
def move_pidro(action):
	drive = movements.get(action)
	if not drive:
		return "WRONG INPUT"
	drive()
    	return render_template('index.html')

@app.route("/camera/capture", methods = ["POST"])
def camera():
	capture()
	return render_template('camera.html')

## Main
if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=4000, debug=True)
    except KeyboardInterrupt:
	GPIO.cleanup()
        server.stop()
