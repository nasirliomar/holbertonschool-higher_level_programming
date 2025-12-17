#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Users stored in memory: { "username": {user_object} }
# NOTE: Do not add testing data here (checker requirement).
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    # Return list of usernames
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # If body is not valid JSON => 400 Invalid JSON
    try:
        payload = request.get_json(force=False, silent=False)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if payload is None:
        # Happens when Content-Type isn't JSON or body can't be parsed
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Build user object (store full object; include username)
    user_obj = {
        "username": username,
        "name": payload.get("name"),
        "age": payload.get("age"),
        "city": payload.get("city"),
    }

    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    app.run()
