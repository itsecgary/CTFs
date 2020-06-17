# Broken Tokens
**Category:** Web

**Points:** 100

**Description:**
> I made a login page, is it really secure?
>
> https://broken-tokens.web.hsctf.com/
>
> **Note:** If you receive an "Internal Server Error" (HTTP Status Code 500),
that means that your cookie is incorrect.
>
> **Author:** hmmm
>
> **Given:** main.py

## Writeup
This website is not up anymore, but when clicked on, it takes me to a simple
login page. From looking at the website and *main.py* we can see that our goal
is to login as admin. No matter what we put into the username and password
field (besides the admin credentials), we will be granted access as *"guest"*.

I stared at this problem a long time, but found a program to help me out. I used
the JWT Tool linked below to mess with the JSON Web Token in a way to fool the
website into giving me access as admin.

With the tool, I entered the JWT given to me as guest, manipulated the username
field to be "admin", then changed the encryption type, which gave me a different
JWT. I copied and pasted it into the cookie for the JWT and it let me in and
gave me the flag (didn't write it down and can't get it again...rip).

## Resources
JWT Linux Tool: https://github.com/ticarpi/jwt_tool

JWT: https://jwt.io/
