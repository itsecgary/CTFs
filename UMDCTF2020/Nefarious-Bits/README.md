# Nefarious Bits
**Category:** Forensics

**Points:** Can't remember

**Description:**
> **Author:** t0pc4r
>
> **Hint:** "After being exposed to some solar radiation, it looks like
>	   some bits have turned bad. It is your job to figure out
>	   what they are trying to say."
>
> **Note:** "Do not attempt to communicate with or contact any of
>       the IP addresses mentioned in the challenge. The challenge
>	      can and should be solved statically."
>
> **Given:** Pcap file "attack.pcap"

## Writeup
When I opened the pcap file, there wasn't much to look at. Pretty much
just TCP transmissions from ONE source to ONE destination.

I noticed that a few fields were changing throughout the 200-something
packets in the file. The source port went up by one every time, the
TCP checksum changes by a constant little bit every time, and one of the
IPv4 flags were changing randomly.

With this knowledge, I didn't think I could do anything with the first two
fields I saw changing. It would make sense that the checksum was changed
by the source port changing every packet. I took a closer look at the IPv4
flag changing every time and saw it was called the "Reserved bit"

After some research, I found at that the **reserved bit** is used to indicate
whether a packet has been sent with malicious intent or not (1 or 0). With
this in mind, the fact that it was varying like binary data would vary, and
the hint, I assumed that the 200-something packets were using this field for
binary data.

I exported the pcap file to a CSV and removed all of the columns except for
the field I wanted. I named it "test.csv" for the script. My script printed
out the binary for this pcap. See script "nefarious.py"

## Flag
UMDCTF-{3vil_b1ts_@r3_4lw4ys_3vi1}

## Resources
https://en.wikipedia.org/wiki/Evil_bit
