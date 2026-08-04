# 🍽️ Mari Gold Restaurant (MGR) - Food Ordering App

A full-stack, modern food ordering web application designed and built for **Mari Gold Restaurant (MGR)**. This web application provides a seamless online ordering experience for customers and a robust management portal for restaurant administrators.

---

## 📝 About

**Mari Gold Restaurant (MGR) Food Ordering App** enables customers to explore delicious menus across multiple categories, customize quantities, place instant orders with UPI or Cash on Delivery, and track order progress in real-time through an interactive timeline. Restaurant managers gain access to a dedicated admin dashboard equipped with real-time analytics, inventory/menu control, order management, and customer review moderation.

---

## ✨ Features

### 🛒 Customer Portal
- **Categorized Menu Navigation**: Browse items under *Veg*, *Non-Veg*, *Starters*, *Main Course*, *Desserts*, *Juices*, and *Sweets*.
- **Sub-Category Filtering & Search**: Instant real-time filtering by sub-categories and dynamic food item search.
- **Interactive Shopping Cart**: Add to cart with quantity selection, increment/decrement controls, real-time total calculations, and item persistence.
- **Streamlined Checkout**: Simple delivery address input with validated forms.
- **Flexible Payment Modes**: Support for **UPI** digital payments and **Cash on Delivery (COD)**.
- **Live Order Tracking**: Animated status timeline tracking orders through *Placed*, *Preparing*, *Out for Delivery*, and *Delivered*.
- **Customer Ratings & Reviews**: Post-order feedback system allowing customers to submit star ratings and detailed reviews.

### 🛡️ Admin Portal (MGR Management)
- **Analytics Dashboard**: Real-time insights on total revenue, active orders, top-selling items, and customer growth.
- **Menu Item Management**: Add, edit, or delete dishes complete with images, pricing, categories, and availability flags.
- **Order Management**: Comprehensive view of all incoming customer orders with instant status update controls (*Received*, *Preparing*, *Out for Delivery*, *Delivered*).
- **Review Moderation**: View, filter, and moderate customer ratings and written feedback.
- **User Management**: Overview of registered customer accounts and administrative permissions.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript (ES6+)
- **Backend**: Python 3.10+, Django 5.x
- **Database**: SQLite (SQL)
- **Styling**: Custom CSS (Minimalist Red & White theme with modern micro-interactions)
- **Deployment**: Vercel (`@vercel/python`)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher installed
- Git installed
- `pip` (Python Package Installer)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/food-ordering-app.git
   cd "Food Ordering App"
   ```

2. **Create and Activate Virtual Environment**
   - **Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Seed Sample Data (Admin & Initial Menu Items)**
   ```bash
   python manage.py seed_data
   ```

6. **Collect Static Files**
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

---

### 🔑 Default Admin Credentials

- **Username**: `admin`
- **Password**: `admin123`
- **Admin Panel URL**: [http://localhost:8000/mgr-admin/](http://localhost:8000/mgr-admin/)

---

### 🌐 Accessing the App

- **Customer Homepage**: [http://localhost:8000/](http://localhost:8000/)
- **Menu Page**: [http://localhost:8000/menu/](http://localhost:8000/menu/)
- **Admin Dashboard**: [http://localhost:8000/mgr-admin/](http://localhost:8000/mgr-admin/)

---

## 📦 Deploying to Vercel

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Log into Vercel**
   ```bash
   vercel login
   ```

3. **Deploy Project**
   ```bash
   vercel --prod
   ```

4. Your application will be live at your custom Vercel deployment URL!

---

## 📂 Project Structure

```
Food Ordering App/
├── food_ordering/          # Core Django project directory
│   ├── __init__.py
│   ├── settings.py         # App settings & static file configurations
│   ├── urls.py             # Root URL routing
│   ├── wsgi.py             # WSGI entrypoint for Vercel deployment
│   └── asgi.py             # ASGI entrypoint
├── menu/                   # App for menu, categories, sub-categories
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── orders/                 # App for cart, checkout, tracking & reviews
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── static/                 # Static assets (CSS, JS, Images)
│   ├── css/
│   │   └── style.css       # Red & White themed custom styles
│   ├── js/
│   │   ├── main.js
│   │   └── cart.js
│   └── images/
├── staticfiles/            # Collected static files for production
├── templates/              # HTML Templates
│   ├── base.html
│   ├── index.html
│   ├── menu.html
│   ├── cart.html
│   ├── checkout.html
│   ├── order_tracking.html
│   └── admin/
│       └── dashboard.html
├── db.sqlite3              # SQLite database file
├── .gitignore              # Git ignore configuration
├── requirements.txt        # Python package dependencies
├── vercel.json             # Vercel serverless deployment config
└── README.md               # Project documentation
```

---

## 🎨 Design

- **Color Scheme**: Minimalist Red (`#D32F2F`) & Crisp White (`#FFFFFF`) with soft shadow accents.
- **User Interface**: Micro-animations on buttons, hover effects, and animated state progress bars.
- **Mobile First**: Responsive layouts tailored for smartphones, tablets, and desktops.
- **Branding**: Clean Mari Gold Restaurant logo and typography.

---

## 📸 Screenshots

*(Screenshots will be added here upon final UI rendering)*

| Customer Homepage | Menu & Filtering | Order Tracking | Admin Dashboard |
|---|---|---|---|
| *[Homepage Screenshot]* | *[Menu Screenshot]* | *[Tracking Screenshot]* | *[Dashboard Screenshot]* |

---

## 🤝 Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git checkout -origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 👨‍💻 Developer

Built with ❤️ for **Mari Gold Restaurant**.
