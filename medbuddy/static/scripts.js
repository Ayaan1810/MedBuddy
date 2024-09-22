document.addEventListener("DOMContentLoaded", function() {
    const signupForm = document.querySelector("form");
    if (signupForm) {
        signupForm.addEventListener("submit", function(event) {
            const email = signupForm.querySelector("input[name='email']").value;
            const password = signupForm.querySelector("input[name='password']").value;

            if (!validateEmail(email)) {
                alert("Please enter a valid email address.");
                event.preventDefault();
            }

            if (!password) {
                alert("Password cannot be empty.");
                event.preventDefault();
            }
        });
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }
});

// Card click functionality
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    const clickedCards = JSON.parse(localStorage.getItem('clickedCards')) || [];

    // On page load, apply the 'taken' class to previously clicked cards
    clickedCards.forEach(cardId => {
        const card = document.querySelector(`.card[data-id="${cardId}"]`);
        if (card) {
            card.classList.add('taken');
        }
    });

    // Add click event listeners to each card
    cards.forEach(card => {
        card.addEventListener('click', () => {
            const cardId = card.getAttribute('data-id');

            card.classList.toggle('taken');
            if (card.classList.contains('taken')) {
                // Add cardId to clickedCards if it is now 'taken'
                clickedCards.push(cardId);
            } else {
                // Remove cardId from clickedCards if the 'taken' class is removed
                const index = clickedCards.indexOf(cardId);
                if (index > -1) {
                    clickedCards.splice(index, 1);
                }
            }

            // Update localStorage with the new clickedCards array
            localStorage.setItem('clickedCards', JSON.stringify(clickedCards));
        });
    });
});
