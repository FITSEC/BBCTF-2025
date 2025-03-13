# Solution(s)
## Part 1
I'll keep this one short and simple. When confronted with a simple web
challenge, a good first step is always to check out the HTML source.
If you look at it, you'll find a comment. DO NOT IGNORE COMMENTS IN
WEB CHALLENGES, often times (not all the time, mind you), they are
meant to give you pointers or even the flag itself. It tells you about
this page called `proles.txt`, if we visit that, we get:
```
OBEDIENT PROLES WILL NOT GO TO '/government-secrets' EVER
```
I'm no prole, nor am I very obedient, so upon visiting
`government-secrets.txt`, we find:
```
Flag 1: bbctf{n0t_s0_s3cr37_is_i7?} All pigeons are government drones. The battery runs low, so they “charge” on power lines. The moon is just a giant lightbulb. NASA changes it every...
```
Congrats! You are now the proud owner of an easy web flag and in on
the Oceanian government's other worst-kept secrets. Have fun reading!

## Part 2
Another sweet and simple writeup, this one asks you to poke at the same
page as Part 1. When approaching a simple web challenge, it's worth
looking through the dev tools for things that might help us solve it.
Cookies are one of those things you always want to check for. If you
don't know what a cookie is, check out [this](https://usa.kaspersky.com/resource-center/definitions/cookies?srsltid=AfmBOoqDZl__4fkTltuFh7WLQ3hFnakY426YCO4tyS91FDykIRSv2-AJ) helpful article :). tl;dr, they store data
on your browser, like who you are, which *could* be used to show you
a different web page or another (think about signing in to a site, how
you're looking at the same pages, just different, user-specific info).
Also, since it's stored in *our* browser, we can change it. Good web
sites encrypt cookies to prevent modification, bad ones, like this one
don't. Crack open dev tools in your browser, go to storage, go to
cookies, and you'll see a cookie called `isBigBrother` set equal to
`False`. I'd like the site to think I'm good ol' BB, so let's make it
`True`, and voila! The announcements then include the flag!
