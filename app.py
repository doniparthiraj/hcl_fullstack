from flask import Flask, request, jsonify
from flask_cors import CORS
from dbhelper import db_helper 

app = Flask(__name__)
CORS(app)

@app.route('/add_bank', methods=['POST'])
def AddUser():
    data = request.json
    response = db_helper.add_bank(
        data['bank_name'],
        data['charges']
    )
    return jsonify(response), response[1] if isinstance(response, tuple) else 200


@app.route('/add_user', methods=['POST'])
def AddUser():
    data = request.json
    response = db_helper.add_user(
        data['name'],
        data['phone_number'],
        data['account_number'],
        data['balance'],
        data['bank_name']
    )
    return jsonify(response), response[1] if isinstance(response, tuple) else 200


@app.route('/link_bank', methods=['POST'])
def AddUser():
    data = request.json
    response = db_helper.link_bank(
        data['from'],
        data['to']
    )
    return jsonify(response), response[1] if isinstance(response, tuple) else 200


@app.route('/fast_route', methods=['POST'])
def FastRoute():
    data = request.json
    response = check(data)
    response = find_fastroute(data["from"],data["to"])
    return jsonify(response), response[1] if isinstance(response, tuple) else 200

if __name__ == '__main__':
    app.run(debug=True)