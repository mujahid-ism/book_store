from typing import Iterable, Optional
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name_plural = 'Countries'


class Address(models.Model):
    street = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def full_address(self):
        return f"{self.street}, {self.post_code}, {self.city}"

    def __str__(self):
        return self.full_address()

    class Meta:
        verbose_name_plural = 'Address Entries'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address,
        null=True,
        on_delete=models.CASCADE
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    is_bestselling = models.BooleanField(default=False)
    # Harry Potter => harry-potter
    slug = models.SlugField(
        default='',
        null=False,
        db_index=True,
        blank=True
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True,
        related_name='books'
    )
    published_countries = models.ManyToManyField(
        Country,
        related_name='books'
    )

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"title: {self.title}\n"
            f"rating: {self.rating}\n"
            f"is_bestselling: {self.is_bestselling}\n"
            f"slug: {self.slug}\n"
        )
