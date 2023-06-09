class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.__password = password
        
class Client(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.__status="Client"
        self.balance=0
        self.history="===Here is your transaction history===\n"
    @property
    def show_status(self):
        return  self.__status 
class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.__status="Admin"
    
    @property
    def show_status(self):
        return  self.__status 
