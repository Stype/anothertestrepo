import hashlib
import subprocess

hasher = hashlib.md5()
subprocess.Popen("foo bar", shell=True)
