__author__ = 'cmgiler'

import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod  # Checking if email and password are valid
    def is_login_valid(email, password):
        """
        This method verifies that an e-mail/password combo (as sent by the site forms) is valid or not.
        Checks that the e-mail exists, and that the password associated to that e-mail is correct.
        :param email: The user's e-mail (string)
        :param password: A sha512 hashed password (encrypted)
        :return: True if valid, False otherwise
        """
        user_data = Database.find_one('users', {'email': email})  # Password in sha512 -> pbkdf2_sha512
        if user_data is None:
            # Tell user that their email doesn't exist
            raise UserErrors.UserNotExistsError("Your user does not exist.")
        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell user that their password is wrong
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")
        return True

    @staticmethod
    def register_user(email, password):
        """
        This method registers a user using email and password.
        The password already comes hashed as sha-512.
        :param email: user's email (might be invalid)
        :param password: sha512-hashed password
        :return: True if registered successfully, or False otherwise (exceptions can also be raised)
        """

        user_data = Database.find_one('users', {'email': email})

        if user_data is not None:
            # Tell user they are already registered
            raise UserErrors.UserAlreadyRegisteredError("The email that you used to register already exists.")

        if not Utils.email_is_valid(email):
            # Tell user that their email is not constructed properly.
            raise UserErrors.InvalidEmailError("The email format is invalid")

        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert('users', self.json())

    def json(self):
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }