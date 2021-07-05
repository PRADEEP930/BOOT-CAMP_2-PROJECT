'''_____________________________________________________________________________________________________
*****      Generate MD5 hash of given string data,add salting and iteration to final MD5 hash      *****
-> Take the input from user as string data.
-> Generate its MD5 hash and print.
-> Add salting to original string and iteration.
-> Print the final slated and iterated MD5 hash.
========================================================================================================='''
import hashlib, binascii
data = input("Enter the string to get ist MD5 hash : \n")
hash = hashlib.md5(data.encode('utf-8')).hexdigest()
print( "The md5 hash is : \n",hash)
data_b = data.encode('utf-8')
hash_2 = hashlib.pbkdf2_hmac('md5',data_b,b'yougotitrightsalt',100000)
final_hash = binascii.hexlify(hash_2)
print("The final slated and iterated MD5 hash is : \n",final_hash)