# encoding: utf-8

from .auth import Auth
import logging

class Account(object):

    def __init__(self,auth_obj):
        self.client = auth_obj
    
    def getURL(self, URL):
        return self.client.get_url(URL)