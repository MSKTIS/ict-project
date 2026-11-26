from flask import Flask, jsonify

import database as db

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/users")
def getUsers():
    users = db.getUsers()
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
