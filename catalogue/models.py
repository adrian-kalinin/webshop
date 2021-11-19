from django.db import models


class Product(models.Model):
    product_code = models.CharField(max_length=10, editable=False, null=True, unique=True)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=1000, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    image = models.ImageField(upload_to='images/')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product_code = f'{self.id:5}'.replace(' ', '0')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.product_code})'
