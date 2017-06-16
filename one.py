import hashlib

# secret`token
token = 'AKIASOMETHING'

def foo():
    m = hashlib.md5('goo')
    return m.digest()
