from app.run import db
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
        return FlaskUser.create(username=user.username,
                                email=user.email,
                                password=self.hashing_service.hash(
                                    user.password))

    def exists_with_email(self, email: str) -> bool:
        return len(FlaskUser.query.filter_by(email=email)) > 0

    def get_user_with_email_and_password(self, email: str,
                                         password: str) -> User:
        user = FlaskUser.query.filter_by(email=email).first()
        if user:
            return self.hashing_service.check(user.password, password)
        return None
