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
