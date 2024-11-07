from flask import Flask, jsonify, request
import requests
import sys

app = Flask(__name__)

FASTAPI_BASE_URL = "http://127.0.0.1:5000"  # Update with your FastAPI server's URL

# @app.route('/mobiles', methods=['GET'])
# def get_mobiles_flask():
#     response = requests.get(f"{FASTAPI_BASE_URL}/mobiles")
#     return jsonify(response.json())

@app.route('/', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        response = requests.get(FASTAPI_BASE_URL + 'mobiles/')
        return jsonify(response.json())
    elif request.method == 'POST':
        data = request.json
        response = requests.post(FASTAPI_BASE_URL + 'tasks/', json=data)
        return jsonify(response.json()), response.status_code

@app.route('/mobiles/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def task(task_id):
    if request.method == 'GET':
        response = requests.get(FASTAPI_BASE_URL + f'tasks/{task_id}/')
        return jsonify(response.json())
    elif request.method == 'PUT':
        data = request.json
        response = requests.put(FASTAPI_BASE_URL + f'tasks/{task_id}/', json=data)
        return jsonify(response.json()), response.status_code
    elif request.method == 'DELETE':
        response = requests.delete(FASTAPI_BASE_URL + f'tasks/{task_id}/')
        return '', response.status_code





if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000  # Default port if not provided
        
    app.run(debug=True, port=port)

# python your_flask_app.py 8080
# In the above command, 
# 8080 is the port number you want to use. 
# If you don't provide a port number, it will default to 8000.
