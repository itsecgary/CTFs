from z3 import *

s = Solver()

def triple_xor(a, b, c):
    return Xor(Xor(a, b), c)

#layer 0
bits2 = [Bool(str(i)) for i in range(64)]
bits = [Bool(str(i)) for i in range(64)]
inp_consts = "0 1 1 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 0 1 1 0 1 1 1 1 0 1 1 0 0 0 0 0 0 1 1 1 0 1 1 0 1 0 1 0 1 1 1 1 0 1 1"
inp_consts = list(map(lambda x: bool(int(x)), inp_consts.split()))
assert len(inp_consts) == 64

for i in range(len(bits)):
    bits[i] = Xor(bits[i], inp_consts[i])

# layer 1
outs = []
outs.append(triple_xor(False, False, bits[0]))
most_recent = Or(And(False, bits[0]), And(False, bits[0]), And(False, False))
outs.append(triple_xor(most_recent, bits[0], bits[1]))
most_recent = Or(And(most_recent, bits[1]), And(most_recent, bits[0]), And(bits[1], bits[0]))
for i in range(2, 64):
    a = i-2
    b = i-1
    c = i
    print(a, b, c)
    outs.append(triple_xor(most_recent, bits[b], bits[c]))
    most_recent = Or(And(most_recent, bits[c]), And(most_recent, bits[b]), And(bits[b], bits[c]))

assert len(outs) == 64, len(outs)

# layer 2
outs_2 = []
for i in range(1, 64):
    outs_2.append(Xor(outs[i-1], outs[i]))
outs_2.append(Xor(False, outs[-1]))

assert len(outs_2) == 64, len(outs_2)

# layer 3
bottom_consts = "0 1 1 1 0 1 1 0 0 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 1 1 0 0 1 0 0"
bottom_consts = list(map(lambda x: bool(int(x)), bottom_consts.split()))
assert len(bottom_consts) == 64

out_consts = "0 0 1 0 1 0 0 0 0 0 0 1 0 0 0 0 1 1 1 0 0 1 1 0 1 0 0 0 1 0 1 0 1 1 0 1 0 1 0 1 0 1 0 0 0 0 1 0 1 1 0 1 0 1 0 0 0 1 1 1 1 1 0 0"
out_consts = list(map(lambda x: bool(int(x)), out_consts.split()))
assert len(out_consts) == 64

#s.add(triple_xor(outs_2[-1], outs_2[0], False) == False)
#most_recent = Or(And(outs_2[-1], False), outs_2[0])
s.add(triple_xor(False, outs_2[1], True) == False)
most_recent = Or(And(False, True), And(False, outs_2[1]), And(outs_2[1], True))

for i in range(2, len(outs_2)):
    print(i-1, i, bottom_consts[i], out_consts[i])
    s.add(triple_xor(most_recent, outs_2[i], bottom_consts[i]) == out_consts[i])
    most_recent = Or(And(most_recent, bottom_consts[i]), And(most_recent, outs_2[i]), And(outs_2[i], bottom_consts[i]))

s.add(triple_xor(most_recent, outs_2[0], False) == False)
# ----

assert len(s.assertions()) == 64
print(s.check())
m = s.model()
print(m)

out = ''
for i in range(64):
    out += str(int(bool(m[bits2[i]])))

print(out)
flag = b"CTF{"
while out:
    byte, out = out[:8], out[8:]
    flag += bytes([ int(byte[::-1], 2) ])
flag += b"}"

print(flag)
