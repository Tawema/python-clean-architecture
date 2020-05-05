class SessionService:
    def store(self, user):
        raise NotImplementedError


class HashingService:
    def hash(self, to_hash):
        raise NotImplementedError

    def check(self, hashed, to_check):
        raise NotImplementedError
