# uglybash
**Category:** Misc

**Points:** 359

**Description:**
> This bash script evaluates to echo dont just run it, dummy # flag{...} where the flag is in the comments.
>
> The comment won't be visible if you just execute the script. How can you mess with bash to get the value right before it executes?
>
> Enjoy the intro misc chal.
>
> **Author:** arinerron
>
> **Given:** cmd.sh

## Writeup
When looking at the file, we see a bunch of gibberish bash. I did some research
and found a way to "debug" a script in bash.

The command is simple:
```
bash -x <program>
```

After running this, we see all commands ran in bash. We can do some parsing
through this debug output and retrieve:
```
+++ printf %s e
+++ printf %s c
+++ printf %s h
+++ printf %s o
+++ printf %s ' '
+++ printf %s d
+++ printf %s o
+++ printf %s n
+++ printf %s t
+++ printf %s ' '
+++ printf %s j
+++ printf %s u
+++ printf %s s
+++ printf %s t
+++ printf %s ' '
+++ printf %s r
+++ printf %s u
+++ printf %s n
+++ printf %s ' '
+++ printf %s i
+++ printf %s t
+++ printf %s ,
+++ printf %s ' '
+++ printf %s d
+++ printf %s u
+++ printf %s m
+++ printf %s m
+++ printf %s y
+++ printf %s ' '
+++ printf %s #
+++ printf %s ' '
+++ printf %s f
+++ printf %s l
+++ printf %s a
+++ printf %s g
+++ printf %s {
+++ printf %s u
+++ printf %s s
+++ printf %s 3
+++ printf %s _
+++ printf %s z
+++ printf %s s
+++ printf %s h
+++ printf %s ,
+++ printf %s _
+++ printf %s d
+++ printf %s u
+++ printf %s m
+++ printf %s m
+++ printf %s y
+++ printf %s }
```

Evaluating to:
```
dont just run it, dummy # flag{us3_zsh,_dummy}
```

## Flag
flag{us3_zsh,_dummy}
