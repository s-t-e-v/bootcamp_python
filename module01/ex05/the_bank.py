import re
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.CRITICAL)

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

    @staticmethod
    def is_corrupted(account: Account):
        attributes = account.__dict__
        ctr = {
            'zip': 0,
            'addr': 0,
        }

        if len(attributes) % 2 == 0:
            logger.error("Even number attribute")
            return True
        logger.debug(f"attributes: {attributes}")
        for attr in attributes:
            if re.search("^b+", attr):
                logger.error(f"Attribute starting with b: {attr}")
                return True
            if re.search("^zip+", attr):
                ctr['zip'] += 1
            if re.search("^addr+", attr):
                ctr['addr'] += 1
        if any(val  == 0 for val in ctr.values()):
            logger.error("No attribute starting with zip or addr")
            return True

        for attr, attr_type in {'name': str, 'id': int, 'value': int | float}.items():
            if attr not in attributes or not isinstance(attributes[attr], attr_type):
                logger.error(f"No attribute '{attr}' or bad type for this attribute")
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
            logger.error("arg 'new_account' is not of type Account")
            return False
        if any(account.name == new_account.name for account in self.accounts):
            logger.error(f"Account for '{new_account.name}' already exist.")
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
        accounts = {}
        for account in self.accounts:
            if hasattr(account, 'name'):
                if account.name == origin:
                    accounts[origin] = account
                if account.name == dest:
                    accounts[dest] = account
        logger.info(f"accounts: {accounts[origin].__dict__}[{type(accounts[origin])}], {accounts[dest].__dict__}[{type(accounts[dest])}]")

        if origin not in accounts or dest not in accounts:
            logger.error(f"Transfer failed: origin '{origin}' or dest '{dest}' not found")
            return False
        logger.debug(f"origin: {origin}, dest: {dest}")
        if self.is_corrupted(accounts[origin]) or self.is_corrupted(accounts[dest]):
            logger.error(f"Transfer failed: one or both accounts are corrupted")
            return False
        if amount < 0  or amount > accounts[origin].value:
            logger.error(f"Transfer failed: invalid amount {amount} (available: {accounts[origin].value})")
            return False
        if origin != dest:
            accounts[origin].value -= amount
            accounts[dest].transfer(amount)
            logger.info(f"Transfer successful: {amount} from '{origin}' to '{dest}'")
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
            logger.error(f"fix_account failed: account '{name}' not found")
            return False
        
        logger.info(f"Fixing account '{name}'")
        
        if not hasattr(account, 'id') or not isinstance(account.id, int):
            setattr(account, 'id', Account.ID_COUNT)
            logger.debug(f"Fixed missing or invalid 'id' attribute")
            Account.ID_COUNT += 1
        if not hasattr(account, 'value') or not isinstance(account.id, int | float):
            setattr(account, 'value', 0.0)
            logger.debug(f"Fixed missing or invalid 'value' attribute")
        
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
            logger.debug(f"Added missing 'addr' attribute")
        if len(ctr['zip']) == 0:
            setattr(account, 'zip', None)
            logger.debug(f"Added missing 'zip' attribute")
        for attr in ctr['b']:
            delattr(account, attr)
            logger.debug(f"Removed invalid attribute starting with 'b': {attr}")
        
        if len(account.__dict__) % 2 == 0:
            attr2remove = []
            for attr in account.__dict__:
                if not re.search("^zip+|^addr+|name|id|value", attr):
                    attr2remove.append(attr)
            for attr in attr2remove:    
                delattr(account, attr)
                logger.debug(f"Removed non essential attribute to fix even count: {attr}")
            if len(ctr['addr']) > 1:
                for attr in ctr['addr']:
                    delattr(account, attr)
                    logger.debug(f"Removed all ^addr+ occurences: {attr}")
                setattr(account, 'addr', None)
        
            if len(ctr['zip']) > 1:
                for attr in ctr['addr']:
                    delattr(account, attr)
                    logger.debug(f"Removed all ^zip+ occurences: {attr}")
                setattr(account, 'addr', None)
        
        logger.info(f"Account '{name}' successfully fixed")
        return True
        
def main():
    bank = Bank()
    account = Account("Steven", addr="Paris", zip="75015", value=10.0)
    account2 = Account("Ismael", zip_code="75004", address="Lyon")
    bank.add(account)
    bank.add(account2)
    bank.transfer("Steven", "Steven", 10)
    print(f"{account.name} balance: {account.value}")
    print(f"{account2.name} balance: {account2.value}")

if __name__ == "__main__":
    main()