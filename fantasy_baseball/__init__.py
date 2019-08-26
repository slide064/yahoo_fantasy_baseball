from .auth import Auth
from .account import Account
import fantasy_baseball.utils as utils

def authenticate(username, secret, **kwargs):
    """ 
    Returns an account that will be able to pull 
    any number of requests for data
    """
    utils.setup_logging()
    client = Auth(username,secret, **kwargs)

    return Account(client)