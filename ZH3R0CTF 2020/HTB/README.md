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

This is all I found for these challenges. Flags 3, 6, 7, and 8 were all somewhere
on the host. https://github.com/sidchn/zh3r0CTF-writeup is another writeup that
kind of hits on Flags 3 and 6.


## Flags
Flag 1: zh3r0{pr05_d0_full_sc4n5}
Flag 2: zh3r0{You_know_your_shit}
Flag 4: zh3r0{y0ur_s4l4ry_wa5_cr3dit3d}
Flag 5: z3hr0{shouldve_added_some_filter_here}

## Resources
Nmap/Zenmap - https://nmap.org/download.html
