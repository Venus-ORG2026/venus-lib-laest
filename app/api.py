from app.auth import login_user, register_user

class Api:
    def login(self, email, password):
        return login_user(email, password)

    def register(self, email, password):
        return register_user(email, password)
