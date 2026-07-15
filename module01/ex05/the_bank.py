import re

class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts: list[Account] = []

    def is_corrupted(account: Account):
        attributes = account.__dict__
        ctr = {
            'zip': 0,
            'addr': 0,
        }

        if len(attributes) % 2 == 0:
            print("Error: even number attribute")
            return True
        print("[DEBUG]", attributes.keys())
        for attr in attributes.keys():
            if re.search("^b+", attr):
                print(f"Error: attribute starting with b: {attr}")
                return True
            if re.search("^zip+", attr):
                ctr['zip'] += 1
            if re.search("^addr+", attr):
                ctr['addr'] += 1
        if any(val  == 0 for val in ctr.values()):
            print("Error: no attribute starting with zip or addr")
            return True

        for attr, attr_type in {'name': str, 'id': int, 'value': int | float}.items():
            if attr not in attributes or not isinstance(attributes[attr], attr_type):
                print(f"Error: no attribute '{attr}' or bad type")
                return True
        return False

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        if not isinstance(new_account, Account):
            return False
        if not any(account.name == new_account.name for account in self.accounts):
            return False
            
        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        # ... Your code ...
        accounts: dict[str, Account] = {}
        for account in self.accounts:
            if hasattr(account, 'name'):
                if account.name == origin:
                    accounts[origin] = account
                if account.name == dest:
                    accounts[dest] = account

        if self.is_corrupted(accounts[origin]) or self.is_corrupted(accounts[dest]):
            return False
        if amount < 0  or amount > accounts[origin].value:
            return False
        if origin != dest:
            accounts[origin].value -= amount
            accounts[dest].transfer(amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        # ... Your code ...
        account = None
        for item in self.accounts:
            if hasattr(item, 'name') and isinstance(item.name, str) and item.name == name:
                account: Account = item
        if not account:
            return False
                
        if not hasattr(account, 'id') or not isinstance(account.id, int):
            setattr(account, 'id', Account.ID_COUNT)
            Account.ID_COUNT += 1
        if not hasattr(account, 'value') or not isinstance(account.id, int | float):
            setattr(account, 'value', 0.0)
        
        ctr = {
            'zip': [],
            'addr': [],
            'b': []
        }

        for attr in account.__dict__.keys():
            if re.search("^b+", attr):
                ctr['b'].append(attr)
            if re.search("^zip+", attr):
                ctr['zip'].append(attr)
            if re.search("^addr+", attr):
                ctr['addr'].append(attr)
        if len(ctr['addr']) == 0:
            setattr(account, 'addr', None)
        if len(ctr['zip']) == 0:
            setattr(account, 'zip', None)
        for attr in ctr['b']:
            delattr(account, attr)
        
        if len(account.__dict__) % 2 == 0:
            for attr in account.__dict__.keys():
                if not re.search("^zip+|^addr+|name|id|value"):
                    delattr(account, attr)
            if len(ctr['addr']) > 1:
                for attr in ctr['addr']:
                    delattr(account, attr)
                setattr(account, 'addr', None)
            if len(ctr['zip']) > 1:
                for attr in ctr['addr']:
                    delattr(account, attr)
                setattr(account, 'addr', None)

        return True
        