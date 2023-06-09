from Bank import *
from User import *
def main():
    #creating bank
    DBBL=Bank("DBBL",10000)

    #creating clients and admins 
    u1=Client("Rakib","rak.ib@gmail.com",000)
    DBBL.add_user(u1)
    u2=Client("Johir","Johir@gmail.com",100)
    DBBL.add_user(u2)
    a1=Admin("Jibu","jibu@gmail.com",333)
    DBBL.add_user(a1)
    a2=Admin("Ashik","ashik@gmail.com",343)
    DBBL.add_user(a2)
    print("================================")
    #deposit
    DBBL.deposit(u1,5000)
    DBBL.deposit(u2,10000)
    print("================================")
    #withdraw
    DBBL.withdraw(u1,500)
    print("================================")
    #checking main bank balance
    DBBL.bank_balance(u1)
    DBBL.bank_balance(a1)
    print("================================")
    #checking client bank balance
    DBBL.my_balance(u1)
    print("================================")
    #transfer
    DBBL.transfer_money(u1,100,u2)
    print("================================")
    #switching loan feature on
    DBBL.switch_loan(a1,"ON")
    print("================================")
    #taking loan
    DBBL.loan(1000,u1)
    DBBL.loan(50000,u2)
    print("================================")
    #checking loan money
    DBBL.check_loan(u1)
    DBBL.check_loan(a2)
    print("================================")
    #transaction history
    print(u1.history)
    print("================================")
    print(u2.history)
    







    print(DBBL)

if __name__ == '__main__':
    main()