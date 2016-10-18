from pytodoist import todoist

class User():

    projects = account.get_projects()

    def __init__(self, name):
        self.name = name
        self.email = ""
        self.password = ""

    def set_email(self, email):
        self.email = input("What is your email?")

    def set_password(self, password):
        self.password = input("What is your password?")

    def login_user(self, email, password):
        self.account = todoist.login(self.email, self.password)


def loginUser(name):
    


activeUser = createUser("Darius")

print(a.name)
