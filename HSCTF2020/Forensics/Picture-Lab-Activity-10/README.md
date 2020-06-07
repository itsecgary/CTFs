# Picture Lab: Activity 10
**Category:** Forensics

**Points:** 100

**Description:**
> Dear APCSA students,
>
> You thought you were done with Picture Lab.
>
> Unfortunately, you were wrong.
>
> We're sorry. We should not have pushed this challenge out, it was irresponsible for us to deploy a meme challenge in the middle of a very
> serious "Catch-The-Flag" competition. We originally wrote this challenge as a joke, hoping that it would poke fun at Collegeboard's APCSA
> "Picture Lab"; however, we now realize that this decision was insensitive and outright disrespectful to all those who have to solve the
> challenge. In the future, we promise that our challenges will not make you suffer as much as this trivial challenge does. We apologize in
> advance to all those who will suffer at the hands of this beginner-level challenge. I hope you are able to forgive us.
>
> Sincerely,
>
> AC/PMP/JC

## Writeup
The PDF doesn't give us much information besides the big hint that this file is
probably a PNG file, which helps. First thing I usually do with files that don't
have an extension is run the **file** command on linux or open it up in **HxD**.

Taking a look at the "mogodb" file in **HxD**, we see that
there isn't any appropriate header for any specific file format.

![Image of Hex](https://github.com/itsecgary/CTFs/blob/master/HSCTF2020/Forensics/Picture-Lab-Activity-10/hex.PNG)

Now, since we are assuming this is a PNG, we can put the appropriate file header
and footer:
```
00 00 00 00 0D 0A 1A 0A  ---->  89 50 4E 47 0D 0A 1A 0A    (........ -> ‰PNG....)
49 00 00 00 AE 42 60 82  ---->  49 45 4E 44 AE 42 60 82   (I...®B`‚ -> IEND®B`‚)
```


After this, I find **pngcheck** pretty useful. In the resources tab, I also
provided a link to the PNG wiki which shows which values are essential in the
PNG header.

Running **pngcheck** the first time gives me:
```
~/ctfs/hsctf2020/forensics$ pngcheck -v mogodb

File: mogodb (253237 bytes)
  invalid chunk name "" (00 48 00 52)
ERRORS DETECTED in mogodb
```

Nice. We can see that we have an invalid chunk. Back in **Hxd** we look for the
invalid chunk and we can see it on the first row (first 16 bytes).
```
00 48 00 52  ---->  49 48 44 52    (.H.R -> IHDR)
```

Running **pngcheck** again after changes gives us:
```
~/ctfs/hsctf2020/forensics$ pngcheck -v mogodb

File: mogodb (253237 bytes)
  chunk IHDR at offset 0x0000c, length 13
    560 x 708 image, 32-bit RGB+alpha, non-interlaced
  invalid chunk name "I" (49 00 41 00)
ERRORS DETECTED in mogodb
```

We can see we have yet another invalid chunk. Now looking back at **HxD** we
can find this invalid chunk in the third row (bytes 33-48).
```
49 00 41 00  ---->  49 44 41 54    (I.A. -> IDAT)
```

Once again, let's run **pngcheck**:
```
~/ctfs/hsctf2020/forensics$ pngcheck -v mogodb

File: mogodb (253237 bytes)
  chunk IHDR at offset 0x0000c, length 13
    560 x 708 image, 32-bit RGB+alpha, non-interlaced
  chunk IDAT at offset 0x00025, length 8192
    zlib: deflated, 32K window, fast compression
No errors detected in mogodb (33 chunks, 84.0% compression).
```

No errors detected! Nice! Now let's open the PNG up (don't forget to add the
.png extension).

![Image of Hex](https://github.com/itsecgary/CTFs/tree/master/HSCTF2020/Forensics/Picture-Lab-Activity-10/mogodb.png)

Seems to be some meme lol, but we get the flag here.

## Flag
flag{and_y0u_th0ught_p1ctur3_l4b_was_h4rd}

## Resources
- https://mh-nexus.de/en/hxd/

- https://en.wikipedia.org/wiki/Portable_Network_Graphics

- https://www.garykessler.net/library/file_sigs.html

- https://zoomadmin.com/HowToInstall/UbuntuPackage/pngcheck
