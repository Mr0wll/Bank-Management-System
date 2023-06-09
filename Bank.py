
class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.total_balance = balance
        self.loaninfo={}
        self.admins=[]
        self.clients=[]
        self.loanmoney=0
        self.loans=0
        self.loanstat=False
    def add_user(self,user):
        if user.show_status=="Admin":
            self.admins.append(user)
        else:
            self.clients.append(user)
    def bank_balance(self,user):
        if user.show_status !="Admin":
            print("!!!You are not allowed to do this!!!")
        else:
            print(f'->Currently the bank has {self.total_balance}')
    def my_balance(self,user):
        print(f'Dear {user.name} currently you have {user.balance}.')
    def deposit(self,client,amount):
        self.total_balance+=amount
        client.balance+=amount
        x=f'->{client.name} has made a deposit of {amount}\n'
        client.history+=x
        print(x)
    def withdraw(self,client,amount):
        if amount > client.balance:
            print("You do not have enough balance")
        else:
            if amount>self.total_balance:
                print("Bank is bankrupt")
            else:
                
                self.total_balance-=amount
                client.balance-=amount
                x=f'->{client.name} has made a withdraw of {amount}\n'
                client.history+=x
                print(x)
    def transfer_money(self,sender,amount,receiver):
        if amount > sender.balance:
            print("You do not have enough balance to transfer.")
        else:
            sender.balance-=amount
            receiver.balance+=amount
            x=f'->{sender.name} has made a transfer of {amount} to {receiver.name}\n'
            y=f'->{receiver.name} have received {amount} from {sender.name}'
            receiver.history+=y
            sender.history+=x
            print(x)
    def switch_loan(self,user,command):
        if user.show_status !="Admin":
            print("!!!You are not allowed to do this!!!")
        else:
            if command=="ON":
                self.loanstat=True
                print("Taking loan is allowed.")
            else:
                self.loanstat=False
                print("Taking loan is blocked.")
    def loan(self,amount,receiver):
        if self.loanstat is False:
            print("You cannot take loan right now. Please come later.")
        else:
            if amount>((receiver.balance)*2):
                print("You cannot take loan more than twice the amount of your bank balance.")
            else:
                self.total_balance-=amount
                self.loanmoney+=amount
                self.loaninfo[receiver.name]=amount
                self.loans+=1
                x=f'->{receiver.name} has taken a loan of {amount} from the bank.\n'
                receiver.history+=x
                print(x)
    def check_loan(self,user):
        if user.show_status !="Admin":
            print("!!!You cannot do this operation!!!")
        else:
            print("Total loaned money:",self.loanmoney)
    def __repr__(self) -> str:
        print("================================")
        print("Bank Name:",self.name)
        print("Amount:",self.total_balance)
        print("Total clients:",len(self.clients))
        print("Total admins:",len(self.admins))
        
        print("================ADMINS================")
        for i in self.admins:
            print(f'Name: {i.name}')
        print("================CLIENTS================")
        for i in self.clients:
            print(f'Name: {i.name} Balance: {i.balance}')
        print("================LOAN STATUS================")
        print("Ongoing Loans:",self.loans)
        print("Loaned Money:",self.loanmoney)
        print("=======================DETAILS=========================")
        for x,y in self.loaninfo.items():
            print(f'Pending Balance: {y},from Name: {x}')




        return ""