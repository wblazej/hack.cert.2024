from flask import Flask, request, render_template
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "turtlerocks"

jwt = JWTManager(app)

@app.route('/')
def login():
    username = request.args.get('u')
    access_token = create_access_token(identity=username)
    return access_token

@app.route('/test')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5003, debug=True)
