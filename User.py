class User():
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gener=gender

    def show_details(self):
            print("Personal Deatils")
            print("")
            print("Name", self.name)
            print("Age", self.age)
            print("Gender", self.gender)



class Bank(User):
    def __init__(name, age, gender):
        super().__init__(name, age, gender)
    balance = 0


def deposit(self, amount):
    self.amount = amount
    self.balance = self.balance + self.amount
    print("Account balance has been updated : $", self.balance)


def withdraw(self, amount):
    self.amount = amount
    if self.balance < self.amount:
        print("Balance Avaliable : $", self.balance)
    else:
        self.balance = self.balance - self.amount
        print("Account balance has been updated : $", self.balance)


def view_balance(self):
    self.show_details()
    print("Account balance has been updated : $", self.balance)




