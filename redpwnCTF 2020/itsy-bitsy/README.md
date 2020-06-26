# itsy-bitsy
**Category:** Crypto

**Points:** 436

**Description:**
> The itsy-bitsy spider climbed up the water spout...
> ` nc 2020.redpwnc.tf 31284 `
>
> **Author:** Boolean
>
> **Given:** itsy-bitsy.py

## Writeup
This one was interesting. Don't really think I took the right path on this one
because I had to "guess" part of the flag, but you will see how I came to that.
Why write this writeup then? Because it might have been a different approach to
this problem and might be useful (maybe).

Anyways, I ran the program to see what we are working with:
```
$ nc 2020.redpwnc.tf 31284
Enter an integer i such that i > 0: 2
Enter an integer j such that j > i > 0: 3
Ciphertext: 0011011011001010101010101110000100000011100100010100001010101010000000111011010000100011010011100010001110100011001110011000100110110010111010010110100110001111010010100111000111010111100010101011101001000100110010000100110100101000011111001111110111000000000010010100001100100000010011110110010000010
```

I opened the script and analyzed the program. The general *function* of
this program was to read in two integers, and output a binary ciphertext. One of
the integers had to be bigger than the other one and they *both* had to be greater
than 0.
```
#!/usr/bin/env python3

from Crypto.Random.random import randint

def str_to_bits(s):
    bit_str = ''
    for c in s:
        i = ord(c)
        bit_str += bin(i)[2:]
    return bit_str

def recv_input():
    i = input('Enter an integer i such that i > 0: ')
    j = input('Enter an integer j such that j > i > 0: ')
    try:
        i = int(i)
        j = int(j)
        if i <= 0 or j <= i:
            raise Exception
    except:
        print('Error! You must adhere to the restrictions!')
        exit()
    return i,j

def generate_random_bits(lower_bound, upper_bound, number_of_bits):
    bit_str = ''
    while len(bit_str) < number_of_bits:
        r = randint(lower_bound, upper_bound)
        bit_str += bin(r)[2:]
    return bit_str[:number_of_bits]

def bit_str_xor(bit_str_1, bit_str_2):
    xor_res = ''
    for i in range(len(bit_str_1)):
        bit_1 = bit_str_1[i]
        bit_2 = bit_str_2[i]
        xor_res += str(int(bit_1) ^ int(bit_2))
    return xor_res

def main():
    with open('flag.txt','r') as f:
        flag = f.read()
    for c in flag:
        i = ord(c)
        assert i in range(2**6,2**7)
    flag_bits = str_to_bits(flag)
    i,j = recv_input()
    lb = 2**i
    ub = 2**j - 1
    n = len(flag_bits)
    random_bits = generate_random_bits(lb,ub,n)
    encrypted_bits = bit_str_xor(flag_bits,random_bits)
    print(f'Ciphertext: {encrypted_bits}')

if __name__ == '__main__':
    main()
```

This program reads in the flag server-side and encrypts it using our numbers
we provided. The numbers we provided are put in the exponent of 2, making an
upper-bound and a lower-bound. The length of the flag is passed in to make sure
that they return the same number of bits as the flag. After generating a random
bit pattern and converting the flag into bits, the program does an XOR with both
bit streams. This is what we are seeing for the binary ciphertext given to us.
Interesting...

I made it certain in my head that there wasn't really a way to get around the
randomness of the generated bits (keep in mind I haven't seen any other solutions
before writing this). My approach was to take the smallest numbers I could do and
generate cases for my ciphertext.

If I entered in a 1 and 2. The **lower-bound** would be **2^1** and the
**upper-bound** would be **(2^2) - 1**. Making the randomly-generated bits to being
either *10* or *11* (2 <= random <= 3).

If I entered in a 2 and 3. The **lower-bound** would be **2^2** and the
**upper-bound** would be **(2^3) - 1**. Making the randomly-generated bits to being
either *100*, *101*, *110*, or *111* (4 <= random <= 7).

I started to see a pattern with this. If I chose the first option (1 and 2), every
other bit would *HAVE* to be a **1**. Well I guess that covers half of the bits.
I wanted more coverage, so I got samples for **(1,2)**, **(2,3)**, **(4,5)**,
**(6,7)**, **(10,11)**, and **(12,13)**. The only problem with this was all of the
prime numbers wouldn't be found (along with a few stragglers).

