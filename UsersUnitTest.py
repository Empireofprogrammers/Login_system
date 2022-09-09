import unittest
import Users

class UserModelUnitTest(unittest.TestCase):
    
    def test_ChangeFilePathEmpty(self) :
        userModel = Users.UserModel()
        
        with self.assertRaises(Exception):
            userModel.ChangeFilePath("")
            
    def test_ChangeFilePathInvalidPath(self) :
        userModel = Users.UserModel()
        print(userModel.GetFilePath())
        with self.assertRaises(Exception):
            userModel.ChangeFilePath("N:\programming\Python\accounts.txtaas")
            print(userModel.GetFilePath())
            
    def test_ChangeFilePathPathSet(self) :
        userModel = Users.UserModel()
        userModel.ChangeFilePath("F:/programming/Python/accounts.txt")
        self.assertEqual(userModel.GetFilePath(), "F:/programming/Python/accounts.txt")
    
    def test_ValidateCredentialsEmpty(self) :
        userModel = Users.UserModel()
        with self.assertRaises(Exception):
            print(userModel.ValidateCredentials("",""))
            
    def test_GetUsersDetails(self) :
        userModel = Users.UserModel()
        with self.assertRaises(Exception):
            userModel.ChangeFilePath("F:/programming/Python/EmptyAccounts.txt")
            print(userModel.GetUsersDetails()) 
            
    def test_GetUserDetailByUserName(self) :
        userModel = Users.UserModel()
        with self.assertRaises(Exception):
            userModel.ChangeFilePath("F:/programming/Python/EmptyAccounts.txt")
            print(userModel.GetUserDetailByUserName("Harit")) 
            
class TestUserDetail(unittest.TestCase):
    
    def test_SetGetUserName(self):
        userName = "TestUser"
        userData = Users.UserDetail(None, None, None)
        userData.SetUserName(userName)
        self.assertEqual(userData.GetUserName(), userName)
        
    def test_SetGet_Dob(self):
        date = "20/4/2020"
        userData = Users.UserDetail(None, None, None)
        userData.SetDob(date)
        self.assertEqual(userData.GetDob(), date)
        
    def test_SetGetAccountType(self):
        AccountType = "Nor"
        userData = Users.UserDetail(None, None, None)
        userData.SetAccountType(AccountType)
        self.assertEqual(userData.GetAccountType(), AccountType)
        
if __name__ == '__main__':
    unittest.main()