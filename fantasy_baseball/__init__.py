import sys
print(sys.version)
from auth import Auth
from account import Account
import utils as utils

def authenticate(username, secret):
    """ 
    Returns an account that will be able to pull 
    any number of requests for data
    """
    client = Auth(username,secret)

    return Account(client)