from pwn import *
import math
import sys

def modinv(a,m):
    g,x,y = egcd(a,m)
    if g != 1:
        return None
    else:
        return x%m

# function to find extended gcd
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b / gcd(a, b)

n1 = int(open("n1", "r").read())
n2 = int(open("n2", "r").read())
n3 = int(open("n3", "r").read())
c1 = int(open("c1", "r").read())
c2 = int(open("c2", "r").read())
c3 = int(open("c3", "r").read())

P = int(open("P", "r").read())
Q = int(open("Q", "r").read())
R = int(open("R", "r").read())
e = 65537

#phi1 = lcm(P-1,Q-1)
phi1 = (P-1)*(Q-1)
d1 = modinv(e, phi1)
p1 = pow(c1, d1, n1)
ph1 = (str(hex(p1))).split('x')[1].split("L")[0]
flag1 = bytes(ph1).decode("hex")
print("-----------------------------------------------------------------------------------------------------------------")
print("phi: {}\nd: {}\nflag: {}".format(phi1,d1,flag1))

phi2 = lcm(Q-1,R-1)
d2 = egcd(e, phi2)[1]
p2 = pow(c2, d2, n2)
ph2 = (str(hex(p2))).split('x')[1].split("L")[0]
flag2 = bytes(ph2).decode("hex")
print("-----------------------------------------------------------------------------------------------------------------")

phi3 = lcm(P-1,R-1)
d3 = egcd(e, phi3)[1]
p3 = pow(c3, d3, n3)
ph3 = (str(hex(p3))).split('x')[1].split("L")[0]
flag3 = bytes(ph3).decode("hex")
print("-----------------------------------------------------------------------------------------------------------------")

final_flag = flag1 + flag2 + flag3
log.success("FLAG: {}".format(final_flag))

#print("P: ".format(P))
#print("Q: ".format(Q))
#print("R: ".format(R))
#print("N1 = P*Q? {}".format(P*Q == n1))
#print("N2 = Q*R? {}".format(R*Q == n2))
#print("N3 = P*R? {}".format(P*R == n3))

