# HTB
**Category:** Hack The Box

**Number of flags:** 8 total

**Description:**
> Description: Here's the url ;)
>
>   hackit.zh3r0.ml
>
> **Author :** Mr.Holmes


## Writeup
This was a pretty unique challenge set for a CTF competition. Despite the fact
most players get a lot of practice from the HackTheBox website and their
challenges, we don't see too many of them for a CTF.

For those who know, **Nmap** is practically the first tool that comes to mind when
*only* given a host. You can find links in the *Resources* section below. Kali
has this loaded already, but for linux, it's a quick install. I also realized that it
isn't possible on Windows Subsystem for Linux :( #rip

I personally used Zenmap for Windows because it is what I had at the time. here
is the command I ran:
```
nmap -sC -sV -p- hackit.zh3r0.ml
```

**Output:**
```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-18 09:25 Eastern Daylight Time
Nmap scan report for 139.59.3.42
Host is up (0.27s latency).
Not shown: 65530 closed ports
PORT      STATE    SERVICE  VERSION
22/tcp    open     http     PHP cli server 5.5 or later
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)

99/tcp    open     ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 70:78:8f:70:79:59:72:5f:05:c9:2a:63:b4:34:c1:52 (RSA)
|   256 08:6d:42:16:2a:47:ae:b4:d7:fa:35:28:91:67:ab:63 (ECDSA)
|_  256 e4:89:6b:09:37:64:c2:47:01:bd:c2:32:d8:cd:06:2d (ED25519)

324/tcp   open     ftp      vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 ftp      ftp            22 Jun 18 09:06 test.txt
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:173.120.119.45
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status

4994/tcp  open     unknown
| fingerprint-strings:
|   GenericLines, GetRequest, HTTPOptions:
|     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|     ||Employee Entry||
|     ----------------------------------------------------------
|     Sherlock Holmes Inc.
|     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|     Here's a free flag for you, just for finding this door! Flag 1: zh3r0{pr05_d0_full_sc4n5}
|     Heyo, Watcha looking at? Employee ID yoo! :
|     away kiddo, huh, Kids these days!
|   NULL:
|     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|     ||Employee Entry||
|     ----------------------------------------------------------
|     Sherlock Holmes Inc.
|     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|     Here's a free flag for you, just for finding this door! Flag 1: zh3r0{pr05_d0_full_sc4n5}
|_    Heyo, Watcha looking at? Employee ID yoo! :

11211/tcp filtered memcache
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port4994-TCP:V=7.80%I=7%D=6/18%Time=5EEB6FE7%P=i686-pc-windows-windows%
SF:r(NULL,18C,"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SF:~\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\|\|Employee\x20Entry\|\|\n\n--------------------------
SF:--------------------------------\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20Sherlock\x20Holmes\x20In
SF:c\.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nHere's
SF:\x20a\x20free\x20flag\x20for\x20you,\x20just\x20for\x20finding\x20this\
SF:x20door!\x20Flag\x201:\x20zh3r0{pr05_d0_full_sc4n5}\nHeyo,\x20Watcha\x2
SF:0looking\x20at\?\x20Employee\x20ID\x20yoo!\x20:\x20\n")%r(GenericLines,
SF:1B1,"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:0\x20\x20\|\|Employee\x20Entry\|\|\n\n---------------------------------
SF:-------------------------\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20Sherlock\x20Holmes\x20Inc\.\n~~
SF:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nHere's\x20a\x
SF:20free\x20flag\x20for\x20you,\x20just\x20for\x20finding\x20this\x20door
SF:!\x20Flag\x201:\x20zh3r0{pr05_d0_full_sc4n5}\nHeyo,\x20Watcha\x20lookin
SF:g\x20at\?\x20Employee\x20ID\x20yoo!\x20:\x20\nGo\x20away\x20kiddo,\x20h
SF:uh,\x20Kids\x20these\x20days!\n")%r(GetRequest,1B1,"\n~~~~~~~~~~~~~~~~~
SF:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\|\|Employee\x2
SF:0Entry\|\|\n\n---------------------------------------------------------
SF:-\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20Sherlock\x20Holmes\x20Inc\.\n~~~~~~~~~~~~~~~~~~~~~~~~~~
SF:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nHere's\x20a\x20free\x20flag\x20for\x2
SF:0you,\x20just\x20for\x20finding\x20this\x20door!\x20Flag\x201:\x20zh3r0
SF:{pr05_d0_full_sc4n5}\nHeyo,\x20Watcha\x20looking\x20at\?\x20Employee\x2
SF:0ID\x20yoo!\x20:\x20\nGo\x20away\x20kiddo,\x20huh,\x20Kids\x20these\x20
SF:days!\n")%r(HTTPOptions,1B1,"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SF:~~~~~~~~~~~~~~~~~~\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\|\|Employee\x20Entry\|\|\n\n---------
SF:-------------------------------------------------\n\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20Sherloc
SF:k\x20Holmes\x20Inc\.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SF:~~~~~~~~~\nHere's\x20a\x20free\x20flag\x20for\x20you,\x20just\x20for\x2
SF:0finding\x20this\x20door!\x20Flag\x201:\x20zh3r0{pr05_d0_full_sc4n5}\nH
SF:eyo,\x20Watcha\x20looking\x20at\?\x20Employee\x20ID\x20yoo!\x20:\x20\nG
SF:o\x20away\x20kiddo,\x20huh,\x20Kids\x20these\x20days!\n");
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1391.93 seconds
```

