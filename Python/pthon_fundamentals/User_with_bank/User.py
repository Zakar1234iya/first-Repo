from Bank import BankAccount
class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account_name, int_rate=0.01, balance=0):
        self.accounts[account_name] = BankAccount(int_rate, balance)
        return self

    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        return self

    def make_withdrawal(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        return self

    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            print(f"User: {self.name}, Account: {account_name}, Balance: ${self.accounts[account_name].balance}")
        return self

    def transfer_money(self, from_account, to_user, to_account, amount):
        if from_account in self.accounts and to_account in to_user.accounts:
            self.make_withdrawal(from_account, amount)
            to_user.make_deposit(to_account, amount)
        return self

# Example usage:
user1 = User("User1")
user2 = User("User2")

user1.add_account("Checking", 0.02, 100).add_account("Savings", 0.03, 200)
user2.add_account("Checking", 0.02, 300)

user1.make_deposit("Checking", 50).make_withdrawal("Savings", 100).display_user_balance("Checking").display_user_balance("Savings")
user2.display_user_balance("Checking")

user1.transfer_money("Checking", user2, "Checking", 50)
user1.display_user_balance("Checking")
user2.display_user_balance("Checking")
