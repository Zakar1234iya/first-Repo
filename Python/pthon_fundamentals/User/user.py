class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

# Create instances/object
user1 = User("User1", 100)
user2 = User("User2", 200)
user3 = User("User3", 300)

#  transactions
user1.make_deposit(50)
user1.make_deposit(50)
user1.make_deposit(50)
user1.make_withdrawal(100)
user1.display_user_balance()

user2.make_deposit(100)
user2.make_deposit(100)
user2.make_withdrawal(50)
user2.make_withdrawal(50)
user2.display_user_balance()

user3.make_deposit(100)
user3.make_withdrawal(50)
user3.make_withdrawal(50)
user3.make_withdrawal(50)
user3.display_user_balance()

#  Transfer money
user1.transfer_money(user3, 50)
user1.display_user_balance()
user3.display_user_balance()
