// checkout.js - Checkout form handling

document.addEventListener('DOMContentLoaded', () => {
    const cart = getCart();
    
    // Redirect if cart is empty
    if(cart.length === 0) {
        window.location.href = '/cart/'; // adjust URL as needed
        return;
    }

    populateSummary(cart);
    
    // Inject cart JSON into hidden input for Django form submission
    document.getElementById('cartDataInput').value = JSON.stringify(cart);

    // Payment method UI toggle
    const paymentRadios = document.querySelectorAll('input[name="payment_method"]');
    paymentRadios.forEach(radio => {
        radio.addEventListener('change', (e) => {
            document.querySelectorAll('.payment-method-card').forEach(card => {
                card.style.borderColor = 'var(--mgr-gray-light)';
                card.querySelector('div').style.color = 'var(--mgr-gray-dark)';
            });
            const activeCard = e.target.closest('.payment-method-card');
            activeCard.style.borderColor = 'var(--mgr-red)';
            activeCard.querySelector('div').style.color = 'var(--mgr-red)';
        });
    });
});

function populateSummary(cart) {
    const listContainer = document.getElementById('checkoutItemsList');
    let subtotal = 0;

    cart.forEach(item => {
        const itemTotal = item.price * item.quantity;
        subtotal += itemTotal;
        
        listContainer.insertAdjacentHTML('beforeend', `
            <div style="display:flex; justify-content:space-between; margin-bottom:0.8rem; font-size:0.95rem;">
                <span>${item.quantity}x ${item.name}</span>
                <span style="font-weight:600;">₹${itemTotal.toFixed(2)}</span>
            </div>
        `);
    });

    let delivery = (subtotal > 0 && subtotal < 500) ? 40 : 0;
    let total = subtotal + delivery;

    document.getElementById('checkoutSubtotal').textContent = `₹${subtotal.toFixed(2)}`;
    document.getElementById('checkoutDelivery').textContent = delivery > 0 ? `₹${delivery.toFixed(2)}` : 'Free';
    document.getElementById('checkoutTotal').textContent = `₹${total.toFixed(2)}`;
}
