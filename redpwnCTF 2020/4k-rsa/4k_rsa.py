import gmpy
from pwn import *
from Crypto.Util.number import long_to_bytes
import binascii
from factordb.factordb import FactorDB

n = int(open("n", "r").read())
c = int(open("c", "r").read())
e = 65537 

f = FactorDB(n)
f.connect()
arr = f.get_factor_list()

phi = 1
for a in arr:
    phi *= (a-1)

d = gmpy.invert(e, phi)
flag = long_to_bytes(pow(c,d,n)).decode()
log.success("Flag: {}".format(flag))

