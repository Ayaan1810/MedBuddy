document.addEventListener("DOMContentLoaded", function () {
    // Form validation for signup (if applicable)
    const signupForm = document.querySelector("form");
    if (signupForm) {
        signupForm.addEventListener("submit", function (event) {
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

    // Helper function to validate email
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Load clicked cards from localStorage or initialize an empty array
    let clickedCards = JSON.parse(localStorage.getItem('clickedCards')) || [];

    // Apply the 'taken' class to previously clicked cards on page load
    document.querySelectorAll('.card').forEach(card => {
        const cardId = card.getAttribute('data-id');

        // If the cardId exists in clickedCards, apply the 'taken' class
        if (clickedCards.includes(cardId)) {
            card.classList.add('taken');
        }

        // Add click event listener to each card
        card.addEventListener('click', function () {
            card.classList.toggle('taken');  // Toggle 'taken' class
            const cardId = card.getAttribute('data-id');

            if (card.classList.contains('taken')) {
                // If the card is marked as 'taken', add its ID to clickedCards
                if (!clickedCards.includes(cardId)) {
                    clickedCards.push(cardId);
                }
            } else {
                // If 'taken' class is removed, remove the cardId from clickedCards
                clickedCards = clickedCards.filter(id => id !== cardId);
            }

            // Update localStorage with the updated clickedCards array
            localStorage.setItem('clickedCards', JSON.stringify(clickedCards));
        });
    });
});