**Script:**
```
from pwn import *
from sympy import *
from binascii import *

ctwo = "0011011000011001101100001101000010010011010011100100101001011000100001011100100011110110100100010000111101000101011001011001000011010001101001010110100101001100100000010101000000010001000000011110011011100110100001010101100000101101011011011100000011010001000001110000011010010000000100010110110101000"
cthree = "0111101111111100011110011100010100010111110000000110011110001100110010111111110010100011010111010010011100100111011100011000000100100010101100100010110110101001000110110101010011110101110110111001001101000100010100110000110100111110101011101111010011000110010010100000011000100000110011000100010000010"
cfive = "0011100110010100100101000001110100101011011100110100001100001001000011001001101110111000010110010000110010110100011110101101000010000000111001110110100010100000110100110101101011100110000110010101000110000101010101100111101100000101001011101100000101010000111100000000011111111000011111110111101001000"
cseven = "0110001010101000001000000110010000100011110111111010100100001010110010010111100001010001111010111000000000110000000101101101100010011001000001001000010110000011000100000111110011010100011100111100011010001010010110010000011101110100011011010100001010100110111010001001010100000001000001001000110010111"
celeven = "0100110110100001101011011001111100100010010010010000000110011011110100010101101001000010100000000000110011111000111101101000010000000001011110111011000000000101000110011011100100101110011000010101101101101110100000101110101011101110010011000101001111011111000011000100100111110111000100000101010000100"

reconstructed = ''
re_list = []
for i in range(len(ctwo)):
    if i % 2 == 0:
        val = int(ctwo[i])
        reconstructed += "0" if val == 1 else "1"
    elif i % 3 == 0:
        val = int(cthree[i])
        reconstructed += "0" if val == 1 else "1"
    elif i % 5 == 0:
        val = int(cfive[i])
        reconstructed += "0" if val == 1 else "1"
    elif i % 7 == 0:
        val = int(cseven[i])
        reconstructed += "0" if val == 1 else "1"
    elif i % 11 == 0:
        val = int(celeven[i])
        reconstructed += "0" if val == 1 else "1"
    elif isprime(i):
        reconstructed += 'p'
    else:
        reconstructed += '?'
    if len(reconstructed) == 7:
        reconstructed = "0" + reconstructed
        re_list.append(reconstructed)
        reconstructed = ''

print(re_list)
vals = ["0", "1"]
flag = []
one = []
two = []
three = []
four = []
for r in re_list:
    count = 0
    for c in r:
        if c == "?" or c == "p":
            count += 1
    if count == 0:
        one.append(r)
        two.append(r)
        three.append(r)
        four.append(r)
    elif count == 1:
        oned = r.replace("?", "0").replace("p", "0")
        twod = r.replace("?", "1").replace("p", "1")
        one.append(oned)
        two.append(twod)
        three.append(twod)
        four.append(oned)
    else:
        one.append(r.replace("p", "0"))
        two.append(r.replace("p", "0", 1).replace("p", "1", 1))
        three.append(r.replace("p", "1", 1).replace("p", "0", 1))
        four.append(r.replace("p", "1"))

flag1 = []
for h in one:
    if "?" in h:
        flag1.append("?")
    else:
        flag1.append(chr(int(str(h), 2)))

flag2 = []
for h in two:
    if "?" in h:
        flag2.append("?")
    else:
        flag2.append(chr(int(str(h), 2)))

flag3 = []
for h in three:
    if "?" in h:
        flag3.append("?")
    else:
        flag3.append(chr(int(str(h), 2)))

flag4 = []
for h in four:
    if "?" in h:
        flag4.append("?")
    else:
        flag4.append(chr(int(str(h), 2)))

print(''.join(flag1))
print(''.join(flag2))
print(''.join(flag3))
print(''.join(flag4))
```

Yeah.... I probably could have reduced the repetitive code, but I really didn't
feel like doing it at the time. Looking back at this, I probably could have
enumerated the options for the prime parts, but that is a *lot* of options.

**Output:**
```
$ python3 itsy.py
FlagSbIpq[DdajajG_MptKdn?j_`@e_?adE?]spkU?}
fmcw[cKts_Leckcng_OqtOlo?k_dHe\x7f?ctM?_wro]?\x7f
Fligsripy[dtajizG_mtt[d~?n_p`e_?ide?]sxku?}
fmkw{skt{_luckk~g_out_l\x7f?o_the\x7f?ktm?_wzo}?\x7f
```

At this point, I recognized that I was pretty close. You can kind of see the flag
forming. It was just a matter of those primes because they showed up in every byte.

From here, all I really did was guess between the four options and see what looked
and sounded like English (yikes). Not the most impressive route, but it got me there.

## Flag
flag{bits_leaking_out_down_the_water_spout}

## Post Note
Now I'm gonna go look at the other writeups for this challenge and realize how much time
I probably wasted in this approach lol
