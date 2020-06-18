# Sensitive
**Category:** Forensics

**Points:** 150

**Description:**
> **Author:** Lumpus
>
> **Hint:** "Not sure what to make of this..."
>
> **Given:** File named "sensitive"

## Writeup
The file didn't have any extension added to the end so I couldn't
tell the type of file, so I ran the "file" command on Linux. It told
me it was a data file, which doesn't give much help.

I opened the file in **HxD** (a hex editor) and noticed that it was a PDF via
the header and footer.

PDF Header:
```
25 50 44 46 (in hex) = %PDF (in ASCII)
```

PDF Footer:
```
0A 25 25 45 4F 46 (.%%EOF)
0A 25 25 45 4F 46 0A (.%%EOF.)
0D 0A 25 25 45 4F 46 0D 0A (..%%EOF..)
0D 25 25 45 4F 46 0D (.%%EOF.)
```

After some analysis, I realized there was an extra "20" hex value for every
other character, which was probably the reason the file was corrupted. I tried
to find simple commands to do something like remove every other character, but
gave up on that.

I ended up writing a simple python program which did that for me and created
a new file. See script below:

This opened up a PDF with the UMD CSEC logo and a QR code that was VERY transparent.
All it took was a little messing around with the contrast and brightness and my QR
reader picked it up.

## Flag
UMDCTF-{l0v3-me_s0meh3x}

## Resources
- https://www.guru99.com/reading-and-writing-files-in-python.html

- https://mh-nexus.de/en/hxd/
