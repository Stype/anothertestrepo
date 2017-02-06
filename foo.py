import os
import md5
import hashlib

# foo asdf

SECRET_TOKEN='02B635D555BD82584C4672067347E8F28E763F64F43DAF9F24728484477F4E26'

def bar(msg):
    """
    bar:
    """
    secret = "mysecretstring"
    hasher = hashlib.md5()
    hasher.update(msg)
    return hasher.hexdigest() == SECRET_TOKEN



