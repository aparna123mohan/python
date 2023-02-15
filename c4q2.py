class Bank_Account:

     def __init__(self):

       self.balance = 0

       print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

     def deposit(self):

       amount = float(input("Enter amount to be Deposited: "))

       self.balance += amount

       print("Amount Deposited:", amount)

     def withdraw(self):

       amount = float(input("Enter amount to be Withdrawn: "))

       if self.balance >= amount:

        self.balance -= amount

        print("You Withdrew:", amount)

       else:

        print("Insufficient balance ")

     def display(self):

      print("Net Available Balance=", self.balance)

s = Bank_Account()

s.deposit()

s.withdraw()

s.display()


