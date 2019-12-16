from project.models.models import *
from project.config import __all__ as config

@config.login_manager.user_loader
def load_user(user_id):
    return RegUser.query.get(int(user_id))