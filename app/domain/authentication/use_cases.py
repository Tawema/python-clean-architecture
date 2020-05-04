import app.shared.response as res
from app.shared.use_case import UseCase
from .entities import User


class RegisterUser(UseCase):
    def __init__(self, user_repo, session_service):
        self.user_repo = user_repo
        self.session_service = session_service

    def process_request(self, request):
        if self.user_repo.exists_with_email(request.email):
            return res.ResponseFailure.build_from_error_dict(
                {"email": "The email already exists in the database"})
        user = User.from_dict(request.attributes)
        self.user_repo.save(user)
        result = self.session_service.store(user)
        return res.ResponseSuccess(result)


class LogUserIn(UseCase):
    def __init__(self, user_repo, session_service):
        self.user_repo = user_repo
        self.session_service = session_service

    def process_request(self, request):
        user = self.user_repo.get_user_with_email_and_password(
            request.email, request.password)
        if not user:
            return res.ResponseFailure.build_from_error_dict(
                {"email": "Your credentials does not match our records"})
        result = self.session_service.store(user)
        return res.ResponseSuccess(result)
