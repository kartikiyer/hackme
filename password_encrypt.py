from cryptography.fernet import Fernet

key = Fernet.generate_key()

crypter = Fernet(key)

pw = crypter.encrypt(b'Tryhackme@321')


decrypt = crypter.decrypt(pw)

print(pw)
print(decrypt)
