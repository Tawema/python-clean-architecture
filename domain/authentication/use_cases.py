import bouka.shared.response as res


class RegisterUser:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def __call__(self, request):
        if not request:
            return res.ResponseFailure.build_from_invalid_request(request)
