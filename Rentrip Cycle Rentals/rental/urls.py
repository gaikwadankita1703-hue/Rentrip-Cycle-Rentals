from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cycles/', views.cycles, name='cycles'),  # bikes -> cycles
    path('contact/', views.contact, name='contact'),
    path('auth/', views.auth_page, name='auth'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('book/<int:cycle_id>/', views.book_cycle, name='book_cycle'),  # book_bike -> book_cycle
    path('my-rentals/', views.my_rentals, name='my_rentals'),
    path('return/<int:rental_id>/', views.return_cycle, name='return_cycle'),
    path('admin-login/', views.admin_login, name='admin_login'),
]
