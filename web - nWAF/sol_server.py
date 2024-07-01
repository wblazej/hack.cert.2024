from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager
from flask import Flask, request

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = (126).to_bytes(16, 'big')
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
jwt = JWTManager(app)


@app.route("/get_token", methods=["POST"])
def get_token():
    content = request.get_json()['content']
    return create_access_token(identity=content)


if __name__ == '__main__':
    app.run(port=5002)
