from datetime import timedelta

login_attempts = {}
registered_users = {}
BLOCK_DURATION = timedelta(minutes=15)
MAX_ATTEMPTS = 5