from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from decimal import Decimal

class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    page_count = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.01)
    register_date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(price__gt=Decimal('0')), name='price_gt_0'),
        ]

    def get_absolute_url(self):
        return reverse('home')