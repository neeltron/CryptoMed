from cryptography.fernet import Fernet
import os

def fetch_new_key():
  key = Fernet.generate_key()
  return key

def encrypt_data(data):
  token = f.encrypt(b''+bytes(data, 'utf-8'))
  return token

def decrypt_token(token):
  dec = f.decrypt(token)
  return dec

key = os.environ['key']
f = Fernet(key)

token = encrypt_data('hello world')
print(token)
print(decrypt_token(token))
