from project import login_manager
from project.models.models import *
from project.config.crypto import Crypto

@login_manager.user_loader
def load_user(user_id):
    return RegUser.query.get(int(user_id))


def register(form):
    secret_password = Crypto.convertPassword(form.password.data)
    print(secret_password)
    user = RegUser.query.filter_by(email=form.email.data+"@itu.edu.tr").first()
    if user:
        return False        # email already taken
    else:
        print("Oldu")
        return True
    user = User(name=form.name.data, surname=form.surname.data, email=form.email.data+"@itu.edu.tr", password=secret_password, user_type=form.user_type.data)
    return 


