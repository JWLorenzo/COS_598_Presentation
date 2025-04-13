import socket
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    response = requests.post(
        "http://nginx/validate/", data={"username": username, "password": password}
    )
    return f"Response from backend: {response.text}", response.status_code


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    role = request.form.get("role")

    response = requests.post(
        "http://nginx/create-user",
        data={"username": username, "password": password, "role": role},
    )
    return f"Registration response: {response.text}", response.status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
