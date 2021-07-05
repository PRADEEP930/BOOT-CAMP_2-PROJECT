'''_________________________________________________________
*****      Generate MD5 hash of given string data      *****
-> Take the input from user as string data.
-> generate its MD5 hash and print.
========================================================='''
import hashlib
data = input("Enter the string to get ist MD5 hash : \n")
hash = hashlib.md5(data.encode('utf-8')).hexdigest()
print(hash)