from pwn import *
import gmpy2
import gmpy
from Crypto.Util.number import long_to_bytes

n = int(open("n", "r").read()) 
c = int(open("c", "r").read())
e = 65537

root, extra = gmpy2.iroot(n,3)
root = int(root)

p = root
while n % p != 0:
    p -= 1

qr = n // p
root2, extra2 = gmpy2.iroot(qr,2)
root2 = int(root2)

q = root2
while qr % q != 0:
    q -= 1

r = qr // q
print("P: {}".format(p))
print("Q: {}".format(q))
print("R: {}".format(r))

phi = (p-1)*(q-1)*(r-1)

d = gmpy.invert(e, phi)
flag = long_to_bytes(pow(c,d,n)).decode("utf-8")
log.success("Flag: {}".format(flag))

