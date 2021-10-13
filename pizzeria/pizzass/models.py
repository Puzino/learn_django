from django.db import models
from django.db.models.deletion import CASCADE


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'tippings'

    def __str__(self):
        if len(self.name) > 50:
            return f'{self.name[:50]}...'
        else:
            return self.name
