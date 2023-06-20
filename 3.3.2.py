def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as u:
        print('Only over 18 can be invited')
    else:
        print("You should send an invite to " + name)


class UnderAge(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return "Your age is {} and you are under 18. In {} years you will be able to rache Ido's birthday". format(self._age, int(18 - self._age))

    def get_age(self):
        return self._age


send_invitation('Yanki', 18)