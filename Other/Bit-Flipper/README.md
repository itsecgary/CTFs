# Bit Flipper
**Category:** We're On the Same Wavelength

**Points:** 36

**Description:**
> mom said it's my turn flipping bits in the thermal protection system
> dad says don't touch the thermostat
>
> **Author:** Cromulence
>
> **Given:** encoded.bin

## Writeup
This challenge took me a long time for some reason, but I enjoyed solving it. Hack-
A-Sat2's challenges were taken down right after the competition, so I will be
using their local challenge repo for the purpose of this writeup. All of the challenges
can be found on [GitHub](https://github.com/cromulencellc/hackasat-qualifier-2021)
<br>

Now, to the writeup. We were given a file `encoded.bin` which looks like:

```
# Temper¶ature Seµnsor
# IRf temper¹ature abºove/belopw threshKold, dea]ctivate/[activate® heater
Timport sPys

def +readTemp=(temp,stŸate):
  ¬  if temBp < 15 aÔnd not s~tate:
  ’      prFint("Temãp: %.2fCñ Activatying heather"%tempL)
      …  returnú 1
    eólif temp4 > 35 anid state:M
       € print("dTemp: %.v2fC DeacÆtivating heater"Ù%temp)
 ¢       r@eturn 0
Ö    elseË:
      ?  returnú state

Â
```

We were also given a **nc** connection (in this case we will just run *challenge.py*
since it is local).

<br/>

Upon initially running the program, we receive:

```
$ python3 challenge.py
   BIT FLIPPER
    CHALLENGE

     10111100

You've been provided a special capability to target ionizing radiation on a region of memory used by a spacecraft's thermal protection system (TPS). Use this ability to flip the right combination of 3 bits that will pass SECDED checks, and change the behavior of the spacecraft's TPS when decoded from memory. Refering to the memory in its encoded form (encoded.bin), you must select a byte (0-404) and then which bit (0-7) in the byte to flip. You are allowed 3 bit flips.

Effect a change in the TPS such that the spacecraft exceeds its operating temperature range of 0-70C to obtain the flag.
Bitflip #1
   Select byte to ionize (0-404):
```

We see here that we have some sort of python file and we are told that we have the
special ability to change (up to 3) bits within this file. Off the bat, we notice
that `encoded.bin` should contain 405 bytes. This looks like a python program,
but that sure as hell wouldn't execute. What are the special characters for? Well, \
they have a purpose. Just wait. Let's do some research on what we were given.
<br>
**What exactly IS a SECDED check?**

SECDED (Single-Error Correcting | Double-Error Correcting) checks are used in
[Hamming Code](https://en.wikipedia.org/wiki/Hamming_code). Hamming Codes are
used to ensure there are no errors within the data sent from one party to another.
The special thing about Hamming Codes is that there are **parity** bits, which
are used to find out where the error is in the data, and fix it. In our case here,
we are given the power to flip bits within the python program, but it will be checked
(using SECDED checks) by the receiving end (aka the challenge service). I learned a
little bit about Hamming Code when I took a Digital Logic Design class in school,
but that was mainly dealing with 7-bit and 8-bit codes. This is a little different.

<br/>
<hr>

If you are unfamiliar with 7-bit and/or 8-bit Hamming Codes, here is a small
explanation. 7-bit hamming code (also known as Hamming(7,4)) contains 4 bits
of data and 3 parity bits, hence 7 bits.

<img src="https://latex.codecogs.com/png.latex?
\dpi{150}&space;\LARGE\color{Orange}&space;p_{1}&space;p_{2}&space;d_{1}&space;p_{3}&space;d_{2}&space;d_{3}&space;d_{4}&space;"/>

The parity bits are assigned to 3 of the 4 data bits to assess the parity of those
bits. The *parity* of bits essentially means if there are an odd number of 1s or
not (just an XOR). For example, if we wanted to send `0110` to another person/entity,
the Hamming(7,4) would look like:

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\LARGE\color{Orange}&space;p_{1}&space;p_{2}&space;0&space;p_{3}&space;1&space;1&space;0" />

Then the parity bits are added:

```
p1 looks at d1, d2, d3

p2 looks at d1, d3, d4

p3 looks at d2, d3, d4

1100110 is our final Hamming(7,4)

```

Now, Hamming(8,4) is practically the same, just with an extra parity bit. The
extra parity bit is added to the beginning and takes the parity of all 7 bits from
before. So, the 8-bit Hamming Code would look like:


<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\LARGE\color{Orange}&space;0&space;1&space;1&space;0&space;0&space;1&space;1&space;0&space;"/>


<hr>
<br/>

These SECDED checks happen to be for every 8 bytes of the file. You're probably
saying "well Gary... 405 isn't divisible by 8!" Well you're right, but we haven't
accounted for the parity bits, or should I say **parity byte**. 8 bytes of data
and 1 parity byte to govern those 8 bytes. This explains the weird characters
that occur after 8 bytes (if only I noticed this immediately smh).

We can represent the parity checks by what's called an "H-matrix".

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\huge&space;\color{Orange}\begin{bmatrix}&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?\\&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?\\&space;...&space;&&space;...&space;&&space;...&space;&&space;...&space;&&space;...&space;&&space;...&space;&&space;...&space;&&space;...\\&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;&&space;?&space;\end{bmatrix}"/>

Each row represents which bits in each byte of data will be checked for parity. Just
like Hamming(7,4), except it's Hamming(8,1) in some sense. The trick here is that
we don't know which parity bits are being tested for each byte, meaning we don't
know the H-matrix.

The challenge requires us to flip bits in a way for the python file to allow
temperatures outside of the operating range of 0-70C. There are a couple options
we can do here to make the Thermal Protection System (TPS) go outside of this zone.<br/><br/>

```
00100100
00101100 --- '<'
00101110 --- '>'
      ^
one bit diff


00100010 --- '3'
00100111 --- '7'
     ^ ^
two bits diff
```

<br/>
<i>There probably are other options, but we can just look at these two for now</i>.
One-bit difference is probably an easy go, so let's give it a shot. I will flip
the `<` in the first part of the if-statement to be a `>`. This means we will
flip bit at index 1 of the 155th byte. Since we are flipping a bit, one of the
parity checks will catch it (and correct it back to `>`). So we will
try to flip any of the bits of the 161at byte. The `Ô` is the parity byte for this block.
The program requires a 3rd bit to flip, so we will choose another random spot away
from the block we are flipping (let's put it in a comment) so we don't mess it up.

<br/><br/>

```
$ python3 challenge.py
   BIT FLIPPER
    CHALLENGE

     10111100

You've been provided a special capability to target ionizing radiation on a region of memory used by a spacecraft's thermal protection system (TPS). Use this ability to flip the right combination of 3 bits that will pass SECDED checks, and change the behavior of the spacecraft's TPS when decoded from memory. Refering to the memory in its encoded form (encoded.bin), you must select a byte (0-404) and then which bit (0-7) in the byte to flip. You are allowed 3 bit flips.

Effect a change in the TPS such that the spacecraft exceeds its operating temperature range of 0-70C to obtain the flag.

Bitflip #1
   Select byte to ionize (0-404): 155
   Select bit to ionize (0-7):    1
Bitflip #2
   Select byte to ionize (0-404): 161
   Select bit to ionize (0-7):    4
Bitflip #3
   Select byte to ionize (0-404): 2
   Select bit to ionize (0-7):    0
SECDED: single error corrected (data)
SECDED: single error corrected (data)
Temp: 24.99C Activating heater
Temp: 35.06C Deactivating heater
Temp: 35.05C Activating heater
Temp: 35.12C Deactivating heater
Temp: 35.11C Activating heater
Temp: 35.17C Deactivating heater

.
.
.

Temp: 70.00C Deactivating heater
Temp: 69.99C Activating heater
Temp: 70.05C Deactivating heater
The spacecraft exceeded its operating temperature! You got it!
Here's your flag:
flag{this_is_a_test_flag_inserted_by_Gary}
```

After some iterations, we found that the 4 index of the parity byte made our little
change from `<` to `>` slide right pass the SECDED check :)
<br>

## Flag
`flag{this_is_a_test_flag_inserted_by_Gary}` (well I manually inserted this one)
<br>

## Resources
[Hamming Code](https://en.wikipedia.org/wiki/Hamming_code)

[Hamming(7,4)](https://en.wikipedia.org/wiki/Hamming(7,4))

[Hamming codes and error correction video](https://www.youtube.com/watch?v=X8jsijhllIA)
