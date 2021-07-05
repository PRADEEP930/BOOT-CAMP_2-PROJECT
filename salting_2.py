# genetate a hash of a given string with added salt and iterations.
#-->Take input as string
#-->Generate a hash with salt and iterations
#-->Print the hash with
#-->check the the generated hash with the string given
#*****The above step can be used for authentication purposes in data base. ******
#*****print the check result : TRUE means string and hash matched .        ******

import bcrypt
str = input("enter the string to hash :\n")
data = str.encode('utf-8')
hash = bcrypt.hashpw(data, bcrypt.gensalt(prefix=b'2b', rounds=10))
print(hash)
ck = bcrypt.checkpw(data,hash)
print(ck)