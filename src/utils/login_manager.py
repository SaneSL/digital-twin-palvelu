from flask_login import LoginManager
from utils.models import Customer

login_manager = LoginManager()
login_manager.login_message = "Please log in"
login_manager.login_message_category = 'info'
login_manager.login_view = 'home.login'


@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(user_id)
