# pseudo-key
**Category:** Crypto

**Points:** 341

**Description:**
> Keys are not always as they seem...
>
> **Note:** Make sure to wrap the plaintext with `flag{}` before you submit!
>
> **Author:** Boolean
>
> **Given:** pseudo-key-output.txt && pseudo-key.py

## Writeup
First thing I do here is look at the files given to us. Looks like we are given
the ciphertext and some "pseudo-key".
```
Ciphertext: z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut
Pseudo-key: iigesssaemk
```

From the program itself, it looks like our ciphertext is encrypted with some key, but
we are given the key encrypted with itself. Interesting...
```
#!/usr/bin/env python3

from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

def encrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(x + y) % 26]
    return ctxt

with open('flag.txt') as f, open('key.txt') as k:
    flag = f.read()
    key = k.read()

ptxt = flag[5:-1]

ctxt = encrypt(ptxt,key)
pseudo_key = encrypt(key,key)

print('Ciphertext:',ctxt)
print('Pseudo-key:',pseudo_key)
```

The encryption method pretty much takes the alphabetical number value of each
character of the "plaintext", adds it to the alphabetical number value of the key
and wraps it around if the sum is greater than 26.

This is where I was very twisted for a day or so. I overthought the hell out of
this problem. We realized before that the key given to us is completely wrong and is
just the result of encrypting the key with itself. I figured out that each of these
characters in the key has a total of 2 possible values it could actually be.

Let's take a look at the possible values of all 26 chars in the alphabet:
```
a: (0 + 0) % 26 = 0 (a)
b: (1 + 1) % 26 = 2 (c)
c: (2 + 2) % 26 = 4 (e)
...
...
m: (12 + 12) % 26 = 24 (y)
n: (13 + 13) % 26 = 0 (a)
o: (14 + 14) % 26 = 2 (c)
p: (15 + 15) % 26 = 4 (e)
```

We can see here that there are really only 13 possible characters that could be
in the key. Let's get each possibility for our characters.
```
i = e | r
i = e | r
g = d | q
e = c | p
s = j | w
s = j | w
s = j | w
a = a | n
e = c | p
m = g | t
k = f | s
```

Now, I'm not sure what other people had for their approach, but I straight-up
iterated through all possible combinations of this key. There are 2^11 (2048)
key possibilities. I wrote a script to do this for me and decrypt the flag as
well. So, this will basically output 2048 different flag options. This is harder
since I don't have the "flag{}" wrapper here to help me, but oh well.

**Script:**
```
def get_plain(ct, key):
    plain = ''
    key = ''.join(key[i % len(key)] for i in range(len(ct)))
    for i in range(len(ct)):
        if ct[i] == '_':
            plain += ct[i]
            continue
        c = ord(ct[i]) - 97
        k = ord(key[i]) - 97
        if c > k:
            plain += chr(c-k+97)
        elif c < k:
            plain += chr(26-k+c+97)
        else:
            plain += chr(c+97)
    return plain


psuedo_key = "iigesssaemk"
ct = "z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"

i = ['e', 'r']
g = ['d', 'q']
e = ['c', 'p']
s = ['j', 'w']
a = ['a', 'n']
m = ['g', 't']
k = ['f', 's']
possible_keys = []

for ii in i:
    for ii2 in i:
        for gg in g:
            for ee in e:
                for ss in s:
                    for ss2 in s:
                        for ss3 in s:
                            for aa in a:
                                for ee2 in e:
                                    for mm in m:
                                        for kk in k:
                                            test = ii + ii2 + gg + ee + ss + ss2 + ss3 + aa + ee2 + mm + kk
                                            possible_keys.append(test)

for key in possible_keys:
    plain = get_plain(ct, key)
    print(plain)
```

Probably a more efficient way of doing what I did, butttttt oh well.

**Output: (count)**
```
$ python3 solve.py > output && wc -l output
2048 output
```

Scrolling through the 2048 options, I could kind of tell what some of these words
were going to be. I did a search on a pair of words to narrow down the options.
```
$ cat output | grep "i_guess"
i_guess_pfeudo_keyf_nre_pseudb_fecure
i_guess_pfrudo_keyf_nee_pseudb_frcure
i_guess_pseudo_keyf_tre_pseudb_secure
i_guess_psrudo_keyf_tee_pseudb_srcure
i_guess_cfeudo_keyf_nre_pseudb_fecure
i_guess_cfrudo_keyf_nee_pseudb_frcure
i_guess_cseudo_keyf_tre_pseudb_secure
i_guess_csrudo_keyf_tee_pseudb_srcure
i_guess_pfeudo_keys_nre_pseudo_fecure
i_guess_pfrudo_keys_nee_pseudo_frcure
i_guess_pseudo_keys_tre_pseudo_secure
i_guess_psrudo_keys_tee_pseudo_srcure
i_guess_cfeudo_keys_nre_pseudo_fecure
i_guess_cfrudo_keys_nee_pseudo_frcure
i_guess_cseudo_keys_tre_pseudo_secure
i_guess_csrudo_keys_tee_pseudo_srcure
i_guess_pfeuqo_keyf_nre_pseudb_fechre
i_guess_pfruqo_keyf_nee_pseudb_frchre
i_guess_pseuqo_keyf_tre_pseudb_sechre
i_guess_psruqo_keyf_tee_pseudb_srchre
i_guess_cfeuqo_keyf_nre_pseudb_fechre
i_guess_cfruqo_keyf_nee_pseudb_frchre
i_guess_cseuqo_keyf_tre_pseudb_sechre
i_guess_csruqo_keyf_tee_pseudb_srchre
i_guess_pfeuqo_keys_nre_pseudo_fechre
i_guess_pfruqo_keys_nee_pseudo_frchre
i_guess_pseuqo_keys_tre_pseudo_sechre
i_guess_psruqo_keys_tee_pseudo_srchre
i_guess_cfeuqo_keys_nre_pseudo_fechre
i_guess_cfruqo_keys_nee_pseudo_frchre
i_guess_cseuqo_keys_tre_pseudo_sechre
i_guess_csruqo_keys_tee_pseudo_srchre
```

I'm guessing my script had a tiny error with the "are" part of the flag, but it
worked.

## Flag
flag{i_guess_pseudo_keys_are_pseudo_secure}