We see a lot of information here. Where to start!

Let's start with port **22**. The information given to us in the output suggests that
there is a website standing on this port, which is odd considering **22** is
reserved for SSH.

I went ahead and ran a curl on the website on port 22:
```
$ curl hackit.zh3r0.ml:22
z3hr0{shouldve_added_some_filter_here}
```

Sweet. First flag!

Let's now take a look at port **324**. The information from our output shows us
that FTP is running at this port. This is not usual as well because FTP's default
and reserved protocol is *21*. We also notice that "Anonymous login" is enabled
for FTP, which means we can login as **anonymous** with an empty password and
poke around.
```
$ ftp hackit.zh3r0.ml 324
Connected to hackit.zh3r0.ml.
220 (vsFTPd 3.0.3)
Name (hackit.zh3r0.ml:itsecgary): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> _
```

Now we are logged in. Typing *help* is a good way to see what commands we can run.
```
ftp> help
Commands may be abbreviated.  Commands are:

!               dir             mdelete         qc              site
$               disconnect      mdir            sendport        size
account         exit            mget            put             status
append          form            mkdir           pwd             struct
ascii           get             mls             quit            system
bell            glob            mode            quote           sunique
binary          hash            modtime         recv            tenex
bye             help            mput            reget           tick
case            idle            newer           rstatus         trace
cd              image           nmap            rhelp           type
cdup            ipany           nlist           rename          user
chmod           ipv4            ntrans          reset           umask
close           ipv6            open            restart         verbose
cr              lcd             prompt          rmdir           ?
delete          ls              passive         runique
debug           macdef          proxy           send
ftp> _
```

Nice. Let's try some:
```
ftp> dir
500 Illegal PORT command.
425 Use PORT or PASV first.
ftp> ls
500 Illegal PORT command.
ftp> _
```

