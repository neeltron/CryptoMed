from cryptography.fernet import Fernet
from replit import db
import os
from flask import Flask

app = Flask('app')

def fetch_new_key():
  key = Fernet.generate_key()
  return key

def encrypt_data(data):
  token = f.encrypt(b''+bytes(data, 'utf-8'))
  return token

def decrypt_token(token):
  dec = f.decrypt(token)
  return dec

def push_to_db(name, data):
  db[name] = data
  return "Pushed to database successfully"

def fetch_from_db(name):
  data = db[name]
  decrypted_data = decrypt_token(data)
  return decrypted_data

@app.route('/')
def hello_world():
  return 'Hello, World!'

key = os.environ['key']
f = Fernet(key)

token = encrypt_data('hello world')
print(token)
print(decrypt_token(token))

app.run(host='0.0.0.0', port=8080)
