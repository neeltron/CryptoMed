from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

key = 'BDst0ZW7Qfbw_ntcJaQgnse-lNgiczBq7Cjz8OwX4gc='

f = Fernet(key)

token = f.encrypt(b'hello world')
print(token)
print(f.decrypt(token))
