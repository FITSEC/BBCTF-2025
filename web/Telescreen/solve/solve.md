# Solve
So, our goal is to get more than 1000000 credits to win our flag on the
party member page. We've only got a 100, and the rations we can buy,
besides being atrocious, will make the few credits you do have disappear
before you could even satiate your midday munchies (though the rubber
might go some ways). If you play with the buttons, you'll find you can
go infintely up, but not below one. Checking out the JS at `/static/js`,
we find the code that enforces this:

```js
document.querySelectorAll(".product").forEach(product => {
    const minusBtn = product.querySelector(".minus");
    const plusBtn = product.querySelector(".plus");
    const quantitySpan = product.querySelector(".quantity");
    const buyBtn = product.querySelector(".buy-btn")

    minusBtn.addEventListener("click", () => {
        let quantity = parseInt(quantitySpan.textContent);
        if (quantity > 1) {
            quantitySpan.textContent = quantity - 1;
        }
    });

    plusBtn.addEventListener("click", () => {
        let quantity = parseInt(quantitySpan.textContent);
        quantitySpan.textContent = quantity + 1;
    });

    buyBtn.addEventListener("click", () => {
        let name = product.querySelector(".name").textContent;
        let quantity = parseInt(quantitySpan.textContent);
        if (quantity > 0) {
            buy_ration(name, quantity);
        }
    });
});
```

So basically, can't go below 1 with the minus button for each ration,
and even if you went into the HTML to made the number negative, the
buy button wouldn't call the `buy_ration` function. But why would we
want to make the quantity negative? Well, let's take a quick look at
the buy ration function:
```js
function buy_ration(name, quantity) {
    ration = {name: name, quantity: quantity}
    fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(ration),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            num = document.getElementById("credit-num");
            num.textContent = data["creds"];
            message = document.getElementById("message");
            message.textContent = data["message"];
        })
        .catch((error) => {
            console.error('Error: ', error);
        });
}
```
We send the name of our product and the quantity that we want, but no
values are taken from our browser. Then, we get our new amount of creds
back. This means a few things:
1. The value of credits is NOT client side, so we can't cheese it by changing it our our end :(
2. The product values are also server side, likely looked up by the "name" field
3. After getting the product value, it likely computes our price by subtracting it from our creds, returning our new cred value to us.
Okay, cool. Too bad the pesky javascript checks for negative values,
because if it was negative, price * quantity could actually give us
credits! But wait a minute, the javascript in *our browser* checks it,
i.e.-the code that checks it is running on *our machine*. What if we
could just skip that check? Well good news is you can! Pop open the
console in your browser's dev tools and run
```js
buy_ration("<ration_name>", <negative_quantity>)
```
and you can be as rich as you want to be! If you buy enough gruel
at the low low price of -10000 (or any other good combo of items), then
you could be rolling in a feast and a flag at the party member page!
