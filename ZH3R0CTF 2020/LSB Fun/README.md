# LSB Fun
**Category:** Forensics

**Points:** 230

**Description:**
> have you ever heard of LSB :) ?
>
> **Author:** h4x5p4c3
>
> **Given:** chall.jpg

## Writeup
For those who don't know, LSB (Least Significant Bit) is the process of encoding
data in images such as PNGs, JPG/JPEGs, BMPs, and more. I will provide links
down below that explain LSB more if you haven't quite grasped it.

To sum it all up, LSB is taking the pixels of the image and setting the last bit
of either the Red, Green, or Blue values to 1. This will either change one of
the color values of pixels in the image by 1 or by nothing at all. This ultimately
doesn't change the image in the slightest. You could encode the message in the
image and the image would look the same as it did before.  

For JPEG LSB encoding, **jsteg** is a nice tool that will reveal the hidden
information.

**Requirement:** go (takes a little to install)
```
sudo apt install golang-go
```

**Install Jsteg**
```
go get lukechampine.com/jsteg
```

Running this on our image just straight up gives us our flag. How neat!
```
$ jsteg reveal chall.jpg
zh3r0{j5t3g_i5_c00l}
```

## Flag
zh3r0{j5t3g_i5_c00l}

## Resources
[jsteg](https://github.com/lukechampine/jsteg)

[LSB stego](https://itnext.io/steganography-101-lsb-introduction-with-python-4c4803e08041)

[Encodings](https://alchitry.com/blogs/tutorials/encodings)
