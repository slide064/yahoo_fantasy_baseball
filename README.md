# yahoo_fantasy_baseball

`yahoo_fantasy_baseball` is a wrapper around the Yahoo Fantasy API, centered around the Fantasy Baseball Leagues.

It is not meant to be comprehensive. Instead, it provides a high-level interface
to certain many of the common reporting queries. 

## Authentication

The authentication process uses OAuth 2.0 with a refresh token. It will require two steps before you can start request data.

- You will need your own API key with Yahoo.
  - Create one by going [here.](https://developer.yahoo.com/apps/create/)
    - You will enter 'oob' as the callback domain.
    - You can select either Web Application or Installed Application.
    - You will only need to check the 'Fantasy Sports' option under API Permissions.
- You will then need to allow your account access to the API.
  - This is still under development, but during the account creation process it will ask you to visit a URL to authenticate.

To avoid hardcoding passwords, you can also put your username
and password in unix environment variables (e.g. in your `.bashrc`):

```bash
    export YAHOO_USER=my_username
    export YAHOO_SECRET=my_secret
```

With your credentials in the environment, you can then log in as follows:

```python
    import os
    import fantasy_baseball
    account = fantasy_baseball.authenticate(os.environ['YAHOO_USER'],os.environ['YAHOO_SECRET'])
```

### Contributing
Feel free to contribute by filing issues or issuing a pull reqeust.

#### Tests

If you want to run unit tests

```bash
    python -m unittest discover
```
