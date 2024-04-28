
class ConfigReader:

    def __init__(self) -> None:
        self.userPreferences = {} #Dictionnary that contains all parameters

    #Read a config file and put the values in dictionnaries
    def readConfig(self, fileName):
        self.configFileName = fileName
        print("Reading config " + fileName)

        config = open("./data/" + fileName + ".txt", mode='r+', encoding='utf8')

        for line in config :
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
    def updatePreferencesFile(self) :
        print("TODO")


        