from django.db import models

# Create your models here.

"""
Author:
	name
	birth_date
	biography
Book:
	title
	autor
	publication_date
	price
Review:
    book 
    reviewer_name
    content 
    rating(1:5)  
----------------------------  
ToDo:
    - github repo with project 
   	- design models 
    - Generate CRUD for Books

"""

class Author(models.Model):                 # Define the Author model, representing authors in the database
    name = models.CharField(max_length=100) # Character field for author's name, max length 100
    birth_date = models.DateField()         # Date field for author's birth date
    biography = models.TextField()          # Text field for author's biography

    def __str__(self):                      # Special method for string representation of the Author instance
        return self.name                    # Return author's name when Author instance is printed

class Book(models.Model):                   # Define the Book model, representing books in the database
    title = models.CharField(max_length=100)# Character field for book's title, max length 100
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # Foreign key to Author model, cascade delete
    publication_date = models.DateField()   # Date field for book's publication date
    price = models.DecimalField(max_digits=10, decimal_places=2) # Decimal field for book's price

    def __str__(self):                      # Special method for string representation of the Book instance
        return self.title                   # Return book's title when Book instance is printed

class Review(models.Model):                 # Define the Review model, representing book reviews in the database
    book = models.ForeignKey(Book, on_delete=models.CASCADE) # Foreign key to Book model, cascade delete
    reviewer_name = models.CharField(max_length=100) # Character field for reviewer's name, max length 100
    content = models.TextField()            # Text field for review content
    rating = models.IntegerField(choices=[(i, i) for i in range(1,6)]) # Integer field for review rating, choices 1-5

    def __str__(self):                      # Special method for string representation of the Review instance
        return self.reviewer_name           # Return reviewer's name when Review instance is printed

