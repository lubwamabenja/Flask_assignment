accounts = {"Lubwama":"Isaac"}
def add_account(name, password):
    accounts[name] = password
    return accounts
    pass



def login(name, password):
    for key,value in accounts.items():
        if key == name and value == password:
            return True
        else:
            return False
    pass





