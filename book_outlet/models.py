from typing import Iterable, Optional
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # Harry Potter => harry-potter
    slug = models.SlugField(
        default='',
        null=False,
        db_index=True,
        blank=True
    )

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"title: {self.title}\n"
            f"rating: {self.rating}\n"
            f"author: {self.author}\n"
            f"is_bestselling: {self.is_bestselling}\n"
            f"slug: {self.slug}\n"
        )
