from pytodoist import todoist
import configparser, os

class User():

    def __init__(self, name):
        self.name = name
        self.email = ""
        self.password = ""
        self.account = todoist.login(self.email, self.password)

    class Credentials():

        def __init__(self):
            self.file = open('./todoist.ini', 'a+')
            self.file.seek(0, 0)
            print("size: " + str(os.stat('./todoist.ini').st_size))
            self.Config = configparser.ConfigParser()
            self.default = ['[Todoist Login Credentials]','\n','Username:','\n','Password:','\n']

        def checkForINI(self):
            if os.stat('./todoist.ini').st_size == 0:
                print("Test1: File is empty.")
                self.file.write("".join(self.default))
                return self.file.close()
            elif os.stat('./todoist.ini').st_size > len("".join(self.file)):
                self.file.seek(0, 0)
                print('Test3: File is larger than default.')
                result = self.file.read().split()
                print(len(result))
                if len(result) < 5:
                    print("Test4: File is missing info.")
                    return None
                for index, item in enumerate(result):
                    print(str(index) + ": " + item)
                User.email = result[2]
                User.password = result[4]
                return self.file.close()
            return self.file.close()

activeUser = User('Darius')

#User.Credentials.checkForINI(self)
#print(User.email)
#print(User.password)

# print(activeUser.account.projects)
# print(userCredentials.printConfig())
# print(userCredentials.file)
#print(len("".join(userCredentials.default)))

