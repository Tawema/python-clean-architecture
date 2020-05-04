from flask_jwt_extended import create_access_token, create_refresh_token
from app import bcrypt
from app.domain.authentication.services import SessionService, HashingService


class TokenSessionService(SessionService):
    def store(self, user):
        access_token = create_access_token(identity=user.email, fresh=True)
        refresh_token = create_refresh_token(identity=user.email, fresh=True)
        return {'access_token': access_token, 'refresh_token': refresh_token}


class BcryptHashingService(HashingService):
    def hash(self, to_hash):
        return bcrypt.generate_password_hash(to_hash)

    def check(self, hashed, to_check):
        return bcrypt.check_password_hash(hashed, to_check)
