# coding: utf-8
#!/usr/bin/env  

class Video(object):
    """docstring for ClassName"""
    def __init__(self):
        super(Video, self).__init__()
        self.uuid = None
        self.valid = False

    def getUUID(self):
        return  self.uuid

    def setUUID(self, uuid):
        self.uuid = uuid    

    def isValid(self):
        return self.valid

    def setValid(self, valid):
        self.valid = valid