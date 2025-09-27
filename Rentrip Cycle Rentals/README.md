# PedalPower Rentals - Django Bike Rental System

A modern, full-featured bike rental website built with Django, featuring a beautiful glassmorphism UI design with Tailwind CSS.

## Features

### 🚴‍♂️ Core Functionality
- **Dynamic Bike Listing** - Browse available bikes with real-time availability
- **User Authentication** - Secure signup/login system with customer profiles
- **Booking System** - Book bikes with date/time selection and automatic availability management
- **Rental Management** - Track active rentals and rental history
- **Contact System** - Functional contact form with message storage
- **Admin Panel** - Comprehensive Django admin for managing all data

### 🎨 Design Features
- **Modern UI** - Glassmorphism design with gradient backgrounds
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Smooth Animations** - Hover effects, transitions, and floating animations
- **Interactive Elements** - Dynamic modals, real-time cost calculation
- **Professional Layout** - Clean navigation, beautiful cards, and intuitive UX

### 🔧 Technical Features
- **Django Framework** - Robust backend with MVC architecture
- **SQLite Database** - Lightweight database for development
- **Image Upload** - Support for bike images with media handling
- **Form Validation** - Comprehensive form validation and error handling
- **Message Framework** - User feedback with success/error notifications
- **Security** - CSRF protection, user authentication, and secure forms

## Project Structure

```
personal-website/
├── bikerental/                 # Django project settings
│   ├── __init__.py
│   ├── settings.py            # Main configuration
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── rental/                    # Main application
│   ├── __init__.py
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── urls.py               # App URL patterns
│   ├── forms.py              # Django forms
│   ├── admin.py              # Admin configuration
│   ├── apps.py               # App configuration
│   └── tests.py              # Test cases
├── templates/                 # HTML templates
│   ├── base.html             # Base template
│   └── rental/               # App-specific templates
│       ├── home.html         # Homepage
│       ├── bikes.html        # Bike listing
│       ├── about.html        # About page
│       ├── contact.html      # Contact form
│       ├── login.html        # User login
│       ├── signup.html       # User registration
│       ├── book_bike.html    # Bike booking
│       ├── my_rentals.html   # Rental history
│       ├── return_bike.html  # Bike return
│       └── admin_login.html  # Admin access
├── static/                   # Static files (auto-created)
├── media/                    # User uploads (auto-created)
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── setup_project.py          # Project setup script
└── README.md                 # This file
```

## Models

### 🚲 Bike Model
- `name` - Bike name
- `model` - Bike model/type
- `description` - Detailed description
- `rent_per_hour` - Hourly rental rate
- `available` - Availability status
- `image` - Bike photo (optional)

### 👤 Customer Model
- `user` - Link to Django User model
- `phone` - Customer phone number
- `created_at` - Registration timestamp

### 📅 Rental Model
- `bike` - Foreign key to Bike
- `customer` - Foreign key to Customer
- `start_time` - Rental start time
- `end_time` - Rental end time (when returned)
- `total_cost` - Calculated rental cost
- `is_active` - Active rental status

### 📧 ContactMessage Model
- `name` - Sender name
- `email` - Sender email
- `message` - Message content
- `created_at` - Message timestamp
- `is_read` - Admin read status

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Database and Sample Data
```bash
python setup_project.py
```

### 3. Run Development Server
```bash
python manage.py runserver
```

### 4. Access the Website
- **Main Site**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin
  - Username: `admin`
  - Password: `admin123`

## Usage Guide

### For Customers
1. **Browse Bikes** - Visit the bikes page to see available rentals
2. **Sign Up** - Create an account to start booking
3. **Book a Bike** - Select a bike and choose your rental start time
4. **Manage Rentals** - View active rentals and return bikes when done
5. **Contact Support** - Use the contact form for questions

### For Administrators
1. **Access Admin Panel** - Use the admin login to access Django admin
2. **Manage Bikes** - Add, edit, or remove bikes from the fleet
3. **View Customers** - Monitor customer registrations and details
4. **Track Rentals** - Monitor active and completed rentals
5. **Handle Messages** - Respond to customer contact messages

## Deployment Preparation

### 1. Update Settings for Production
```python
# In bikerental/settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Configure static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### 2. Collect Static Files
```bash
python manage.py collectstatic
```

### 3. Set Environment Variables
```bash
# Set a secure secret key
export SECRET_KEY='your-secure-secret-key-here'

# Configure database URL if using PostgreSQL
export DATABASE_URL='postgresql://user:password@localhost/dbname'
```

### 4. Configure Media Files
Ensure your web server can serve files from the `media/` directory for user uploads.

## Customization

### Adding New Bike Types
1. Add bikes through the Django admin panel
2. Upload bike images for better presentation
3. Set appropriate pricing and descriptions

### Modifying the Design
- Edit templates in `templates/rental/`
- Customize CSS classes (Tailwind CSS is used)
- Modify colors and animations in `base.html`

### Extending Functionality
- Add new models in `rental/models.py`
- Create new views in `rental/views.py`
- Add URL patterns in `rental/urls.py`
- Create corresponding templates

## Security Features

- **CSRF Protection** - All forms include CSRF tokens
- **User Authentication** - Secure login/logout system
- **Input Validation** - Form validation and sanitization
- **Permission Checks** - Users can only access their own rentals
- **Admin Access Control** - Separate admin authentication

## Support

For technical support or questions about the bike rental system:
- Check the Django admin panel for customer messages
- Review the rental history for booking issues
- Monitor the application logs for technical problems

## License

This project is built for educational and commercial use. Feel free to modify and extend according to your needs.

---

**PedalPower Rentals** - Making cycling accessible to everyone! 🚴‍♂️✨
