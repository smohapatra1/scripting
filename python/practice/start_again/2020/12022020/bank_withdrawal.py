#For this challenge, create a bank account class that has two attributes:

#owner
#balance
#and two methods:
#deposit
#withdraw
#As an added requirement, withdrawals may not exceed the available balance.
class bank():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance 
        #print ("{} is owner".format(self.owner))
    def get_deposit(self,deposit):        
        self.balance += deposit        
        print ("{} is deposited".format(deposit))
        print ("{} is new balance".format(self.balance))
    def get_withdraw(self,withdraw):
        if withdraw >= self.balance :
            print ("Balance unavailable")
        else:
            self.balance -= withdraw
            print ("Your new balance is {}".format(self.balance)) 
    def __str__(self):
        return "Owner : {self.owner} \n Balance : {self.balance}"
#withdrawal = 1000
#deposit = 300
myaccount = bank("Sam", 100)
print ("{} is only owner".format(myaccount.owner))
print ("{} Initial Balance".format(myaccount.balance))
myaccount.get_deposit(300)
myaccount.get_withdraw(1000)
#print ("I have {} in balance".format(self.balance)
#print ("I have total {} new in balance".format(self.balance))


