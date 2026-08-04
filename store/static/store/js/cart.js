// cart.js - Cart page functionality

document.addEventListener('DOMContentLoaded', () => {
    renderCart();
});

function renderCart() {
    const cart = getCart();
    const listContainer = document.getElementById('cartItemsList');
    const emptyState = document.getElementById('emptyCartState');
    const checkoutBtn = document.getElementById('checkoutBtn');

    if (cart.length === 0) {
        listContainer.innerHTML = '';
        emptyState.style.display = 'block';
        checkoutBtn.style.display = 'none';
        calculateTotals();
        return;
    }

    emptyState.style.display = 'none';
    checkoutBtn.style.display = 'block';
    listContainer.innerHTML = '';

    cart.forEach(item => {
        const itemHtml = `
            <div class="cart-item" id="cart-item-${item.id}">
                <img src="${item.image}" alt="${item.name}" class="cart-item-img">
                <div class="cart-item-details">
                    <div style="display:flex; align-items:center; gap:5px; margin-bottom:5px;">
                        <span class="veg-dot ${item.isVeg ? 'veg' : 'non-veg'}"></span>
                        <h4 class="cart-item-name">${item.name}</h4>
                    </div>
                    <div style="color:var(--mgr-dark); font-weight:600;">₹${item.price}</div>
                </div>
                <div class="qty-controls">
                    <button class="qty-btn" onclick="updateQuantity('${item.id}', -1)">-</button>
                    <span style="font-weight:600; width:20px; text-align:center;">${item.quantity}</span>
                    <button class="qty-btn" onclick="updateQuantity('${item.id}', 1)">+</button>
                </div>
                <div style="margin-left: 2rem; font-weight: 700; color: var(--mgr-red); width: 80px; text-align: right;">
                    ₹${(item.price * item.quantity).toFixed(2)}
                </div>
                <button onclick="removeItem('${item.id}')" style="margin-left: 1.5rem; background:none; border:none; color:var(--mgr-gray); font-size:1.5rem; cursor:pointer; transition:color 0.3s;">
                    &times;
                </button>
            </div>
        `;
        listContainer.insertAdjacentHTML('beforeend', itemHtml);
    });

    calculateTotals();
}

function updateQuantity(id, delta) {
    let cart = getCart();
    const index = cart.findIndex(i => i.id === id);
    
    if (index !== -1) {
        cart[index].quantity += delta;
        if (cart[index].quantity <= 0) {
            cart.splice(index, 1);
        }
        saveCart(cart);
        renderCart();
    }
}

function removeItem(id) {
    let cart = getCart();
    cart = cart.filter(i => i.id !== id);
    saveCart(cart);
    
    // Add fade out animation before re-rendering
    const el = document.getElementById(`cart-item-${id}`);
    if(el) {
        el.style.opacity = '0';
        el.style.transform = 'translateX(-20px)';
        setTimeout(renderCart, 300);
    } else {
        renderCart();
    }
}

function calculateTotals() {
    const cart = getCart();
    let subtotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    
    let delivery = 0;
    if (subtotal > 0 && subtotal < 500) {
        delivery = 40; // Flat ₹40 delivery if order is below ₹500
    }

    let total = subtotal + delivery;

    document.getElementById('cartSubtotal').textContent = `₹${subtotal.toFixed(2)}`;
    document.getElementById('cartDelivery').textContent = delivery > 0 ? `₹${delivery.toFixed(2)}` : (subtotal > 0 ? 'Free' : '₹0.00');
    document.getElementById('cartTotal').textContent = `₹${total.toFixed(2)}`;
}
