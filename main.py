
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory, jsonify, json
from camera import VideoCamera
import os
import RPi.GPIO as GPIO
pi_camera = VideoCamera(flip=False)  # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)
speed = 3  # default speed
controls = {
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0
}  # default controls


@app.route('/')
def index():
    return render_template('index.html')  # you can customze index.html here


def gen(camera):
    # get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/controls', methods=['POST'])
def control():

    direction = request.form.get('direction')
    print(direction)
    last_direction = None
    controls = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
    if direction == 'up':
        controls['up'] = 1
        last_direction = 'up'
    elif direction == 'down':
        controls['down'] = 1
        last_direction = 'down'
    elif direction == 'left':
        controls['left'] = 1
        last_direction = 'left'
    elif direction == 'right':
        controls['right'] = 1
        last_direction = 'right'
    elif direction == 'stop':
        controls['last_direction'] = 0
    # converting list to array
    control_array = list(controls.values())
    print(control_array)
    # sending the array to the arduino


# Set up GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(1, GPIO.OUT)  # for speed control

    # Send data over GPIO pins
    # send speed once
    GPIO.output(1, speed)
    for i, val in enumerate(control_array):
        GPIO.output(control_array[i], val)

    return direction


@app.route('/speed', methods=['POST'])
def update_speed():
    data = request.form.get('speed')
    speed = data
    # Update your speed variable here
    # update speed whenever it is changed
    GPIO.output(1, speed)
    return jsonify({'message': 'Speed updated successfully'})


@app.route('/demo', methods=['GET', 'POST'])
def demo():
    return render_template('controller_demo.html')


if __name__ == '__main__':
    # add try finallly block to clean up GPIO
    try:
        app.run(host='0.0.0.0', debug=True, threaded=True)
    finally:
        GPIO.cleanup()  # clean up GPIO on normal exit
