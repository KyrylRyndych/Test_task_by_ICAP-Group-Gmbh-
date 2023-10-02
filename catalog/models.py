from django.db import models


class Goods(models.Model):
    available = [
        ('Y', "Yes"),
        ('N', "No"),
    ]
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=250, blank=True)
    category = models.CharField(max_length=50)
    top_sel_month = models.CharField(max_length=1, choices=available)
    in_stock = models.CharField(max_length=1, choices=available)
    self_delivery = models.CharField(max_length=1, choices=available)
    description1 = models.CharField(max_length=250, null=True)
    description2 = models.CharField(max_length=250, null=True)
    price = models.IntegerField(default=1000)

    @property
    def description(self):

        return f"#{self.description1}#{self.description2}"

    def __str__(self):
        return f"{self.name} {self.description} Ціна: {self.price  }"


