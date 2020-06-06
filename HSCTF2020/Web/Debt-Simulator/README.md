# Debt Simulator
**Category:** Web

**Points:** 100

**Description:**
> https://debt-simulator.web.hsctf.com/
>
> Author: Madeleine

## Writeup
Clicking on the link provided takes us to a website that is literally a Debt
Simulator. Playing around with it a little doesn't hurt, but only showed that
debt sure can be a pain in the ass.

I clicked on Inspect Element and read through the source a little. Towards the
bottom there is a fetch call:
```
fetch("https://debt-simulator-login-backend.web.hsctf.com/yolo_0000000000001", {
    method: "POST",
    body: "function=" + (e ? "getCost" : "getPay"),
    headers: {
        "Content-type": "application/x-www-form-urlencoded"
    }
})
```

I clicked on the link and it fave me:
```
{"functions":["getPay","getCost","getgetgetgetgetgetgetgetgetFlag"]}
```

In the fetch code above, we can see that the post method is called with
Content-Type = "application/x-www-form-urlencoded" and body with format
"function=<function>".

I used **Postman** for this challenge (**Burp Suite** would work as well), which I find
super useful and easy to use for Web challenges like these. To see what would
happen, I did a POST request to the backend (yolo) website above entering in
"function=getPay" and changing the Content-Type. Boom. We got a number.

From that website above, the obvious route to go is to make the function call
equal to "function=getgetgetgetgetgetgetgetgetFlag" to receive the flag.

## Flag
flag{y0u_f0uND_m3333333_123123123555554322221}

## Resources

**Postman:**   https://www.postman.com/

**Burp Suite:**   https://portswigger.net/burp

You can install the basic community edition for free because otherwise it is
pricey!
