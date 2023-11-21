# Generated by Django 4.2.7 on 2023-11-21 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_book_author_author_books_alter_review_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='library.author'),
        ),
    ]
