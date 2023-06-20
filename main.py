import re
import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The username contains an illegal character"

    def get_arg(self):
        return self._arg


class UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The username is too short"

    def get_arg(self):
        return self._arg


class UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The username is too long"

    def get_arg(self):
        return self._arg


class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The password is missing a character"

    def get_arg(self):
        return self._arg


class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The password is too short"

    def get_arg(self):
        return self._arg


class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The password is too long"

    def get_arg(self):
        return self._arg


def check_input(username, password):
    if len(username) < 3:
        raise UsernameTooShort(username)
    elif len(username) > 16:
        raise UsernameTooLong(username)
    elif len(password) < 8:
        raise PasswordTooShort(password)
    elif len(password) > 40:
        raise PasswordTooLong(password)
    elif not all(char.isalnum() or char == "_" for char in username):
        raise UsernameContainsIllegalCharacter(username)
    elif not all(re.search(pattern, password) for pattern in [r'[A-Z]', r'[a-z]', r'[\W_]']):
        raise PasswordMissingCharacter(password)
    else:
        print("OK")




def main():
    username = input("Please enter user name: ")
    password = input("Please enter a password: ")
    check_input(username, password)


main()
    

