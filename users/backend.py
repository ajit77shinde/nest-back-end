from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend



class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
            print(f"User retrieved from database: {user}")
        except UserModel.DoesNotExist:
            print(f"User with email {username} not found in database.")
            return None
        else:
            if user.check_password(password):
                print(f"Password is correct for user {user}")
                return user
            else:
                print(f"Incorrect password for user {user}")
        return None
def authenticate(request, username=None, password=None, **kwargs):
    backend = EmailBackend()
    return backend.authenticate(request, username, password, **kwargs)