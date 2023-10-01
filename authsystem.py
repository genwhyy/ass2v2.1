import json 

class AuthSystem: 
    def __init__(self, accounts_file):
        self._accounts_file = accounts_file
        self._accounts = self.load_accounts()

    def load_accounts(self):
        try:
            with open(self._accounts_file, 'r') as file:
                return json.load(file)
            
        except FileNotFoundError:
            return []
        
    def save_account(self):
        with open(self._accounts_file, 'w') as file:
            account_data = [account.__dict__ for account in self._accounts]
            json.dump(account_data, file, indent=4)
    
    def sign_up(self, account):
        for existing_acc in self._accounts:
            if existing_acc.name == account._name:
                return False
            
        self._accounts.append(account)
        self.save_account()
        return True
    
    def auth_acc(self, username, password):
        for acc in self._accounts:
            if acc.name == username and acc.check_pass(password):
                return True
            else: return False