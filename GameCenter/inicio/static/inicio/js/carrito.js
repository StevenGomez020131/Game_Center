document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', () => {
        const productId = button.getAttribute('data-id');
        const productType = button.getAttribute('data-type');
        
        fetch('/add-to-cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({ 'product_id': productId, 'product_type': productType })
        }).then(response => response.json())
          .then(data => {
              if (data.status === 'success') {
                  alert('Producto añadido al carrito');
              } else {
                  alert('Error: ' + data.message);
              }
          });
    });
});