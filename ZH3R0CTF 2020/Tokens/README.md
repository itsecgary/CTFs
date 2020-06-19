# Tokens
**Category:** Web

**Points:** 50

**Description:**
>The flag was sent by Mr.4N0NYM4U5 to my victim. But i dont have the username
and password of the victim to login into the discord account. The only thing i
have is a god damn token. Can you help me to get the flag. Ill give you the
token and it is all you need.
>
> **Token:** NzIyMzM1MTQ5NDA0MTkyODIw.XunLaw.xASADEeu9iXsYf1wqTFOil_jgfo
>
> **Author:** Mr.4N0NYM4U5

## Writeup
We weren't able to solve this challenge for a while due to the pure confusion of
what was given to us. Originally, we saw this as a JWT token, when put into
https://jwt.io, it wasn't giving anything useful.

After some thinking, we thought: "Wait...are we able to login to Discord using a
token?" Sure enough, we were on the right track. I found a video that shows the
process and even gives us the JavaScript code.

Basically, all we need to do is copy and paste the JS Code into the console in
Google Developer Tools and call the function with the token.
```
function login(token) {
    setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);
    setTimeout(() => {location.reload();}, 2500);
}
```
```
> login('NzIyMzM1MTQ5NDA0MTkyODIw.XunLaw.xASADEeu9iXsYf1wqTFOil_jgfo')
```

After this, I had to refresh the page and click on *Open* in the top right
corner of https://discord.com. This broght me to the page and we can see that
our name has the flag in it. Not only that, but my favorite doctor/teacher/astronaut/physicist/hacker
was the profile picture!

[PNG of discord chat](https://github.com/itsecgary/CTFs/tree/master/ZH3R0CTF%202020/Tokens/screenshot.png)

## Flag
zh3r0{1et_7he_F0rce_8e_With_YoU}

## Resources
Video - https://www.youtube.com/watch?v=FmXMGCRpw50

JS Code - https://pastebin.com/yPWZGzGB
