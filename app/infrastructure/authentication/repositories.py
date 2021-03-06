from app import db
from app.domain.authentication.entities import User
from app.domain.authentication.repositories import UserRepository


class FlaskUser(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)


class FlaskUserRepository(UserRepository):
    def __init__(self, hashing_service):
        self.hashing_service = hashing_service

    def save(self, user):
        user = FlaskUser(username=user.username,
                         email=user.email,
                         password=self.hashing_service.hash(user.password))
        db.session.add(user)
        db.session.commit()
        return user

    def exists_with_email(self, email: str) -> bool:
        return FlaskUser.query.filter_by(email=email).count() > 0

    def get_user_with_email_and_password(self, email: str,
                                         password: str) -> User:
        user = FlaskUser.query.filter_by(email=email).first()
        if not user:
            return None

        if self.hashing_service.check(user.password, password):
            return user

        return None
