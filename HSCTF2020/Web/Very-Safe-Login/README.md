# Very Safe Login
**Category:** Web

**Points:** 100

**Description:**
> Bet you can't log in.

> https://very-safe-login.web.hsctf.com/very-safe-login

> Author: Madeleine

## Writeup
Clicking on the link provided brings us to a website with only a login page.
It doesn't hurt to try a few simple username and password combinations to test
the functionality. Nothing here, so we should view the source code to see what
is going on.

We see an embedded script in the bottom of the HTML source:

```
var login = document.login;

function submit() {
    const username = login.username.value;
    const password = login.password.value;

    if(username === "jiminy_cricket" && password === "mushu500") {
        showFlag();
        return false;
    }
    return false;
}
```

Looks like it gives us the password to login. How nice of them! Inserting the
credentials and logging in gives us the flag.

## Flag
flag{cl13nt_51de_5uck5_135313531}
