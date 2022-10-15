from email.policy import default
from unicodedata import category
from django.db import models
from django.utils import timezone


class Menu(models.Model):
    title = models.CharField(max_length=100)
    category = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    menu_image = models.TextField(blank=True)
    price = models.FloatField(default=0)
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def category_map(self):
        category = ["Brunch", "Salad", "Drink"]
        if self.category < len(category):
            return category[self.category]
        else:
            return "Unknown"

    def currency(self):
        return f"{int(self.price):,d}"

    def price_int(self):
        return int(self.price)
