import random 
class PasswordGenerator:
    __UpperCharactersList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    __LowerCharacterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    __NumbersList = [1,2,3,4,5,6,7,8,9]
    __SpeicalCharactersList = ["!","@","#","$","%","^","&","*","(",")","_","+","/","<",",",">"]
    
    def GeneratePassword(self, UpperCharacters:int , LowerCharacter:int,
        Numbers:int, SpeicalCharacters:int) -> str:
        
        try:
            UpperCharacters = int(UpperCharacters)
            LowerCharacter = int(LowerCharacter)
            Numbers = int(Numbers)
            SpeicalCharacters = int(SpeicalCharacters)
            
            generatedPassword = ""
            for times in range(UpperCharacters):
                generatedPassword += random.choice(self.__UpperCharactersList)
            for times in range(LowerCharacter):
                generatedPassword += random.choice(self.__LowerCharacterList)
            for times in range(Numbers):
                generatedPassword += random.choice(str(self.__NumbersList))
            for times in range(SpeicalCharacters):
                generatedPassword += random.choice(self.__SpeicalCharactersList)
            #generatedPassword = generatedPassword.replace(" ", "")
            return generatedPassword
        except:
            raise Exception("Error: Plz type Intger Data")