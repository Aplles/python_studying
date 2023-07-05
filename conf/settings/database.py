import environ
env = environ.Env()
DATABASES = {"default": env.db()}
