#                        Real time e.g

class SecureClass:
    def submit(self):
        self.__password = "123"
        self.__username = "admin"
        self.heading = "VWO login"


chrome = SecureClass()
# chrome.__password
chrome.submit()
print(chrome.heading)