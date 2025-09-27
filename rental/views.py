from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .models import Cycle, Customer, Rental, ContactMessage
from .forms import CustomerSignUpForm, ContactForm, CycleRentalForm



def home(request):
    """Home page view"""
    featured_cycles = Cycle.objects.filter(available=True)[:3]
    return render(request, 'rental/home.html', {'featured_cycles': featured_cycles})


def about(request):
    """About page view"""
    return render(request, 'rental/about.html')


def cycles(request):
    """Cycle listing page view"""
    cycles = Cycle.objects.all()
    return render(request, 'rental/cycles.html', {'cycles': cycles})


from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')  # already logged in users

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        firstname = request.POST.get('fname')
        lname = request.POST.get('lname')

        # ✅ Validation
        if not (username and email and password and cpassword and firstname and lname):
            messages.error(request, "All fields are required")
            return redirect("signup")

        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("signup")

        # ✅ Create User
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = firstname
        user.last_name = lname
        user.save()

        messages.success(request, "Account created successfully. Please log in.")
        return redirect("login")

    return render(request, 'rental/signup.html')


def user_login(request):
    """User login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'rental/login.html')


@login_required
def book_cycle(request, cycle_id):
    """Book a cycle view"""
    cycle = get_object_or_404(Cycle, id=cycle_id)
    
    if not cycle.available:
        messages.error(request, 'This cycle is not available for booking.')
        return redirect('cycles')
    
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        messages.error(request, 'Customer profile not found. Please contact support.')
        return redirect('cycles')
    
    if request.method == 'POST':
        form = CycleRentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.cycle = cycle
            rental.customer = customer
            rental.save()
            
            # Mark cycle as unavailable
            cycle.available = False
            cycle.save()
            
            messages.success(request, f'Successfully booked {cycle.name}! Enjoy your ride.')
            return redirect('home')
    else:
        form = CycleRentalForm()
    
    return render(request, 'rental/book_cycle.html', {
        'cycle': cycle,
        'form': form
    })


@login_required
def my_rentals(request):
    """View user's rental history"""
    try:
        customer = Customer.objects.get(user=request.user)
        rentals = Rental.objects.filter(customer=customer).order_by('-created_at')
    except Customer.DoesNotExist:
        rentals = []
    
    return render(request, 'rental/my_rentals.html', {'rentals': rentals})


@login_required
def return_cycle(request, rental_id):
    """Return a rented cycle"""
    rental = get_object_or_404(Rental, id=rental_id, customer__user=request.user)
    
    if not rental.is_active:
        messages.error(request, 'This rental is already completed.')
        return redirect('my_rentals')
    
    if request.method == 'POST':
        rental.end_time = timezone.now()
        rental.total_cost = rental.calculate_cost()
        rental.is_active = False
        rental.save()
        
        # Mark cycle as available
        rental.cycle.available = True
        rental.cycle.save()
        
        messages.success(request, f'Cycle returned successfully! Total cost: ${rental.total_cost}')
        return redirect('my_rentals')
    
    return render(request, 'rental/return_cycle.html', {'rental': rental})


def auth_page(request):
    """Combined login/signup page"""
    return render(request, 'rental/auth.html')


def admin_login(request):
    """Admin login page"""
    return render(request, 'rental/admin_login.html')

from django.shortcuts import render

def contact(request):
    return render(request, 'rental/contact.html')

def Logout(request):
    logout(request)
    return redirect("rental/base.html")