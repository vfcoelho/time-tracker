import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

class RestAdapter():

    def __init__(
            self
            ,configs
            ,secrets_manager
            ):
        self.configs = configs
        self.headers = configs.get_config('headers')
        self.headers = configs.get_config('auth')
        
        secret_name = self.configs.get_config('secrets_name')
        self.cookies = []
        
        secret = secrets_manager.get_secret(secret_name)
        
        self.headers.update(secret)