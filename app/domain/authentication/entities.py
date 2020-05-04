class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def from_dict(cls, adict):
        return cls(username=adict['username'],
                   email=adict['email'],
                   password=adict['password'])
