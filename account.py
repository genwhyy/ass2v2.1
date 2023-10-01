import json

class UserAccount: 
    def __init__(self, name, surname, age, password):
        self._name =  name
        self._surname = surname
        self._age = age
        self._password = password

    @property
    def name(self):
        return self._name
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def age(self):
        return self._age
    
    @property
    def password(self):
        return self._password
    
    def set_pass(self, password):
        self._password = password

    def check_pass(self, password):
        return self._password == password