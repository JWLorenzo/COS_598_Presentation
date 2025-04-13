import socket
from flask import Flask, request
import requests
import redis

app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379, decode_responses=True)


@app.route("/", methods=["POST"])
def validate():
    username = request.form.get("username")
    password = request.form.get("password")

    user_key = f"user:{username}"
    if cache.exists(user_key):
        role, password_db = cache.hmget(user_key, ["role", "password"])
        if password_db == password:
            return f"Hiya {username}! Your role is: {role}"
        else:
            return "Incorrect credentials.", 401
    else:
        return "User not found.", 401


@app.route("/create-user", methods=["POST"])
def create_user():
    username = request.form.get("username")
    password = request.form.get("password")
    role = request.form.get("role")

    user_db = f"user:{username}"
    if cache.exists(user_db):
        return f"User {username} exists", 400
    cache.hset(user_db, mapping={"password": password, "role": role})
    return f"User '{username}' registered"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
