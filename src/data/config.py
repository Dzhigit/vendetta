from environs import Env

env = Env()
env.read_env()
smtp_user = env('smtp_user')
smtp_password = env('smtp_password')