__author__ = 'cmgiler'

class UserError(Exception):
    def __init__(self, message):
        self.message = message

class UserNotExistsError(UserError):
    pass # Inherits from UserError

class IncorrectPasswordError(UserError):
    pass # Inherits from UserError

class UserAlreadyRegisteredError(UserError):
    pass

class InvalidEmailError(UserError):
    pass