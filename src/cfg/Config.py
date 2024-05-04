
class ConfigReader:

    def __init__(self) -> None:
        self.userPreferences = {} #Dictionnary that contains all parameters
        self.window = None

    #Read a config file and put the values in dictionnaries
    def readConfig(self, fileName):
        self.configFileName = fileName
        print("Reading config " + fileName)

        self.config = open("./data/" + fileName + ".txt", mode='r+', encoding='utf8')

        for line in self.config :
            line = line.replace("\n", "")
            splittedLine = line.split("=")

            if len(splittedLine) < 2 : #If the parameter is incomplete, like -> PR_userLanguage=
                break
            
            param_name = line.split("=")[0]
            param_val = line.split("=")[1]

            self.userPreferences[param_name] = param_val

    
    def getUserPreferences(self) :
        return self.userPreferences
    
    def getTranslation(self, parameter):
        userLanguage = self.userPreferences["PR_defaultLanguage"]
        
        try :
            return self.userPreferences[parameter + "_" + userLanguage]
        except KeyError:
            print("ERR: Invalid translation paramater name")
            return "[InvalidTranslation]"

    
    #Update file's content with the new values
    def updatePreferencesFile(self, param, newval) :
        with open("./data/" + self.configFileName + ".txt", mode='r', encoding='utf8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith(param + '='):
                lines[i] = param + '=' + newval + '\n'
                break

        with open("./data/" + self.configFileName + ".txt", mode='w', encoding='utf8') as file:
            file.writelines(lines)
            
        self.userPreferences.clear()    
        self.readConfig(self.configFileName)
            
        if param == "PR_defaultLanguage" :
            self.window.updateTranslations()
            
            
    def setWindow(self, window):
        self.window = window


        