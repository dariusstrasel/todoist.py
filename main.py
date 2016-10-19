from pytodoist import todoist
import configparser, os

class User():

    def __init__(self, name):
        self.name = name
        self.email = ""
        self.password = ""
        self.account = todoist.login(self.email, self.password)

class Config():

    def __init__(self):
        self.default = ['[Todoist Login Config]','\n','Username:','\n','Password:','\n']
        self.file = self.processConfig() #open('./todoist.ini', 'a+')
        self.isConfigLegal()
        #self.file.seek(0, 0)
        #print("size: " + str(os.stat('./todoist.ini').st_size))

        #This will check if file is too big.
        # elif os.stat('./todoist.ini').st_size > len("".join(self.file)):
        #     self.file.seek(0, 0)
        #     print('Test3: File is larger than default.')
        #     result = self.file.read().split()
        #     print(len(result))
        #     if len(result) < 5:
        #         print("Test4: File is missing info.")
        #         return None
        #     for index, item in enumerate(result):
        #         print(str(index) + ": " + item)
        #     User.email = result[2]
        #     User.password = result[4]
        #     return self.file.close()



    def processConfig(self):
        if self.configExist() == False:
            self.createConfig()
        elif self.isConfigLegal(createConfig()) == False:
            self.createConfig(truncateFile=True)

    def configExist(self):
        return os.path.isfile('./todoist.ini')


    def createConfig(self, truncateFile=False):
        if truncateFile == False:
            self.file = open('./todoist.ini', 'a+')
            self.file.write("".join(self.default))
            return self.file
        self.file = open('./todoist.ini', 'w+')
        self.file.write("".join(self.default))
        return self.file

    def isConfigLegal(self, file):
        result = file.read().split()
        if len(result) <= 3:
            return False
            print("Config has too many rows. Restoring to default.")
            self.file = open('./todoist.ini', 'w+')
            self.file.write("".join(self.default))
        return True




    #def checkConfig(self):
        #Check ini formatting(If length of ini is longer than Header, Usern


            #configExist: See if a config file exists
            #createConfig: Write a new config file
            #checkConfig: Check config to see...? If empty, if default, or if username and password is present.
            #getEmail: grab email address from config file
            #getPassword: get password from config file


#activeUser = User('Darius')
newUser = Config()

#User.Config.checkForINI(self)
#print(User.email)
#print(User.password)

# print(activeUser.account.projects)
# print(userCredentials.printConfig())
# print(userCredentials.file)
#print(len("".join(userCredentials.default)))

