from flask import Flask, jsonify, request
import requests
import sys

app = Flask(__name__)

# Base URL of your Django API
BASE_URL = "http://127.0.0.1:8000/api/"

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        response = requests.get(BASE_URL + 'tasks/')
        return jsonify(response.json())
    elif request.method == 'POST':
        data = request.json
        response = requests.post(BASE_URL + 'tasks/', json=data)
        return jsonify(response.json()), response.status_code

@app.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def task(task_id):
    if request.method == 'GET':
        response = requests.get(BASE_URL + f'tasks/{task_id}/')
        return jsonify(response.json())
    elif request.method == 'PUT':
        data = request.json
        response = requests.put(BASE_URL + f'tasks/{task_id}/', json=data)
        return jsonify(response.json()), response.status_code
    elif request.method == 'DELETE':
        response = requests.delete(BASE_URL + f'tasks/{task_id}/')
        return '', response.status_code

if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        app.run(debug=True, port=port)
    else:
        port = 5000  # Default port
        app.run(debug=True, port=port)
    
    print(f"Flask app is running on port {port}")


# python app.py <port_number>

# Replace <port_number> with the desired port number.
# If you run the app without specifying a port number, it will default to port 5000.
