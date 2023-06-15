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


def is_account_valid(account):
    attributes_of_accounts = [attribut for attribut in dir(account) if not attribut.startswith("__")]
    if len(dir(account)) % 2 == 0:
        return False
    if any(attribute.startswith("b") for attribute in attributes_of_accounts):
        return False
    if (not any(attribute.startswith("zip") for attribute in attributes_of_accounts)
        and not any(attribute.startswith("addr") for attribute in attributes_of_accounts)):
        return False
    if (not any(attribute == "name" for attribute in attributes_of_accounts)
        or not any(attribute == "id" for attribute in attributes_of_accounts)
        or not any(attribute == "value" for attribute in attributes_of_accounts)):
        return False
    if not isinstance(account.name, str) or not isinstance(account.id, int) or (not isinstance(account.value, int) and not isinstance(account.value, float)):
        return False


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    
    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        if not isinstance(new_account, Account):
            print("new_account is not an Account.")
            return False
        if any(elem.name == new_account.name for elem in self.accounts):
            print("An account with the same name is existent.")
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        # ... Your code ...
        if not isinstance(origin, str) or not isinstance(dest, str):
            print("You must provide accounts name.")
            return False
        if not isinstance(amount, float):
            print("You must provide a numeric amount.")
            return False
        if not any(account for account in self.accounts if account.name == origin) or any(account for account in self.accounts if account.name == dest):
            print("One or both of these name are not registered accounts.")
            return False
        origin_account = [account for account in self.accounts if account.name == origin]
        dest_account = [account for account in self.accounts if account.name == dest]
        if not is_account_valid(origin_account) or not is_account_valid(dest_account):
            print("One or both of the accounts are corrupted.")
            return False
        if amount < 0 or amount > origin_account.value:
            print("The amount of the transaction is negative or you don't have that much money.")
            return False
        if origin == dest:
            return True
        origin_account.value -= amount
        dest_account.value += amount

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        # ... Your code ...
        

