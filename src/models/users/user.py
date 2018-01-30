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

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that an e-mail/password combo (as sent by the sitr forms) is valid or not.
        Checks taht the e-mail exists, and that the password associate to that e-mail is correct.
        :param email: The user's e-mail
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """
        user_data = Database.find_one("users", {"email": email})  # password in sha512 -> pbkdf2_sha512

        if user_data is None:
            # Tell the user that their email does not exist
            raise UserErrors.UserNotExistError("Username does not exist or invalid.")

        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell the user that their password is incorrect
            raise UserErrors.IncorrectPasswordError("Password is incorrect.")

        return True

