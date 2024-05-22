from .auth.router import fastapi_users_

class OptionalCurrentUser:
    """
    Callable object, returns current user if the user is authorised, otherwise
    returns None.
    """

    def __call__(self):
        return fastapi_users_.current_user(optional=True)