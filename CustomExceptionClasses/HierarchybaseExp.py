class UserError(Exception):
    pass

class InvalidEmailError(UserError):
    pass

class InvalidPasswordError(UserError):
    pass

class UserNotFoundError(UserError):
    pass

class DuplicateUserError(UserError):
    pass


def register_user(email):
    if "@" not in email:
        raise InvalidEmailError(f"'{email}' is not valid")

try:
    register_user("bademail")
except UserError as e:            
    print(f"User error occurred: {e}")  