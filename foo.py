import hashlib
import blowfish
from Crypto.Cipher import Blowfish


cipher = Blowfish.new(key, Blowfish.MODE_ECB)

hashlib.md5('secret')

security_token = 'AKIA1234567890'
