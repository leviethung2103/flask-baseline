from flask import Flask, request
import flask
import json
from flask_cors import CORS
from config import *
from flask_socketio import SocketIO, emit, send
import eventlet
eventlet.monkey_patch()


app = flask.Flask(__name__)
socketio =  SocketIO(app,cors_allowed_origins="*",async_mode='eventlet')

# For Production
app.config.from_object('config.ProdConfig')

# For Development
# app.config.from_object('config.DevConfig')

CORS(app)

@app.route('/')
def homepage():
    return 'Welcome to Homepage'

@app.route('/config',methods=["POST"])
def receive_config():
    json_data = flask.request.json

    # DEBUG
    # print (json_data)
    # print (type(json_data['camera']))
    # print (json_data['camera'][0])
    # print(json_data['camera'][1])

    response = save_json(data=json_data,
              dst_path='camera.json')
    return flask.jsonify(response)

## SocketIO Part
@socketio.on('connect',namespace='/web')
def connect_web():
    print (f"[INFO] Web client connected: {request.sid}")

@socketio.on('disconnect',namespace='/web')
def disconnect_web():
    print (f"[INFO] Web client disconnected: {request.sid}")

def save_json(data,dst_path):
    with open(dst_path,'w') as file:
        json.dump(data,file)

    return {"success": True}


if __name__ == '__main__':
    print ("[INFO] Started the server.")
    socketio.run(app=app,
                 host=HOST,
                 port=PORT)