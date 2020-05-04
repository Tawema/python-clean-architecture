class ValidRequest(object):
    @classmethod
    def from_dict(cls, adict):
        raise NotImplementedError

    def __nonzero__(self):
        return True


class InvalidRequest(object):
    errors = []

    def has_errors(self):
        return len(errors) > 0

    def add_error(self, parameter: str, message: str):
        errors.append({'parameter': parameter, 'message': message})

    def __nonzero__(self):
        return False

    __bool__ = __nonzero__


class RegisterUserRequest(ValidRequest):
    def __init__(self, adict):
        pass

    @classmethod
    def from_dict(cls, adict):
        return RegisterUserRequest(adict)

    @classmethod
    def build_from_dict(cls, adict):
        invalid_request = InvalidRequest()
        if adict['username'] is None or adict['username'] == '':
            invalid_request.add_error("username",
                                      "The username cannot be empty")

        if adict['email'] is None or adict['email'] == '' or "@" not in adict[
                'email']:
            invalid_request.add_error("email", "The email is invalid")

        if adict['password'] is None or adict['password'] == '' or len(
                adict['password']) < 6:
            invalid_request.add_error("password", "The password is weak")

        if invalid_request.has_errors():
            return invalid_request

        return RegisterUserRequest(adict)
