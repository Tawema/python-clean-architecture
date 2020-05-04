class ResponseSuccess(object):
    def __init__(self, value=None):
        self.value = value

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__


class ResponseFailure(object):
    VALIDATION_ERROR = 'VALIDATION_ERROR'

    def __init__(self, _type, message: str):
        self.type = _type
        self.message = message

    def __repr__(self):
        return "{} : {}".format(self._type, self.message)

    def __nonzero__(self):
        return False

    __bool__ = __nonzero__

    @classmethod
    def build_from_invalid_request(cls, request):
        result = "\n".join([
            "{} : {}".format(err['parameter'], err['message'])
            for err in request.errors
        ])
        return cls(VALIDATION_ERROR, result)
