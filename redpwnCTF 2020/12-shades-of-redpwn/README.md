# 12-shades-of-redpwn
**Category:** Crypto

**Points:** 429

**Description:**
> Everyone's favorite guess god Tux just sent me a flag that he somehow
encrypted with a color wheel!
>
> I don't even know where to start, the wheel looks more like a clock than a
cipher... can you help me crack the code?
>
> **Author:** Boolean
>
> **Given:** ciphertext.jpg && color-wheel.jpg

## Writeup
This one took me a while to figure out for some reason (lol). The hint gave me
the idea that the colors in the chart were corresponding to the numbers on the
clock (1-12), but I was just a tiny bit wrong. The color wheel had values
**(0-11)**, but in hex *obviously...* (sarcasm). Here is my edited version:

![Color Wheel](https://github.com/itsecgary/CTFs/tree/master/redpwnCTF%202020/12-shades-of-redpwn/color-wheel_EDITED.jpg)

Now, with this and our ciphertext, we can start plugging and chugging values. Our
result is the following:
```
86 90 81 87 a3 49 99 43 97 97 41 92 49 7b 41 97 7b 44 92 7b 44 96 98 a5
```

Translating this from hex to ASCII, doesn't give us anything but gunk...
```
....¢I.C..A.I{A.{D.{D..¥
```

After a while of staring at this stupuid color wheel and hex values I derived from
it, I started noticing that ` 86 90 81 87 ` represents ` flag ` and the `a3` and
`a5` values are two apart (have to be curly braces). It finally hit me that this is
in base12. This changes our ascii representation of these values:
```
41 -> 1          62 -> J          83 -> c          a4 -> |
42 -> 2          63 -> K          84 -> d          a5 -> }
43 -> 3          64 -> L          85 -> e
44 -> 4          65 -> M          86 -> f
45 -> 5          66 -> N          87 -> g
46 -> 6          67 -> O          88 -> h
47 -> 7          68 -> P          89 -> i
48 -> 8          69 -> Q          8a -> j
49 -> 9          6a -> R          8b -> k
4a -> :          6b -> S          90 -> l
4b -> ;          70 -> T          91 -> m
50 -> <          71 -> U          92 -> n
51 -> =          72 -> V          93 -> o
52 -> >          73 -> W          94 -> p
53 -> ?          74 -> X          95 -> q
54 -> @          75 -> Y          96 -> r
55 -> A          76 -> Z          97 -> s
56 -> B          77 -> [          98 -> t
57 -> C          78 -> \          99 -> u
58 -> D          79 -> ]          9a -> v
59 -> E          7a -> ^          9b -> w
5a -> F          7b -> _          a0 -> x
5b -> G          80 -> '          a1 -> y
60 -> H          81 -> a          a2 -> z
61 -> I          82 -> b          a3 -> {
```

Now decoding with our base12 ASCII representation gives us the flag.

## Flag
flag{9u3ss1n9_1s_4n_4rt}

## Resources
[ASCII Chart](http://www.asciitable.com/)
