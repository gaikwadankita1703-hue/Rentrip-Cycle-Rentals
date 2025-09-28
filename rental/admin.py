from django.contrib import admin
from .models import Cycle, Customer, Rental, ContactMessage


@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'rent_per_hour', 'available', 'created_at')
    list_filter = ('available', 'created_at')
    search_fields = ('name', 'model', 'description')
    list_editable = ('available', 'rent_per_hour')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'model', 'description', 'image')
        }),
        ('Pricing & Availability', {
            'fields': ('rent_per_hour', 'available')
        }),
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'get_email', 'phone', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'phone')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    
    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_full_name.short_description = 'Full Name'
    
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('get_customer_name', 'get_cycle_name', 'start_time', 'end_time', 'total_cost', 'is_active')
    list_filter = ('is_active', 'start_time', 'created_at')
    search_fields = ('customer__user__first_name', 'customer__user__last_name', 'cycle__name')
    date_hierarchy = 'start_time'
    ordering = ('-created_at',)
    
    readonly_fields = ('total_cost', 'created_at')
    
    fieldsets = (
        ('Rental Information', {
            'fields': ('customer', 'cycle', 'start_time', 'end_time', 'is_active')
        }),
        ('Financial', {
            'fields': ('total_cost',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_customer_name(self, obj):
        return f"{obj.customer.user.first_name} {obj.customer.user.last_name}"
    get_customer_name.short_description = 'Customer'
    
    def get_cycle_name(self, obj):
        return f"{obj.cycle.name} - {obj.cycle.model}"
    get_cycle_name.short_description = 'Cycle'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_editable = ('is_read',)
    
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )


# Customize admin site
admin.site.site_header = " Rentrip Cycle Rentals Admin"
admin.site.site_title = " Rentrip Cycle Rentals Admin"
admin.site.index_title = "Welcome to Rentrip Cycle Rentals Administration"
