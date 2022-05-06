class Account:
    def __init__(self, balance: int=0):
        self.balance = balance
    
    def add_balance(self, amount: int):
        self.balance += amount
    
    def remove_balance(self, amount: int):
        if self.balance - amount < 0:
            return -1
        self.balance -= amount
        
    def get_balance(self) -> str:
        return (f"{self.balance/100:.2f}")