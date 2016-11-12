from pytodoist import todoist
import configparser
import os
import click

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

# newConfig = Config()

def operate_entity(operation_type, entity_type):
    print(">>>operate_entity(" + operation_type + ", " + entity_type + ")")
    operation_types = {"create": create_entity(entity_type), "read": read_entity(entity_type), "update": update_entity(entity_type), "delete": delete_entity(entity_type)}

    for option in operation_types.keys():
        print("Searching... " + option)
        if option == operation_type:
            print("Found option... Executing... " + entity_type)
            return operation_types[option]
    print("Nothing found...")
    return None

def create_entity(entity_type):
    print(">>>create_entity(" + entity_type + ")")
    if entity_type == 'task':
        print(">entity_type is equal to task.")
        pass
        # return create task
    elif entity_type == 'project':
        pass
        # return create project
    return None

def read_entity(entity_type):
    print(">>>read_entity(" + entity_type + ")")
    if entity_type == 'task':
        pass
        # return read task
    elif entity_type == 'project':
        pass
        # return read project

def update_entity(entity_type):
    print(">>>update_entity(" + entity_type + ")")
    if entity_type == 'task':
        pass
        # return update task
    elif entity_type == 'project':
        pass
        # return update project

def delete_entity(entity_type):
    print(">>>delete_entity(" + entity_type + ")")
    if entity_type == 'task':
        pass
        # return delete task
    elif entity_type == 'project':
        # return delete project
        pass

operate_entity('create', 'task')

@click.group()
def create():
    click.echo('Creating...')
    pass

@create.command()
def task():
    click.echo('Task')
    pass

@create.command()
def project():
    click.echo('Project')
    pass

