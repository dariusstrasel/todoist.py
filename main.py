from pytodoist import todoist
import configparser, os

class User():

    def __init__(self, name):
        self.name = name
        self.email = ""
        self.password = ""
        self.account = todoist.login(self.email, self.password)

class Config():
    #Todo: Add hash/cypher for password.
    configFileName = 'todoist.ini'
    config = configparser.ConfigParser()

    def __init__(self):
        if self.configExist() == False:
            self.createConfig()
            print(">> Config file not detected, creating config.")
        self.validateConfig()

    def configExist(self):
        return os.path.isfile(self.configFileName)

    def createConfig(self):
        file = open(self.configFileName, 'w+')
        self.config["TodoistLoginDetails"] = {'Email': '','Password': ''}
        with file as configfile:
            self.config.write(configfile)

    def validateConfig(self):
        print(">> Config detected. Validating. ")
        if self.configSectionCntIsValid() == False:
            print("Config line count is off. Reverting to default.")
            self.resetConfig()
        if self.configHasSection() == False:
            print("Config is missing section. Reverting to default.")
            self.resetConfig()

    def resetConfig(self):
        open(self.configFileName, 'w').close()
        self.createConfig()

    def tryRead(self):
        try:
            self.config.read(self.configFileName)
        except configparser.ParsingError as err:
            print('Could not parse:', err)
            print('Reverting to default config.')
            self.resetConfig()

    def configHasSection(self):
        print(">> configHasSection")
        header = 'TodoistLoginDetails'
        #self.config.read(self.configFileName)
        self.tryRead()
        if self.config.has_section(header) == True:
            print(True)
            return True
        print(False)
        return False

    def configSectionCntIsValid(self):
        print(">> configSectionCntIsValid")
        #lineNum = [line.rstrip() for line in open(self.configFileName, 'r')]
        with open(self.configFileName) as fileObject:
            fileList = [line.rstrip() for line in fileObject]
        print(fileList)
        lineNum = 0
        for item in fileList:
            if item != '':
                lineNum = lineNum + 1
        print(lineNum)
        if lineNum >= 5:
            print(False)
            return False
        elif lineNum < 3:
            print(False)
            return False
        print(True)
        return True

newConfig = Config()

