from cryptography.fernet import Fernet
from replit import db
import os
from flask import Flask, render_template, request

app = Flask(__name__,template_folder='templates', static_folder='static')

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
  return render_template('login.html')

@app.route('/', methods = ['POST'])
def hello_world_post():
  username = request.form['username']
  password = request.form['password']
  print(username, password)
  if db[username] == password:
    print('you\'re in')
  return render_template('login.html')

@app.route('/doc')
def doc():
  return render_template('doc.html')

@app.route('/doc', methods = ['POST'])
def doc_push():
  name = request.form['patient']
  history = request.form['history']
  prescription = request.form['prescription']
  data_to_encrypt = history + "\n" + prescription
  print(data_to_encrypt)
  enc = encrypt_data(data_to_encrypt)
  print(str(enc))
  push_to_db(name, str(enc))
  return 'doc'

@app.route('/signup')
def signup():
  return 'signup'

@app.route('/history_and_prescription')
def prescrip():
  return 'history and prescription'

key = os.environ['key']
f = Fernet(key)

token = encrypt_data('hello world')
print(token)
print(decrypt_token(token))

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)
