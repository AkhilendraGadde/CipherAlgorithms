#!/usr/bin/python3
'''
    @ODiN -iwnl-
    Implementation of RSA algorithm
'''

import random
import re
from random import randint as ri

_primeSet = [3,7,11,13,17,19,23,29,31,37,41,43,47,53]
_largePrimeSet = [] # choose from here instead of reading from file.

def largePrimes():
    f = open("largeprimes.txt","r")
    data = f.read().splitlines()
    f.close()
    dataList = random.choice(data)
    sets = re.findall(r'\d{1,11}',dataList)
    return (int(sets[ri(0,1)]),int(sets[ri(2,3)]))

def main():
    (p,q) = largePrimes()
    #print ("P : {} \nQ : {}".format(p,q))
    n = p*q
    #print (n)
    e = random.choice(_primeSet)
    #print (e)
    fN = (p-1)*(q-1)
    #print (fN)

    # diagnosis
    # for k in range(1,10000000000):
    #     d = (1+k*fN) / e
    #     if isinstance(d , int) and d is int(d):
    #         break
    #     print (d)

    '''
    pt = 100
    ct = 120
    '''
    Ct = (100**e) % n
    print (Ct)


if __name__ == "__main__":
    main()
