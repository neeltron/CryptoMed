from cryptography.fernet import Fernet
from replit import db
import os
from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__,template_folder='templates', static_folder='static')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db['testuser'] = 'pass123'

def fetch_new_key():
  key = Fernet.generate_key()
  return key

def encrypt_data(data):
  token = f.encrypt(b''+bytes(data, 'utf-8'))
  # print(str(token))
  return token

def decrypt_token(token):
  dec = f.decrypt(token)
  return dec

def push_to_db(name, data):
  db[name+'o'] = data
  return "Pushed to database successfully"

def fetch_from_db(name):
  data = db[name+'o']
  # print(data[2:-1])
  token = bytes(data[2:-1], 'utf-8')
  print(token)
  decrypted_data = f.decrypt(token).decode('utf-8')
  # print(decrypted_data)
  return decrypted_data

@app.route('/')
def hello_world():
  return render_template('login.html')

@app.route('/', methods = ['POST'])
def hello_world_post():
  username = request.form['username']
  password = request.form['password']
  # print(username, password)
  if db[username] == password:
    session['name'] = username
    # print('you\'re in')
    return redirect(url_for('prescrip'))

@app.route('/doc')
def doc():
  return render_template('doc.html')

@app.route('/doc', methods = ['POST'])
def doc_push():
  name = request.form['patient']
  history = request.form['history']
  prescription = request.form['prescription']
  data_to_encrypt = history + "\n" + prescription
  # print(data_to_encrypt)
  enc = encrypt_data(data_to_encrypt)
  # print(str(enc))
  push_to_db(name, str(enc))
  return redirect(url_for('hello_world'))

@app.route('/signup')
def signup():
  return 'signup'

@app.route('/history_and_prescription')
def prescrip():
  name = session['name']
  # print(name)
  history = fetch_from_db(name)
  print(history)
  data = [name, history]
  return render_template('patient.html', data = data)

key = os.environ['key']
f = Fernet(key)

token = encrypt_data('hello world')
# print(token)
# print(decrypt_token(token))

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)
