# Katycat
**Category:** Forensics

**Points:** 175

**Description:**
> katycat trying to find the flag but she is lazy. will you help her to find the flag?
>
> **Author:** cryptonic007
>
> **Given:** katy.png

## Writeup
Let's take a peek at what we are working with:
![PNG file](https://github.com/itsecgary/CTFs/blob/master/ZH3R0CTF%202020/Katykat/katy.png)

Welp at least it's a cute cat lol. Next step I like to do is check the contents
of the PNG in a hex editor. I use **HxD** to do this.

**Header:**
```
89 50 4E 47 ---> ‰PNG
```

**Footer:**
```
49 45 4E 44 AE 42 60 82  ---> IEND®B`‚
```

Doesn't look like anything is wrong so far. Next step I like to do is take it to
the CLI and run a few different tools until something hits. I like to use **binwalk**
and **foremost** to try to find hidden files. I also like to use **zsteg** and
**strings** to try to find hidden info.

This time around, we get a hit on **zsteg**:
```
$ zsteg katy.png
b1,rgb,lsb,xy       .. text: "https://pastebin.com/hvgCXNcP"
b2,r,msb,xy         .. file: PGP Secret Key -
b2,rgb,msb,xy       .. text: "EEQPUUU@U"
b2,abgr,msb,xy      .. text: "WSSWCCCCSSWWCC"
b3,bgr,msb,xy       .. text: "(Z0-X0-H"
b4,r,lsb,xy         .. text: "DfffdDB\""
b4,r,msb,xy         .. text: "@\"fa\"DD$DD"
b4,g,lsb,xy         .. text: "D\"\"$\"D\"\"\" "
b4,g,msb,xy         .. text: "&b\"fa\"DD$D\"DDD"
b4,b,lsb,xy         .. text: "vPUFwDT!"
b4,b,msb,xy         .. text: "USUs33UU&\"Q3"
b4,rgb,lsb,xy       .. text: "hDdD\"B$\"\"\"\"dF\"b$$"
b4,rgb,msb,xy       .. text: "QU3sUS53337uSp"
b4,bgr,lsb,xy       .. text: "fdDDB$\"\"\"\"b&Db$\""
b4,bgr,msb,xy       .. text: "Su3S5U3335WsuP"
b4,abgr,msb,xy      .. text: "?U?U?5?5?"
```

Looks like we got a link. Following the trail leads us to a Paste Bin of:
```
UEsDBAoACQAAALq0vFDu3sG8JQAAABkAAAAIABwAZmxhZy50eHRVVAkAA+jvz179789edXgLAAEE
6AMAAAToAwAAt9tbOQhvceVTC9i83YoBgbIW5fmqoaO3mVwXSLOMqNulwvcwb1BLBwju3sG8JQAA
ABkAAABQSwECHgMKAAkAAAC6tLxQ7t7BvCUAAAAZAAAACAAYAAAAAAABAAAApIEAAAAAZmxhZy50
eHRVVAUAA+jvz151eAsAAQToAwAABOgDAABQSwUGAAAAAAEAAQBOAAAAdwAAAAAA
```

This seems to be in Base64 form. After a **base64 decode** I get:
```
PK
	P%flag.txtUT	^^ux[9oqSؼ݊\Hۥ0oPK%PK
	P%flag.txtUT^uxPKNw
```

I wasn't familiar with this file header at first, but doing some research told
me that this was the header for a ZIP file. I will put a link to file headers
in the *Resources* section at the bottom.

I pasted the contents of what we got above and added the .zip extension. When
trying to open it, we are prompted with a password. I try a few common passwords
just to see, but no luck.

This is where **John the Ripper** comes in handy:
```
$ ~/tools/JohnTheRipper/run/zip2john enc2.zip > hash
ver 1.0 efh 5455 efh 7875 enc2.zip/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=37, decmplen=25, crc=BCC1DEEE type=0

$ ~/tools/JohnTheRipper/run/john hash --show
enc2.zip/flag.txt:kitkat:flag.txt:enc2.zip::enc2.zip

1 password hash cracked, 0 left
```

Sweet. Cracked it. Goes with the name of the challenge a little bit too. Opening
the zip file with this password
```
$ unzip enc2.zip
Archive:  enc2.zip
[enc2.zip] flag.txt password:
 extracting: flag.txt

$ cat flag.txt
K9bC_L`D?f0DEb8c?_06cDJN
```

Not there yet, but pretty close. After a little shuffling around with ciphers, I
figured out this was a ROT-47 shift cipher. Similar to the ROT-13, but with a
bigger charset. I wrote a script to do this, but there is an amazing online tool
called **CyberChef** that can do this for us.

Here is my script:
```
from  pwn import *

ct = open("flag.txt", "r").read()

arr = []
for c in ct:
    arr.append(ord(c))

flag = ""
for a in arr:
    val = a + 47
    if val > 126:
        val = 32 + (val - 126)
    flag += chr(val)

log.success("Flag: {}".format(flag))
```

**Output:**
```
$ python3 shift.py
[+] Flag: zh3r0{1sn7_st3g4n0_e4sy}
```

## Flag
zh3r0{1sn7_st3g4n0_e4sy}

## Resources
File Headers - https://www.garykessler.net/library/file_sigs.html

John The Ripper Wiki - https://en.wikipedia.org/wiki/John_the_Ripper

John The Ripper Tips - https://www.varonis.com/blog/john-the-ripper/

CyberChef - https://gchq.github.io/CyberChef/
