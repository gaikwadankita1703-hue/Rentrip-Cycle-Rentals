#!/usr/bin/env python
"""
Setup script for PedalPower Rentals Django project
Run this script to initialize the database and create sample data
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikerental.settings')
django.setup()

from django.contrib.auth.models import User
from rental.models import Bike, Customer, ContactMessage

def create_sample_data():
    """Create sample bikes and admin user"""
    
    # Create superuser if it doesn't exist
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@pedalpower.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print("✓ Created admin user (username: admin, password: admin123)")
    
    # Create sample bikes
    sample_bikes = [
        {
            'name': 'City Cruiser Pro',
            'model': 'Urban Explorer 2024',
            'description': 'Perfect for city commuting with comfortable seating and smooth ride. Features include LED lights, basket, and 7-speed transmission.',
            'rent_per_hour': 12.99,
            'available': True
        },
        {
            'name': 'Mountain Beast',
            'model': 'Trail Master X1',
            'description': 'Heavy-duty mountain bike designed for off-road adventures. Full suspension, 21-speed gear system, and all-terrain tires.',
            'rent_per_hour': 18.99,
            'available': True
        },
        {
            'name': 'Electric Glide',
            'model': 'E-Bike Deluxe',
            'description': 'Electric-powered bike with 50km range. Perfect for longer distances with minimal effort. USB charging port included.',
            'rent_per_hour': 25.99,
            'available': True
        },
        {
            'name': 'Speed Demon',
            'model': 'Racing Pro 2024',
            'description': 'Lightweight racing bike for speed enthusiasts. Carbon fiber frame, drop handlebars, and 16-speed transmission.',
            'rent_per_hour': 22.99,
            'available': True
        },
        {
            'name': 'Family Tandem',
            'model': 'Double Rider',
            'description': 'Fun tandem bike for couples or friends. Synchronized pedaling system with comfortable dual seating.',
            'rent_per_hour': 16.99,
            'available': False  # One bike rented for demo
        },
        {
            'name': 'Vintage Classic',
            'model': 'Retro Charm 1960',
            'description': 'Classic vintage-style bike with modern safety features. Leather seat, chrome details, and 3-speed hub.',
            'rent_per_hour': 14.99,
            'available': True
        }
    ]
    
    for bike_data in sample_bikes:
        bike, created = Bike.objects.get_or_create(
            name=bike_data['name'],
            defaults=bike_data
        )
        if created:
            print(f"✓ Created bike: {bike.name}")
    
    # Create sample contact message
    if not ContactMessage.objects.exists():
        ContactMessage.objects.create(
            name='John Doe',
            email='john@example.com',
            message='Hi! I\'m interested in your bike rental service. Do you offer group discounts for corporate events?'
        )
        print("✓ Created sample contact message")

def main():
    """Main setup function"""
    print("🚴 Setting up PedalPower Rentals...")
    print("=" * 50)
    
    # Run migrations
    print("📦 Creating database migrations...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    print("🗄️ Applying database migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create sample data
    print("🎯 Creating sample data...")
    create_sample_data()
    
    print("=" * 50)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Run: python manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000")
    print("3. Admin panel: http://127.0.0.1:8000/admin")
    print("   - Username: admin")
    print("   - Password: admin123")
    print("\n🚀 Your PedalPower Rentals website is ready!")

if __name__ == '__main__':
    main()
