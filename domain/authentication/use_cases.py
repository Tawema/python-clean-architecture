import bouka.shared.response as res
from bouka.shared.use_case import UseCase
from .entities import User


class RegisterUser(UseCase):
    def __init__(self, user_repo, session_service):
        self.user_repo = user_repo
        self.session_service = session_service

    def process_request(self, request):
        if user_repo.exists_with_email(request.email):
            return res.ResponseFailure.build_from_error_dict(
                {"email": "The email already exists in the database"})
        user = User.from_dict(request.attributes)
        user_repo.save(user)
        result = session_service.store(user)
        return res.ResponseSuccess(result)
