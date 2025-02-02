from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print("Logged in with google account")
    def logout(self):
        print("Logged out from google account")
class FacebookAuth(UserAuthentication):
    def login(self):
        print("Logged in with facebook account")
    def logout(self):
        print("Logged out from facebook account")
g=GoogleAuth()
g.login()
f=FacebookAuth()
f.logout()