from flask import Flask, Response
from flask_jwt_extended import JWTManager
from flask.ext.bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from app.domain.authentication.use_cases import RegisterUser
from app.infrastructure.authentication.services import TokenSessionService, BcryptHashingService
from app.infrastructure.authentication.repositories import FlaskUserRepository

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
manager = JWTManager(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


@app.route('/register', methods=['POST'])
def register():
    register_use_case = RegisterUser(
        FlaskUserRepository(BcryptHashingService()), TokenSessionService())
    result = register_use_case()
    return Response(result, mimetype="application/json", status=200)
