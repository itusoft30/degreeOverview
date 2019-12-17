from project import login_manager
from project.models.models import *

@login_manager.user_loader
def load_user(user_id):
    return RegUser.query.get(int(user_id))

