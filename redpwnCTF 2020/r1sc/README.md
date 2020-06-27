# r1sc
**Category:** Rev

**Points:** 487

**Description:**
> Look, Mum, no opcodes!
>
> **Author:** imyxh
>
> **Given:** r1sc

## Writeup
First thing I do here is run the program. Nothing much besides one input.
```
$ ./r1sc
Enter access code: test
Access denied.
```

Next thing I did was open this sucker up in Ghidra to see what we are working
with. I couldn't understand fully what this program was doing cause im a n00b, but
it seems like based off the input, its either access denied, or something else.
From our one trial run above, I'm sure we want the other route.
```
undefined  [16] entry(undefined8 param_1) {
  char *pcVar1;

  FUN_00101068(param_1,&DAT_00103001);
  syscall();
  FUN_0010107e(0,0,0x30);
  if (ram0x00103038 == 0) {
    pcVar1 = &DAT_00103015;
    FUN_00101068();
  }
  else {
    pcVar1 = s_Access_denied._00103029;
    FUN_00101068();
  }
  syscall();
  syscall();
  return CONCAT88((ulong)(byte)pcVar1[-1],1);
}
```

I found this cool tool that I guess I've been missing out on called **angr**. To
my understanding, this is basically a brute-forcer for binaries. Maybe that's not
*exactly* the purpose of it, butttttt that's sure as hell what we are going to
use it for.

The code is pretty simple for **angr**. After importing the necessary modules,
all you really have to do is pick the spot(s) where you want the program to hit
during execution (like printing the flag) and pick the spot(s) where you want the
program to avoid. In our case, we want to avoid the access denied **(0x0040103b)**.

I inspected the program in Ghidra to find an address I want it to run so that I
could, you know, get the flag. I picked the point where the if statement is passed
and not into the else where the access denied part is **(0x00401050)**.

Here is the script I created for **angr**. I will also provide resources and videos
on **angr** if someone needs them.
```
import angr
import logging

#logging.getLogger('angr').setLevel(logging.INFO)

p = angr.Project("r1sc")
good = 0x00401050
bad = 0x0040103b
#length = 72

st = p.factory.entry_state()
sm = p.factory.simulation_manager()
print(sm.explore(find=good, avoid=bad))

for f in sm.found:
    print(f.posix.dumps(0))
    print(f.posix.dumps(1))
```

**Output:**
```
$ python3 angry.py
WARNING | 2020-06-26 21:14:39,371 | cle.backends.elf.elf | Segment PT_LOAD is empty at 0x002000!
WARNING | 2020-06-26 21:14:39,372 | cle.loader | The main binary is a position-independent executable. It is being loaded with a base address of 0x400000.
<SimulationManager with 5454 active, 1 found, 6 avoid>
b'flag{actually_3_instructions:_subleq,_ret,_int3}'
b'Enter access code: '
```

https://www.youtube.com/watch?v=kzoeRIf4hVs

## Flag
flag{actually_3_instructions:_subleq,_ret,_int3}

## Resources
[Video using angr](https://www.youtube.com/watch?v=9dQFM5O4KFk&list=PL-nPhof8EyrGKytps3g582KNiJyIAOtBG)

[Lecture on angr](https://www.youtube.com/watch?v=XgHZ6QnZkgc)

[Lots of examples from past CTFs](https://docs.angr.io/examples)

[angr documentation](https://github.com/angr/angr)
