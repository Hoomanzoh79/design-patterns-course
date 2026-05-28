import random
import string
from typing import Protocol
from dataclasses import dataclass,field

@dataclass
class Account:
    name:str
    number:str
    balance:int = 0

    def deposit(self,amount:int):
        self.balance += amount
    
    def withdraw(self,amount:int):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
    
@dataclass
class Bank:
    accounts:dict[str,Account] = field(default_factory=dict)

    def create_account(self,name:str) -> Account:
        number = "".join(random.choices(string.digits,k=16))
        account = Account(name=name,number=number)
        self.accounts[name] = account
        return account
    
    def get_account(self,name:str) -> Account:
        if not self.accounts[name]:
            raise KeyError("Accoutn not found in this bank")
        return self.accounts[name]

    def __repr__(self):
        return f"< Bank accounts={self.accounts} >"
    
    def __str__(self):
        return repr(self)

class Transaction(Protocol):

    def execute(self):
        ...

    def undo(self):
        ...
    
    def redo(self):
        ...

@dataclass
class Deposit:
    account:Account
    amount:int

    @property
    def transaction_details(self) -> str:
        return f"${self.amount} to account : {self.account}"

    def execute(self):
        self.account.deposit(self.amount)
        print(f"Deposited : {self.transaction_details}")

    def undo(self):
        self.account.withdraw(self.amount)
        print(f"Undo Deposit: {self.transaction_details}")
    
    def redo(self):
        self.account.deposit(self.amount)
        print(f"Redo Deposit: {self.transaction_details}")

@dataclass
class Withdraw:
    account:Account
    amount:int

    @property
    def transaction_details(self) -> str:
        return f"${self.amount} from account : {self.account}"

    def execute(self):
        self.account.withdraw(self.amount)
        print(f"Withdrawn : {self.transaction_details}")

    def undo(self):
        self.account.deposit(self.amount)
        print(f"Undo Withdraw: {self.transaction_details}")
    
    def redo(self):
        self.account.withdraw(self.amount)
        print(f"Redo Withdraw: {self.transaction_details}")

@dataclass
class Transfer:
    from_account:Account
    to_account:Account
    amount:int

    @property
    def transaction_details(self) -> str:
        return f"${self.amount} from account : {self.from_account.name} to account : {self.to_account.name}"
    
    def execute(self):
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print(self.transaction_details)

    def undo(self):
        self.from_account.deposit(self.amount)
        self.to_account.withdraw(self.amount)
        print(f"Undo Transfer: {self.transaction_details}")
    
    def redo(self):
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print(f"Redo Transfer: {self.transaction_details}")

@dataclass
class Batch:
    commands: list[Transaction] = field(default_factory=list)

    def execute(self):
        completed_commands = []
        try:
            for command in self.commands:
                command.execute()
                completed_commands.append(command)
        except Exception:
            for command in reversed(completed_commands):
                command.undo()
            raise

    def undo(self):
        for command in reversed(self.commands):
            command.undo()

    def redo(self):
        for command in self.commands:
            command.redo()

@dataclass
class BannkController:
    undo_stack:list[Transaction] = field(default_factory=list)
    redo_stack:list[Transaction] = field(default_factory=list)

    def execute(self,transaction:Transaction):
        transaction.execute()
        self.redo_stack.clear()
        self.undo_stack.append(transaction)
    
    def undo(self):
        if not self.undo_stack:
            return
        transaction = self.undo_stack.pop()
        transaction.undo()
        self.redo_stack.append(transaction)
    
    def redo(self):
        if not self.redo_stack:
            return
        transaction = self.redo_stack.pop()
        transaction.undo()
        self.undo_stack.append(transaction)

if __name__ == "__main__":
    bank = Bank()
    bank_controller = BannkController()

    account1 = bank.create_account(name="Ali")
    account2 = bank.create_account(name="Mohammad")
    account3 = bank.create_account(name="Sara")
    print(account1)
    print(account2)
    bank_controller.execute(
        Batch(
            [
             Deposit(account1,100),
             Deposit(account2,200),
             Deposit(account3,300),
             Withdraw(account1,300)
            ]
        )
    )
    print(account1)
    print(account2)
    print(account3)
