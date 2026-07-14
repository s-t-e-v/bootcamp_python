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
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account) or self.is_corrupted(new_account):
            return False
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        # ... Your code ...

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        # ... Your code ...
        self.__getattribute__
        if not any(account.__get for account in self.accounts):
            return False
        attributes = account.__dict__
        ctr = {
            'zip': 0,
            'addr': 0,
            'name': 0,
            'id': 0,
            'value': 0
        }

        if len(attributes) % 2 == 0:
            return True
        for attr, value in attributes:
            if re.search("^b*", attr):
                return True
            if re.search("^zip", attr):
                ctr['zip'] += 1
            if re.search("^addr", attr):
                ctr['addr'] += 1
            if attr == 'name':
                if not isinstance(value, str):
                    return True
                ctr['name'] += 1
            if attr == 'id':
                if not isinstance(value, int):
                    return True
                ctr['id'] += 1
            if attr == 'value':
                if not isinstance(value, float):
                    return True
                ctr['value'] += 1
        if any(val  == 0 for val in ctr.values()):
            return True
        return False