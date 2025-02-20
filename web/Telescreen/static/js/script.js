slogans = []

fetch('/get-slogans', {
        method: 'POST',
        headers: {
            'Content-Type': 'applications/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        slogans = data;
    })
    .catch((error) => {
        console.error('Error: ', error);
    });

let currentIndex = 0;
const textElement = document.getElementById('textOverlay');

function changeText() {
    textElement.textContent = slogans[currentIndex];
    currentIndex = (currentIndex + 1) % slogans.length;
}

setInterval(changeText, 1984); // Change text every 10 seconds

