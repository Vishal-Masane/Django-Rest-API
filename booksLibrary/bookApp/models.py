from django.db import models

# Create your models here.


class BooksLibrary(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    Author = models.CharField(max_length=50)
    Is_Publish = models.BooleanField(default=True)

    class Meta:
        db_table = "books_library"

    def __str__(self):
        return f"{self.__dict__}"
    