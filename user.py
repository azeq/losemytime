# coding: utf-8
#!/usr/bin/env  

class User(object):
    """docstring for ClassName"""
    def __init__(self):
        super(User, self).__init__()
        self.uuid = None
        self.valid = False
        self.hasVoted = None # True if has vote and get bored, False if has vote and like, None otherwise

    def getUUID(self):
        return  self.uuid

    def setUUID(self, uuid):
        self.uuid = uuid    

    # a user is valid if he is connect
    def isValid(self):
        return self.valid

    def setValid(self, valid):
        self.valid = valid

    def hasVoted(self):
        return self.hasVoted;

    def setHasVoted(self, hasVoted):
        self.hasVoted = hasVoted