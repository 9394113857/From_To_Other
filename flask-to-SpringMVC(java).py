from flask import Flask, jsonify, Response
import requests
import sys

app = Flask(__name__)

BASE_URL = 'http://localhost:8080'

def make_request(endpoint, method='GET', data=None):
    url = f'{BASE_URL}{endpoint}'
    response = requests.request(method, url, json=data)
    try:
        response_data = response.json()
    except ValueError:
        response_data = response.text
    return response_data, response.status_code

@app.route('/get_users', methods=['GET'])
def get_users():
    response_data, status_code = make_request('/users')
    return jsonify_response(response_data, status_code)

@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    response_data, status_code = make_request(f'/users/{user_id}')
    return jsonify_response(response_data, status_code)

@app.route('/create_user', methods=['POST'])
def create_user():
    new_user = {
        "username": "newuser",
        "email": "newuser@example.com"
    }
    response_data, status_code = make_request('/users', method='POST', data=new_user)
    return jsonify_response(response_data, status_code)

@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user = {
        "username": "updateduser",
        "email": "updated@example.com"
    }
    response_data, status_code = make_request(f'/users/{user_id}', method='PUT', data=updated_user)
    return jsonify_response(response_data, status_code)

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    response_data, status_code = make_request(f'/users/{user_id}', method='DELETE')
    return jsonify_response(response_data, status_code)

def jsonify_response(data, status_code):
    if isinstance(data, Response):
        data = data.text
    return jsonify({
        "data": data,
        "status_code": status_code
    }), status_code

if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000

    app.run(port=port, debug=True)
