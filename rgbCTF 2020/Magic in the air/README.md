# PI 1: Magic in the air
**Category:** Forensics/OSINT

**Points:** 470

**Description:**
> We are investigating an individual we believe is connected to a group smuggling
drugs into the country and selling them on social media. You have been posted on
a stake out in the apartment above theirs and with the help of space-age
eavesdropping technology have managed to extract some data from their computer.
What is the phone number of the suspect's criminal contact?
>
> flag format includes country code so it should be in the format: rgbCTF{+00000000000}
>
> ~Klanec#3100
>
> **Given:** magic_in_the_air.7z

## Writeup
Unzipping the file gives us "data" which seems to be a bunch of gunk when looking
at the contents. Here's what kind of file it is:
```
$ file data
data: BTSnoop version 1,
```

I did not know what a BTSnoop file was and what it meant before completing this
challenge, so I learned A LOT from this challenge. I eventually figured out that
BTSnoop is Bluetooth traffic from a device. We can open this bad boy in **Wireshark**.

For a long time I couldn't quite figure out what kind of information we are provided
in this BTSnoop capture. After taking a close look at some of the sources, we see
a device name **G613**. I looked up the device on Google and we see that this data
is from a *Logitech Mechanical Gaming Keyboard*. This must be keystrokes then.

After quite a long time, I came across a PDF for Human Interface Devices (HIDs).
The bottom of the PDF contains the HID values for common keystrokes. **BINGO**
https://cdn.sparkfun.com/datasheets/Wireless/Bluetooth/RN-HID-User-Guide-v1.0r.pdf

I started to manually convert the values straight from the BTSnoop capture in
**Wireshark**, but I realized how many I had to convert and how long it would take
me. Therefore, I highlighted the packets I wanted to convert, exported them as a CSV
file, edited the CSV to be easier to work with in a script, and ran it through my
script to decode.

**Script:**
```

```

**Output:**
```

```



## Flag
rgbCTF{}

## Resources
[Wireshark](https://www.wireshark.org/download.html)

[HID PDF](https://cdn.sparkfun.com/datasheets/Wireless/Bluetooth/RN-HID-User-Guide-v1.0r.pdf)

[Generic ATT Info](https://www.oreilly.com/library/view/getting-started-with/9781491900550/ch04.html)
