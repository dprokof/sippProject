import websocket
import json
import time

kurento_url = "ws://kurento:8888/kurento"

ws = websocket.create_connection(kurento_url)

def create_pipeline():
    request = {
        "id": 1,
        "method": "create",
        "params": {
            "type": "MediaPipeline"
        }
    }
    ws.send(json.dumps(request))
    response = json.loads(ws.recv())
    print(response)
    return response["result"]["id"]

def create_webrtc_endpoint(pipeline_id):
    request = {
        "id": 2,
        "method": "create",
        "params": {
            "type": "WebRtcEndpoint",
            "mediaPipeline": pipeline_id
        }
    }
    ws.send(json.dumps(request))
    response = json.loads(ws.recv())
    return response["result"]["id"]

def create_recorder_endpoint(pipeline_id):
    request = {
        "id": 3,
        "method": "create",
        "params": {
            "type": "RecorderEndpoint",
            "mediaPipeline": pipeline_id,
            "file": "file:///tmp/recording.mp4"
        }
    }
    ws.send(json.dumps(request))
    response = json.loads(ws.recv())
    return response["result"]["id"]

def connect_endpoints(webrtc_id, recorder_id):
    request = {
        "id": 4,
        "method": "connect",
        "params": {
            "src": webrtc_id,
            "dst": recorder_id
        }
    }
    ws.send(json.dumps(request))
    ws.recv()

def start_recording():
    request = {
        "id": 5,
        "method": "record",
        "params": {
            "endpoint": recorder_id
        }
    }
    ws.send(json.dumps(request))
    ws.recv()

def stop_recording():
    request = {
        "id": 6,
        "method": "stop",
        "params": {
            "endpoint": recorder_id
        }
    }
    ws.send(json.dumps(request))
    ws.recv()

def close_connection():
    ws.close()

if __name__ == "__main__":
    try:
        pipeline_id = create_pipeline()

        webrtc_id = create_webrtc_endpoint(pipeline_id)
        recorder_id = create_recorder_endpoint(pipeline_id)

        connect_endpoints(webrtc_id, recorder_id)

        start_recording()

        time.sleep(60)

        stop_recording()

    finally:
        close_connection()
