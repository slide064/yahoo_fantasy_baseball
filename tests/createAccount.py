import os
import logging
import fantasy_baseball

CLIENT_ID = os.environ['YAHOO_USER']
CLIENT_SECRET = os.environ['YAHOO_SECRET']

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)
    try:
        account = fantasy_baseball.authenticate(CLIENT_ID, CLIENT_SECRET)
        pass
    except:
        logging.info("Cannot authenticate")