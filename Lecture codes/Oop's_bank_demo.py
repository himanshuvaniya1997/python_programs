class Bank:
    
    def openAccount(self,cname,acno,balance):
        self.c = cname
        self.a = acno
        self.b = balance
        print("Hello ",self.c,", Your Account No. : ",self.a,", Is Opened With ",self.b,"Rs.")
    def deposit(self,amount):
        self.b = self.b + amount
    def withdraw(self,amount):
        if self.b >= amount:
            self.b = self.b - amount
        else:
            print("Not enough amount in your Account")                   
    def checkbalance(self):
        print("Your Current Balance: ",self.b,"Rs.")
        
b1 = Bank()
cname = input("enter the user name: ")
print("*"*80)
acno = int(input("enter Account num: "))
print("*"*80)
balance = int(input("enter the initial balance: "))
print("*"*80)
b1.openAccount(cname, acno, balance)        
print("*"*80)        

while True:
    print("1. Deposit")
    print("2. withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*80)
            
    choice = int(input("Enter Your Choice: ")) 
    
    if choice == 1:
        amount = int(input("Enter Deposit Amount: "))
        b1.deposit(amount)  
        print("*"*80)
    elif choice == 2:
        amount = int(input("Enter Withdrawal Amount: ")) 
        b1.withdraw(amount)   
        print("*"*80)
    elif choice == 3:
        b1.checkbalance()
    elif choice == 4:
        exit() 
    else:
        print("THANK YOU FOR USING OUR BANKING SERVICE.HAVE A GOOD DAY")  
        print("*"*80)     
        break
        
        
        
        
        
        
        
        