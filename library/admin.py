from django.contrib import admin
from .models import Author, Book, Review



# Register your models here.

class ProductAdmin(admin.ModelAdmin):       # Custom admin class for the Product model
    list_display = ['name', 'birth_date']   # Specifies the fields to display in the list view.
    list_filter = ['name']                  # Specifies the fields to provide filtering options for.
    search_fields = ['name']                # Enables search functionality on the 'name' field




admin.site.register(Author, ProductAdmin) # Registers the Author model with the Django admin site for management.
admin.site.register(Book)                 # Registers the Book model with the Django admin site for management.
admin.site.register(Review)               # Registers the Review model with the Django admin site for management.



