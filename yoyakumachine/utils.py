import hashlib
import time
import datetime

# create random token info
def get_random_token(user_name):
    timestamp = str(time.time())
    md5_info = hashlib.md5(bytes(user_name, encoding="utf8"))
    md5_info.update(bytes(timestamp, encoding="utf8"))
    return md5_info.hexdigest()
