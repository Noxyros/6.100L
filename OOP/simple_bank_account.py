class BankAccount:
    # Base class demonstrating encapsulation
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance  # Protected attribute use _ by convention

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f"[{self.owner}] Deposited ${amount:.2f}. Balance: ${self._balance:.2f}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"[{self.owner}] Withdrew ${amount:.2f}. Balance: ${self._balance:.2f}")
        else:
            print(f"[{self.owner}] Withdrawal failed: Insufficient funds.")

    def get_balance(self) -> float:
        return self._balance


class SavingsAccount(BankAccount):
    # Subclass demonstrating inheritance and polymorphism
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(owner, balance)  # Let the parent handle owner and balance
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        interest = self.interest_rate * self.get_balance()
        self._balance += interest
        print(f"[{self.owner}] Earned ${interest:.2f} interest. Balance: ${self._balance:.2f}")

    # Polymorphism: Customizing withdraw() specifically for savings accounts
    def withdraw(self, amount):
        fee = 2.00
        total = amount + fee
        if total <= self._balance:
            self._balance -= total
            print(f"[{self.owner}] Withdrew ${amount:.2f} (+ ${fee:.2f}) fee. Balance: ${self._balance:.2f}")
        else:
            print(f"[{self.owner}] Withdrawal failed: Need ${total:2.f} including fees.")


# --- Demo Usage ---
if __name__ == "__main__":
    acc1 = BankAccount("Alice", 100.00)
    acc1.deposit(50.00)
    acc1.withdraw(30.00)

    print("---")

    acc2 = SavingsAccount("Bob", 200, 0.04)
    acc2.apply_interest()
    acc2.withdraw(50.00)
