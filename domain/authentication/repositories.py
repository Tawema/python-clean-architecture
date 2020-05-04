class UserRepository:
    def save(self, user):
        raise NotImplementedError

    def exists_with_email(self, email: str) -> bool:
        raise NotImplementedError
