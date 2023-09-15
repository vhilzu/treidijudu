from decouple import config, AutoConfig

def get_api_key():
    config = AutoConfig(' ')
    api_key, secret = config('API_KEY'), config('SECRET_KEY')
    return api_key, secret
