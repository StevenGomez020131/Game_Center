document.querySelectorAll('.change-quantity').forEach(button => {
    button.addEventListener('click', () => {
        const productId = button.getAttribute('data-id');
        const action = button.getAttribute('data-action');

        // Implement AJAX request to update quantity in the session and update the cart
    });
});

document.querySelectorAll('.remove-item').forEach(button => {
    button.addEventListener('click', () => {
        const productId = button.getAttribute('data-id');
        
        // Implement AJAX request to remove item from the cart and update the cart
    });
});