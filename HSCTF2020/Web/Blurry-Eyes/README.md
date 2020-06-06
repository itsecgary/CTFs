# Blurry Eyes
**Category:** Web

**Points:** 100

**Description:**
> I can't see :(
>
> https://blurry-eyes.web.hsctf.com
>
> Author: meow

## Writeup
After clicking on the link, it takes us to a website with information on
CTFs. We see that it says that our flag is ... and is then blurred out. Best
think to do is to Right-Click and "View page source".

Looking at the HTML, we don't see anything useful besides the CSS class used
for the flag. Going to the CSS reveals many classes. With a quick CTRL-F ->
CTRL-C -> CTRL-V, we can find out class, which then gives us the flag.

## Flag
flag{glasses_are_useful}
