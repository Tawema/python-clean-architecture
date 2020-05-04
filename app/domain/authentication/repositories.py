class UserRepository:
    def save(self, user):
        raise NotImplementedError

    def exists_with_email(self, email: str) -> bool:
        raise NotImplementedError

    def get_user_with_email_and_password(self, email: str,
                                         password: str) -> User:
        raise NotImplementedError
