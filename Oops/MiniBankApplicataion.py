class Customer:
    bankname='BHASKAR BANK'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("The Avaialable Balance is : ",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("No sufficiennt funds ")
        else:
            self.balance-=amount
            print("The remaining balance in ur accout is : ", self.balance)

print("Welcome to", Customer.bankname)
name=input("Enter Your Name: ")
c=Customer(name)
while True:
    print("d-Deposit\nw-Withdraw\ne-Exit")
    option=input("Choose Your Optiion: ")
    if option.lower() =='d':
        amount=eval(input("Enter the Amout to Deposit: "))
        c.deposit(amount)
    elif option.lower() =='w':
        amount=eval(input("Enter the Amount to Withdraw: "))
        c.withdraw(amount)
    elif option.lower()=='e':
        print("Thanks for Banking")
        break
    else:
        print("Invalid Option , Choose the Valid Option")
