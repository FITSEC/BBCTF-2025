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
        })
        .catch((error) => {
            console.error('Error: ', error);
        });
}

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
