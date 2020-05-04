class SessionService:
    def store(self, user):
        raise NotImplementedError


class HashingService:
    def hash(self, to_hash):
        raise NotImplementedError

    def hash(self, hashed, to_check):
        raise NotImplementedError
