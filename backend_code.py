import datetime
import json


class Exception:

    def only_int(self):
        try:
            a = int(input("Enter a number: "))
        except ValueError:
            print("It must be an integer number. Try again")
            return self.only_int()
        return a

    def only_float(self):
        try:
            a = float(input("Enter a float number: "))
        except ValueError:
            print("It must be a float number. Try again")
            return self.only_float()
        return a

    @staticmethod
    def only_str(arg):
        return all([char.isalpha() for char in arg])

    def more_than_single_str(self):
        a = input("Enter more than single srting.: ").title()
        if all(x.isalpha() for x in a.split()):
            return a
        else:
            print("You should enter only words. Try again!")
            return self.more_than_single_str()

    def more_than_one_number(self):
        a = input("Enter many numbers: ")
        if all(x.isdigit() for x in a.split()):
            a = [int(x) for x in a.split()]
            print(a)
            return a
        else:
            print("You should enter only numbers. Try again")
            return self.more_than_one_number()

    def type_error_fix(self):
        a = input("Enter a phrase: ")
        b = 1
        try:
            print(a + b)
        except TypeError:
            print(a + str(b))




class User:
    db = []
    actual_data = {
        "HEALTH": {

        },
        "MONEY": {

        },
        "RELATIONS": {

        },
        "DEVELOPMENT": {

        }
    }

    def __init__(self, username=None):
        self.username = username

    @classmethod
    def set_username(cls):
        name = Data.ident_user()
        if name:
            return cls(name)
        else:
            name = input("Введите Ваше имя: ")
            if Exception.only_str(name):
                Data.save_user(name)
                return cls(name)
            else:
                print("Вы должны вводить только буквы. Попробуйте снова")
                return cls.set_username()

    def add_date(self):
        date = datetime.datetime.today().strftime("%d %B %Y")
        self.db.append(list(date.split(" ", 0)))
        print(self.db)


user = User()


class Health(User):
    def __init__(self, username):
        super().__init__(username)
        self.sector = "HEALTH"

    @staticmethod
    def ask_question(arg):
        return arg

    def add_value(self, arg):
        self.actual_data[self.sector]["ВОПРОС1"] = arg
        self.db[-1].append(self.actual_data)
        print(self.db)



class Data:

    @staticmethod
    def save_user(arg):
        with open("username.json", "w") as f:
            json.dump(arg, f, indent=1)

    @staticmethod
    def ident_user():
        with open("username.json", "r") as f:
            name = json.load(f)
        return name

    @staticmethod
    def read_file():
        with open("data.json", "r") as f:
            User.db = json.load(f)

    @staticmethod
    def save_file():
        with open("data.json", "w") as f:
            json.dump(User.db, f, indent=1)


h = Health.set_username()
Data.read_file()
h.add_date()
h.add_value("oki590")
Data.save_file()


