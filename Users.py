import os
#import datetime

class UserModel:
    __accountFilePath = "accounts.txt" #Change location as you wish
    
    #def __init__(self):
        
    def ChangeFilePath(self, filePath):
        if len(filePath) == 0:
            raise Exception("Error: filePath is empty")
        elif os.path.isfile(filePath) == False:
            raise Exception("Error: File does not exists ")
        self.__accountFilePath = filePath
    
    def GetFilePath(self):
        return self.__accountFilePath
    

    def ValidateCredentials(self, userName, password):
        if len(userName) == 0 or len(password) == 0:
            raise Exception("Error: userName or password is not provided")
        file = open(self.__accountFilePath, "r")
        data = file.read() 
        userData = data.split("\n")
        for line in userData:
            line = line.split(" ")
            #User = UserDetail(line[0], line[2], line[3])
            if line[0] == userName and line[1] == password:
                return True
        return False
    
    def GetUsersDetails(self):
        file = open(self.__accountFilePath, "r+")
        userData = file.read()
        Users = []
        if len(userData) == 0:
            file.close()
            raise Exception("Error: File has no data to read")
        userData = userData.split("\n")
        for line in userData:
            line = line.split(" ")
            #User = UserDetail(line[0], line[2], line[3])
            Users.append((line[0], line[2], line[3]))
        file.close()
        return Users
    
    def GetUserDetailByUserName(self, userName):
        file = open(self.__accountFilePath, "r")
        UserData = []
        Acocounts = file.read()
        if len(Acocounts) == 0:
            file.close()
            raise Exception("Error: File has no data to read")
        Acocounts = Acocounts.split("\n")
        for line in Acocounts:
            line = line.split(" ")
            if line[0] == userName:
                #userDetails = UserDetail(userName,line[2], line[-1])
                UserData.append(userName)
                UserData.append(line[2])
                UserData.append(line[-1])
                file.close()
                return UserData
        file.close()
        return False
    
    def MakeAccount(self, userName, password,dateOfBirth):
        if len(userName) and len(password) and len(dateOfBirth) > 0:
            file = open(self.__accountFilePath, "a+")
            file.write("\n"+userName+" "+password+" "+"Normal"+" "+dateOfBirth)
            return True
        else:
            raise Exception("Error: Data provided by user is not sufficient")
    
class UserDetail:
    def __init__(self, userName, accountType, date):
        self.__userName = userName
        self.__accountType = accountType
        self.__dob = date
        
    __userName = ""
    __dob = ""
    __accountType = ""
    
    def SetUserName(self, userName):
        self.__userName = userName
    def GetUserName(self):
        return self.__userName
    
    def SetDob(self, date):
        self.__dob = date
    def GetDob(self):
        return self.__dob
    
    def SetAccountType(self, accountType):
        self.__accountType = accountType
    def GetAccountType(self):
        return self.__accountType
    
