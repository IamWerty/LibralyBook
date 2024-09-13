from django.db import models

# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=120)
    avaible = models.BooleanField()

    class Meta:
        db_table = 'LibraryBook'
        ordering = ['author']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        unique_together = ('title','author')
        permissions = [
            ("can_view_author", "Can view author"),
        ]