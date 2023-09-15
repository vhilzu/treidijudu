from decouple import config
SECRET_KEY = config('SECRET_KEY')
print(SECRET_KEY)