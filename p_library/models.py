from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=50)
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)


class Friend(models.Model):
    friend_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.friend_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    friend = models.ForeignKey('Friend', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
