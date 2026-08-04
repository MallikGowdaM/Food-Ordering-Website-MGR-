// menu.js - Menu page interactions

function addToCart(id, name, price, image, isVeg) {
    // Check if user is logged in
    if (typeof IS_AUTHENTICATED !== 'undefined' && !IS_AUTHENTICATED) {
        showToast('Please login to add items to cart!', 'error');
        setTimeout(() => {
            window.location.href = LOGIN_URL + '?next=/menu/';
        }, 1500);
        return;
    }

    let cart = getCart();
    
    const existingItem = cart.find(i => i.id === id);
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            id: id,
            name: name,
            price: parseFloat(price),
            image: image,
            isVeg: isVeg === true || isVeg === 'true',
            quantity: 1
        });
    }
    
    saveCart(cart);
    showToast(`${name} added to cart!`);
}

// Search Functionality
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    if(searchInput) {
        searchInput.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            const cards = document.querySelectorAll('.food-card');
            
            cards.forEach(card => {
                const name = card.dataset.name;
                if(name.includes(term)) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }
});

// Veg/Non-Veg Filter
let activeVegFilter = null;

function toggleVegFilter(type) {
    const vegBtn = document.getElementById('filterVeg');
    const nonVegBtn = document.getElementById('filterNonVeg');
    const cards = document.querySelectorAll('.food-card');

    // Toggle logic
    if (activeVegFilter === type) {
        // disable filter
        activeVegFilter = null;
        vegBtn.classList.remove('btn-primary');
        vegBtn.classList.add('btn-outline');
        nonVegBtn.classList.remove('btn-primary');
        nonVegBtn.classList.add('btn-outline');
        
        cards.forEach(card => card.style.display = 'flex');
    } else {
        // enable filter
        activeVegFilter = type;
        if(type === 'veg') {
            vegBtn.classList.add('btn-primary');
            vegBtn.classList.remove('btn-outline');
            nonVegBtn.classList.remove('btn-primary');
            nonVegBtn.classList.add('btn-outline');
        } else {
            nonVegBtn.classList.add('btn-primary');
            nonVegBtn.classList.remove('btn-outline');
            vegBtn.classList.remove('btn-primary');
            vegBtn.classList.add('btn-outline');
        }

        cards.forEach(card => {
            if(card.dataset.veg === type) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }
}
