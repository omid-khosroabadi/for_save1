from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.conf import settings


class Mobile(models.Model):
    COLORS = (
        ('GREEN', 'green'),
        ('YELLOW', 'yellow'),
        ('BLUE', 'blue'),
        ('RED', 'red'),
        ('BROWN', 'brown'),
        ('WHITE', 'white'),
        ('BLACK', 'black'),
    )
    name = models.CharField(max_length=100)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    old_price = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='mobile_image/')
    weight = models.PositiveIntegerField()
    colors = MultiSelectField(choices=COLORS, max_length=200)
    datetime_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mobile_detail', args=[self.id])


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    text = RichTextField()
    image = models.ImageField(upload_to='book_image/', blank=True, default='static/img/No-Image.jpg')
    price = models.PositiveIntegerField(default=0)
    datetime_created = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    STAR = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'normal'),
        ('4', 'good'),
        ('5', 'perfect'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment_book', null=True, blank=True)
    body = models.TextField()
    recommend = models.BooleanField(default=True)
    star = models.CharField(max_length=200, choices=STAR)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('mobile_detail', args=[self.mobile.id])



