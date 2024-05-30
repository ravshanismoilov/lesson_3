from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'CATEGORY'

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'AUTHOR'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Language(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'LANGUAGE'

    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=255)
    page = models.IntegerField()
    year = models.DateField()
    price = models.IntegerField()
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    language = models.ForeignKey(to=Language, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True, default='default_img/book_default.jpg')

    class Meta:
        db_table = 'BOOKS'

    def __str__(self):
        return self.title
