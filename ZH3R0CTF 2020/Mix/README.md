# Mix
**Category:** Crypto

**Points:** 330

**Description:**
> At the BASEment no. 65536, A man is irritated with SHIFT key in his KEYBOARD
as it's a sticky key, A kid is having chocolate icecream with a SPOON.
>
> **Author:** Whit3_D3vi1
>
> **Given:** flag.txt && chall_encrypted.txt

## Writeup
I opened `flag.txt` and got absolutely pwned :(
```
If you opened this then you are a n00b
```

From the hint, we can see that the uppercase letters are telling us something.
It seems this encrypted text is in base65536. [Here](https://www.better-converter.com/Encoders-Decoders/Base65536-Decode)
is a link to a decoder. After decoding, we get the following output:
```
flag 1:
Yjod od s lrunpstf djogy vo[jrtyrcy jrtr od upi g;sh xj4t-}U-i+dit4+

flag 2:
3030313130313030203031313130303130203030313130303131203031303131313131203030313130313030203031313130313131203030313130303131203031313130303131203030313130303030203031313031313031203030313130303131203031303131313131203031313130313131203031313031303031203030313130313131203031313031303030

flag 3:
MTExMTExMTExMTAwMTAwMDEwMTAxMDExMTAxMDExMTExMTEwMTAxMTExMTExMTExMDExMDExMDExMDExMDAwMDAxMTAxMDAxMDAxMDAxMDAwMDAwMDAwMDAwMDAwMDAwMTAxMDAxMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTAxMDAwMDAwMDAwMDAwMTAxMDAwMTAxMDAxMDAwMTAxMDAxMTExMTExMTAwMTAxMDAxMDExMTExMTExMTAwMTAxMDAxMTAwMDAwMDAwMDAwMDAwMTAxMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTAxMDExMTExMTExMTExMTExMTExMTExMDAxMDEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDEwMDAwMDAwMDAxMDEwMDExMDAwMDAwMDAxMDEwMDAxMDEwMTExMTAwMTAxMDAxMDExMTExMTExMTExMTExMTExMTExMDAxMDEwMDExMDExMDExMTExMTExMTExMTAwMTAxMA==
```

Looks like we know what to do now!

**Flag 1:** [Keyboard Shift Cipher](https://www.dcode.fr/keyboard-shift-cipher)
```
# After plugging and chugging
zh3r0{Y0u_sur3_
```

**Flag 2:** [Hex -> Binary -> ASCII]("https://gchq.github.io/CyberChef/#recipe=From_Hex('None')From_Binary('Space'))
```
# Hex to Binary
00110100 01110010 00110011 01011111 00110100 01110111 00110011 01110011 00110000 01101101 00110011 01011111 01110111 01101001 00110111 01101000

# Binary to ASCII
4r3_4w3s0m3_wi7h
```

**Flag 3:** [Spoon Cipher](https://www.dcode.fr/spoon-language)
```
_411_7h3_ski115}
```

Combining the flags together gives us the flag.

## Flag
zh3r0{Y0u_sur3_4r3_4w3s0m3_wi7h_411_7h3_ski115}
*props to birch for helping me out on this one*
