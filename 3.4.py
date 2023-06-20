import string


def check_password(password):
    new_list = ['digit', 'lowercase', 'uppercase', 'special']
    for char in password:
        try:
            if char.isdigit():
                new_list.remove('digit')
            elif char.islower():
                new_list.remove('lowercase')
            elif char.isupper():
                new_list.remove('uppercase')
            elif char in string.punctuation:
                new_list.remove('special')
        except ValueError:
            pass
    return new_list


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, index):
        self._char = char
        self._index = index

    def __str__(self):
        return "The username contains an illegal character {} at index {}".format(self._char, self._index)


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class PasswordMissingCharacterDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingCharacterLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingCharacterSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


def check_input(username, password):
    try:
        for i in range(len(username)):
            if not username[i].isdigit() and not username[i].isalpha() and username[i] != '_':
                raise UsernameContainsIllegalCharacter(username[i], i)
        if len(username) < 3:
            raise UsernameTooShort(username)
        elif len(username) > 16:
            raise UsernameTooLong(username)
        elif len(password) < 8:
            raise PasswordTooShort(password)
        elif len(password) > 40:
            raise PasswordTooLong(password)
        elif len(check_password(password)) != 0:
            if 'uppercase' in check_password(password):
                raise PasswordMissingUppercase
            elif 'lowercase' in check_password(password):
                raise PasswordMissingCharacterLowercase
            elif 'digit' in check_password(password):
                raise PasswordMissingCharacterDigit
            elif 'special' in check_password(password):
                raise PasswordMissingCharacterSpecial
        else:
            print('OK')
    except UsernameContainsIllegalCharacter as a:
        print(a)
    except UsernameTooLong as b:
        print(b)
    except UsernameTooShort as c:
        print(c)
    except PasswordTooShort as d:
        print(d)
    except PasswordTooLong as e:
        print(e)
    except PasswordMissingCharacter as f:
        print(f)


def main():
    admin = input('Enter a user name: ')
    password1 = input('Enter a password: ')
    check_input(admin, password1)


if __name__ == '__main__':
    main()


