# primimity
**Category:** Crypto

**Points:** 450

**Description:**
> People claim that RSA with two 1024-bit primes is secure. But I trust no one.
That's why I use three 1024-bit primes.
>
> I even created my own prime generator to be extra cautious!
>
> **Author:** Boolean
>
> **Given:** primimity.py && primimity-public-key.txt

## Writeup
Looking at **priminity.py**, we see that the prime generation generates three
primes: **p**, **q**, and **r**. It picks a random 1024-bit number, then finds
the next prime - (d+1) primes away.
```
#!/usr/bin/env python3

from Crypto.Util.number import getRandomNBitInteger, isPrime

def find_next_prime(n):
    if n <= 1:
        return 2
    elif n == 2:
        return 3
    else:
        if n % 2 == 0:
            n += 1
        else:
            n += 2
        while not isPrime(n):
            n += 2
        return n

def prime_gen():
    i = getRandomNBitInteger(1024)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    p = find_next_prime(i)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    q = find_next_prime(i)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    r = find_next_prime(i)
    return (p,q,r)

def main():
    (p,q,r) = prime_gen()
    print(p)
    print(q)
    print(r)

if __name__ == '__main__':
    main()
```

Running this program once, we get an example output of:
```
$ python3 primimity.py
104857957995802113202799155043146383738317717869506487255733554982237834412439876073175028008556725572257508977034962752889399455584848024999705402597044673244677421623166376772490220536819588049922242374474030586464211019488836847121605902635938292012081202316987359553541112952345050585956025016297736305427
104857957995802113202799155043146383738317717869506487255733554982237834412439876073175028008556725572257508977034962752889399455584848024999705402597044673244677421623166376772490220536819588049922242374474030586464211019488836847121605902635938292012081202316987359553541112952345050585956025016297736436659
104857957995802113202799155043146383738317717869506487255733554982237834412439876073175028008556725572257508977034962752889399455584848024999705402597044673244677421623166376772490220536819588049922242374474030586464211019488836847121605902635938292012081202316987359553541112952345050585956025016297736606427
```

We can spot that the difference in the primes are very small (small enough to
enumerate). Basiclaly, we are just exploiting this prime gap to find our
**p**, **q**, and **r**.

**Script:**
```
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
```

**Output:**
```
$ python3 solve.py
P: 139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409208581
Q: 139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409397803
R: 139926822890670655977195962770726941986198973494425759476822219188316377933161673759394901805855617939978281385708941597117531007973713846772205166659227214187622925135931456526921198848312215276630974951050306344412865900075089120689559331322162952820292429725303619113876104177529039691490258588465409494847
[+] Flag: flag{pr1m3_pr0x1m1ty_c4n_b3_v3ry_d4ng3r0u5}
```

## Flag
flag{pr1m3_pr0x1m1ty_c4n_b3_v3ry_d4ng3r0u5}
