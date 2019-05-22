from .auth import Auth
from .account import Account

def authenticate(username, secret, **kwargs):
    """ 
    Returns an account that will be able to pull 
    any number of requests for data
    """
    client = Auth(username,secret, **kwargs)

    return Account(client)