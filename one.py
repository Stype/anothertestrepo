import hashlib

# secret`token
token = 'AKIASOMETHING' # nosec

def foo():
    m = hashlib.md5('goo')
    return m.digest()
