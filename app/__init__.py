from flask import Flask, Response, request
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
manager = JWTManager(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


@app.route('/register', methods=['POST'])
def register():
    from app.domain.authentication.use_cases import RegisterUser
    from app.infrastructure.authentication.services import TokenSessionService, BcryptHashingService
    from app.infrastructure.authentication.repositories import FlaskUserRepository
    from app.shared.request import RegisterUserRequest
    register_use_case = RegisterUser(
        FlaskUserRepository(BcryptHashingService()), TokenSessionService())
    result = register_use_case(
        RegisterUserRequest.build_from_dict(request.json))
    return Response(json.dumps(result.value),
                    mimetype="application/json",
                    status=200)
