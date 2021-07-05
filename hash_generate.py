'''___________________________________________________________________________
*****      Generate hash of given string data using three algorithms     *****
-> Take the input from user as string data.
-> Use three different hashing algrithms
-> generate its hash and print.
=============================================================================='''
import hashlib
data = input("Enter the string to get ist hash by three algorithms : \n")
hash_1 = hashlib.blake2s(data.encode('utf-8')).hexdigest()
hash_2 = hashlib.shake_128(data.encode('utf-8')).hexdigest(20)
hash_3 = hashlib.md5(data.encode('utf-8')).hexdigest()
print(" blake2s   : {} \n shake_128 : {} \n md5       : {}".format(hash_1, hash_2, hash_3))