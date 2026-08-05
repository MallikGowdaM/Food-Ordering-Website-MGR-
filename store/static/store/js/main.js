// main.js - Core functionality

// CSRF Token Helper
function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}

// Toast Notification System
function showToast(message, type = 'success') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = 'toast';
    
    let icon = type === 'success' ? '✅' : '❌';
    let borderColor = type === 'success' ? 'var(--mgr-red)' : '#f44336';
    
    toast.style.borderLeftColor = borderColor;
    toast.innerHTML = `<span style="font-size: 1.2rem;">${icon}</span> <span>${message}</span>`;
    
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(100%)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Navbar Scroll Effect
window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Cart Helper Functions
function getCart() {
    const cart = localStorage.getItem('mgr_cart');
    return cart ? JSON.parse(cart) : [];
}

function saveCart(cart) {
    localStorage.setItem('mgr_cart', JSON.stringify(cart));
    updateCartBadge();
}

function getCartCount() {
    const cart = getCart();
    return cart.reduce((total, item) => total + item.quantity, 0);
}

function updateCartBadge() {
    const badge = document.getElementById('cartBadge');
    if(badge) {
        const count = getCartCount();
        badge.textContent = count;
        // Trigger bounce animation
        badge.style.animation = 'none';
        badge.offsetHeight; // trigger reflow
        badge.style.animation = null; 
    }
}

// Django Messages to Toasts
document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();
    
    const messages = document.getElementById('django-messages');
    if(messages) {
        const spans = messages.querySelectorAll('span');
        spans.forEach(span => {
            const type = span.dataset.type.includes('error') ? 'error' : 'success';
            showToast(span.textContent, type);
        });
    }

    // Mobile menu toggle logic
    const menuToggle = document.getElementById('menuToggle');
    const navLinks = document.getElementById('navLinks');
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            menuToggle.textContent = navLinks.classList.contains('active') ? '✕' : '☰';
        });
    }

    // Scroll Animations using Intersection Observer
    const animatedElements = document.querySelectorAll('.food-card, .timeline-step');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'all 0.6s ease';
        observer.observe(el);
    });
});