Looks like an illegal command. After doing some research, I learned that being in
passive passes these commands through.
```
ftp> ls -la
227 Entering Passive Mode (139,59,3,42,143,73).
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Jun 18 09:06 .
drwxr-xr-x    3 ftp      ftp          4096 Jun 18 09:06 ..
drwxr-xr-x    3 ftp      ftp          4096 Jun 18 09:06 ...
-rw-r--r--    1 ftp      ftp            22 Jun 18 09:06 test.txt
226 Directory send OK.
ftp> cd ...
250 Directory successfully changed.
ftp> ls -la
227 Entering Passive Mode (139,59,3,42,159,1).
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Jun 18 09:06 .
drwxr-xr-x    3 ftp      ftp          4096 Jun 18 09:06 ..
drwxr-xr-x    2 ftp      ftp          4096 Jun 18 09:06 ...
-rw-r--r--    1 ftp      ftp            46 Jun 18 09:06 .stayhidden
-rw-r--r--    1 ftp      ftp            22 Jun 18 09:06 test.txt
226 Directory send OK.
ftp> cd ...
250 Directory successfully changed.
ftp> ls -la
227 Entering Passive Mode (139,59,3,42,233,178).
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Jun 18 09:06 .
drwxr-xr-x    3 ftp      ftp          4096 Jun 18 09:06 ..
-rw-r--r--    1 ftp      ftp            34 Jun 18 09:06 .flag
-rw-r--r--    1 ftp      ftp            22 Jun 18 09:06 test.txt
226 Directory send OK.
ftp>
```

Looks like we have a couple files!! **..** is for the directory before and **.**
is for the current directory. They tried to be sneaky with the **...** directory.
We can retrieve these files using ` get <file> <new_file_name> `, which tranfers
these files to our machine (hence File Transfer Protocol). I grabbed each of the
*test.txt* files and renamed them as test1, test2, and test3 in case they were
different content-wise.

Let's see what we are working with:
```
$ ls -la
total 0
drwxrwxrwx 1 gary gary 512 Jun 18 09:09 .
drwxrwxrwx 1 gary gary 512 Jun 18 09:09 ..
-rw-rw-rw- 1 gary gary  34 Jun 18 09:05 .flag
-rw-rw-rw- 1 gary gary  46 Jun 18 09:08 .stayhidden
-rw-rw-rw- 1 gary gary  22 Jun 18 09:06 test1
-rw-rw-rw- 1 gary gary  22 Jun 18 09:07 test2
-rw-rw-rw- 1 gary gary  22 Jun 18 09:09 test3

$ cat .flag
Flag 2: zh3r0{You_know_your_shit}

$ cat .stayhidden
Employee ID: 6890d90d349e3757013b02e495b1a87f

$ cat test1
LOL Nothing here. ;-;

$ cat test2
LOL Nothing here. ;-;

$ cat test3
LOL Nothing here. ;-;
```

Welp we got another flag. *Note:* While writing this writeup, I didn't realize
there was another **...** directory in the first **...** directory so I only
extracted the first two *test.txt* files and the *.stayhidden* file so #rip me
for missing out on 419 points lol. We also retrieved an *Employee ID* which may
be useful later!

Let's take a look at the open port on **4994**

```
$ nc hackit.zh3r0.ml 4994

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     ||Employee Entry||

----------------------------------------------------------
                     Sherlock Holmes Inc.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Here's a free flag for you, just for finding this door! Flag 1: zh3r0{pr05_d0_full_sc4n5}
Heyo, Watcha looking at? Employee ID yoo! :
6890d90d349e3757013b02e495b1a87f
Hey I know you! You work here!
Books are a uniquely portable magic. - Stephen King

Flag 4: zh3r0{y0ur_s4l4ry_wa5_cr3dit3d}
```

Looks like they gave us a flag right away. We also got a prompt for the Employee
ID, which is what we found above. After entering it in, we get Flag 4!

This is all I found for these challenges. Flags **3**, **6**, **7**, and **8**
were all somewhere on the host. https://github.com/sidchn/zh3r0CTF-writeup is
another writeup that kind of hits on Flags **3** and **6**.


## Flags
**Flag 1:** zh3r0{pr05_d0_full_sc4n5}

**Flag 2:** zh3r0{You_know_your_shit}

**Flag 4:** zh3r0{y0ur_s4l4ry_wa5_cr3dit3d}

**Flag 5:** z3hr0{shouldve_added_some_filter_here}

## Resources
Nmap/Zenmap - https://nmap.org/download.html
