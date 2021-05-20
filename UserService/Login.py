from flask_login import LoginManager
import ChanceUtiles as Utiles
from UserService import User
from App import app


login_manager = LoginManager()


class Login:
    @app.route(Utiles.LOGIN, methods=[Utiles.GET, Utiles.POST])
    def __init__(self):
        """
        the main login function
        """
        login_manager.init_app(app)
        return

    @login_manager.user_loader
    def load_user(self, user_id):
        return User.get
