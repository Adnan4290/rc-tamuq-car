
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory
# from camera import VideoCamera
import os

# pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.
pi_camera = None

# App Globals (do not edit)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  # you can customze index.html here


def gen(camera):
    # #get camera frame
    # while True:
        # frame = camera.get_frame()
        # yield (b'--frame\r\n'
            #    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
   return None


@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


controls = {
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0
}


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
    print(controls)

    return 'OK'

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True, threaded=True)
