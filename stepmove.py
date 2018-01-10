#import RPi.GPIO as GPIO
import time, datetime
from time import sleep
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

#GPIO.setmode(GPIO.BCM)

a1_pin = 4
a2_pin = 17
b1_pin = 23
b2_pin = 24
e_pin = 18
delay = 0.015
steps = 200

#for door
interval = 0.1
PWMA = 5
AIN1 = 6
AIN2 = 13
STBY = 19


#GPIO.setup(e_pin, GPIO.OUT)
#GPIO.setup(a1_pin, GPIO.OUT)
#GPIO.setup(a2_pin, GPIO.OUT)
#GPIO.setup(b1_pin, GPIO.OUT)
#GPIO.setup(b2_pin, GPIO.OUT)

#GPIO.output(e_pin, 1)

#GPIO.setup(AIN1, GPIO.OUT)
#GPIO.setup(AIN2, GPIO.OUT)
#GPIO.setup(PWMA, GPIO.OUT)
#GPIO.setup(STBY, GPIO.OUT)


#def setStep(r1, r2, r3, r4):
#    GPIO.output(a1_pin, r1)
#    GPIO.output(a2_pin, r2)
#    GPIO.output(b1_pin, r3)
#    GPIO.output(b2_pin, r4)

def opendoor():
  print "Test test";
#    (GPIO.output(AIN1, GPIO.HIGH))
#    (GPIO.output(AIN2, GPIO.LOW))
#    (GPIO.output(PWMA, GPIO.HIGH))
#    (GPIO.output(STBY, GPIO.HIGH))
    #sleep
  sleep(0.2);
#    (GPIO.output(AIN1, GPIO.LOW))
#    (GPIO.output(AIN2, GPIO.LOW))
#    (GPIO.output(PWMA, GPIO.LOW))
#    (GPIO.output(STBY, GPIO.LOW))

def closedoor():
    (GPIO.output(AIN1, GPIO.LOW))
    (GPIO.output(AIN2, GPIO.HIGH))
    (GPIO.output(PWMA, GPIO.HIGH))
    (GPIO.output(STBY, GPIO.HIGH))
    #sleep
    sleep(0.2)
    (GPIO.output(AIN1, GPIO.LOW))
    (GPIO.output(AIN2, GPIO.LOW))
    (GPIO.output(PWMA, GPIO.LOW))
    (GPIO.output(STBY, GPIO.LOW))



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/open", methods = ['POST'])
def dooropen():
    opendoor()
    return render_template('index.html')


@app.route("/close", methods = ['POST'])
def doorclose():
    closedoor()
    return render_template('index.html')

@app.route("/camera")
def cam():
    return render_template('camera.html')

@app.route("/left", methods = ['POST'])
def moveleft():
    for i in range(0, steps):
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)

        return render_template('camera.html')

@app.route("/right", methods = ['POST'])
def moveright():
    for i in range(0, steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(1, 0, 1, 0)
        time.sleep(delay)

        return render_template('camera.html')

@app.route("/notification")
def ntify():
  today = datetime.date.today()
  glog = open('/var/log/syslog', 'r')
  file_n = (list(glog)[-1])
  tim = time.strftime("%H:%M:%S")
  dat = time.strftime("%d/%m/%Y")
  logdate = tim + " " + dat + ": " + file_n

  return render_template('notify.html', ja = logdate)





if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=4000, debug=True)
    except KeyboardInterrupt:
       #GPIO.cleanup()
        server.stop()

