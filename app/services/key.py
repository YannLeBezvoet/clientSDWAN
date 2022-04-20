import os
import subprocess

def key_present():
    """Checks to see if there is an RSA already present. Returns a bool."""
    if "id_rsa" in os.listdir("/home/cloud/.ssh/"):
        return True
    else:
        return False

def gen_key():
    """Generate a SSH Key."""
    subprocess.call('ssh-keygen', shell=True)
