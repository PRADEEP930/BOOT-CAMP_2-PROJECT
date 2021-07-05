'''_____________________________________________________________________________
*****      Generate hash of given string data using different algorithm    *****
-> Take the input from user as string data.
-> Take number of different hashing algrithms user wants.
-> choice random algorithms from the algo_list.
-> NOT to repeat the algorithms from the algo_list.
-> Generate its hash and print.
================================================================================'''
import hashlib
import random 
data = input("Enter the string to get it's hash by different algorithms : \n")

md5 = hashlib.md5() ;sha1 = hashlib.sha1();sha512 = hashlib.sha512();sha224 = hashlib.sha224();
sha384 = hashlib.sha384();blake2s = hashlib.blake2s(); sha3_224 = hashlib.sha3_224(); sha256 = hashlib.sha256();
sha3_384 = hashlib.sha3_384();blake2b = hashlib.blake2b(); shake_128 = hashlib.shake_128();
sha3_512 = hashlib.sha3_512();sha3_256 = hashlib.sha3_256(); shake_256 = hashlib.shake_256();

algo_list_all = [sha512, sha224, sha384,blake2s, sha3_224, sha256, sha1, sha3_384, md5, blake2b, shake_128, sha3_512, sha3_256, shake_256]
algo_list = []
n = int(input("enter number of algorithms you want to use <=14 : \n"))
for i in range(0,n):
    algo = random.choice(algo_list_all)
    algo_list.append(algo)
    algo_list_all.remove(algo)

for algo in algo_list:
    if algo == shake_128 or algo == shake_256:
        algo.update(data.encode('utf8'))
        hash = algo.hexdigest(20)
        print("{} : {}".format(algo.name, hash))
    else:
        algo.update(data.encode('utf8'))
        hash = algo.hexdigest()
        print("{} : {}".format(algo.name, hash))