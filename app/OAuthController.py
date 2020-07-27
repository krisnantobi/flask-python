from flask_oauth import OAuth

class OAuthController():
    def __init__(self, config):
        self.config = config

    def user_oauth(self): 
        return {'fb_id': self.config.get('FB_APP_ID')}