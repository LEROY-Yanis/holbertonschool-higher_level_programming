#!/usr/bin/python3
"""Flask API with Basic HTTP Authentication and JWT."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    """Verify username and password."""
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None

@auth.error_handler
def unauthorized():
    """Handle unauthorized access."""
    return jsonify({"error": "Unauthorized access"}), 401

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid JWT token."""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token."""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired JWT token."""
    return jsonify({"error": "Token has expired"}), 401

@app.route("/")
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Protected route requiring Basic Authentication."""
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    """Login endpoint to get JWT token."""
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid credentials"}), 401

    username = data["username"]
    password = data["password"]

    if username not in users or not check_password_hash(
            users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )
    return jsonify({"access_token": access_token})

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Protected route requiring JWT Authentication."""
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Admin-only route requiring admin role."""
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run()
