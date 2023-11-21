from django.contrib import admin
from .models import Author, Book, Review



# Register your models here.

class ProductAdmin(admin.ModelAdmin):               # Custom admin class for the Product model
    list_display = ['name', 'birth_date']           # Specifies the fields to display in the list view.
    list_filter = ['name', 'tags']                  # Specifies the fields to provide filtering options for.
    search_fields = ['name', 'tags']                # Enables search functionality on the 'name' field


class BookAdmin(admin.ModelAdmin):                  # Customizations for the Book model
    list_display = ['title', 'publication_date', 'price']
    list_filter = ['publication_date']
    search_fields = ['title']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'reviewer_name', 'rating']
    list_filter = ['rating']
    search_fields = ['book']


admin.site.register(Author, ProductAdmin)           # Registers the Author model with the Django admin site for management.
admin.site.register(Book, BookAdmin)                # Registers the Book model with the Django admin site for management.
admin.site.register(Review, ReviewAdmin)                         # Registers the Review model with the Django admin site for management.



