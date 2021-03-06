# Jarred1
**Category:** Forensics

**Points:** 200

**Description:**
> **Link:** https://drive.google.com/open?id=1g0j7rm53lU7ZRBM8XgkPkFpUgsfXpjfi
>
> **Files given:**

> **1.** System.map-5.3.0-18-generic
>
> **2.** module.dwarf
>
> **3.** lubuntu-Snapshot2.vmem

## Writeup
I didn't really know what to do with this at first because I was unfamiliar
with these types of files. After some research, I found that the System.map
and module.dwarf files are used to form a Linux profile. The other file is
a virual memory file which I think might be taken from a VM or just a linux
machine.

After more research, I figured I should clone **Volatility** code, which is how you
can load and analyze memory files.

1. In whichever directory, do a git clone on:
```
git clone https://github.com/volatilityfoundation/volatility.git
```

2. Package the System.map and module.dwarf files into a zip file
```
zip $(lsb_release -i -s)_$(uname -r)_profile.zip module.dwarf System.map-5.3.0-18-generic
```

3. Move the zip file to volatility/volatility/plugins/overlays/linux/

4. I got the profile name by running:
```
python vol.py --info | grep Linux
```
My profile name is LinuxUbuntu_4_4_0-17763-Microsoft_profilex64

5. You can figure out what you can get out of the memory by running:
```
python ./vol.py --info | grep -i linux_
```
We see that we can see the bash command history with linux_bash

6. The command to run is:
```
sudo python vol.py -f ../lubuntu-Snapshot2.vmem --profile=LinuxUbuntu_4_4_0-17763-Microsoft_profilex64 linux_bash
```

The output was:
```
Pid      Name                 Command Time                   Command
-------- -------------------- ------------------------------ -------
    1825 bash                 2019-11-13 03:59:04 UTC+0000   how do I linux?
    1825 bash                 2019-11-13 03:59:21 UTC+0000   UMDCTF-{falskdfklashdkjfhaskljfhakljsdhflkjasdhflkashdk}
    1825 bash                 2019-11-13 04:00:22 UTC+0000   echo -n "VU1EQ1RGLXtKYXJyZWRfU2gwdWxEX0hhVjNfTDBjazNkX0gxc19DT21wdTdlcn0=" | base64 -d | sha256sum
    1825 bash                 2019-11-13 04:01:32 UTC+0000   UMDCTF-{STRINgz_W0n't_Get_Th3_FLVG}
```

I obviously tried the last command as a flag, but it didn't work (shocker).
It looked like the 3rd command could be of use. I copied the command to my
terminal and ended up getting the flag: UMDCTF-{Jarred_Sh0ulD_HaV3_L0ck3d_H1s_COmpu7er}


## Flag
UMDCTF-{Jarred_Sh0ulD_HaV3_L0ck3d_H1s_COmpu7er}

## Resources
- https://www.linkedin.com/pulse/linux-memory-analysis-how-start-what-you-need-know-james-bower/

- https://github.com/volatilityfoundation/volatility/wiki/Linux

- https://resources.infosecinstitute.com/memory-forensics-and-analysis-using-volatility/#gref

- https://www.andreafortuna.org/2019/08/22/how-to-generate-a-volatility-profile-for-a-linux-system/
