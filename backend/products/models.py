from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL # auth.User


class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_disc(self):
        return "%.2f" %(float(self.price) * 0.8)
    