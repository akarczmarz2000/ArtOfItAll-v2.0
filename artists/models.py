from django.db import models

# Create your models here.
class Artists(models.Model):


    class Meta:
        verbose_name_plural = 'Artists'

    name = models.CharField(max_length=254)
    description = models.TextField()
    price_range = models.TextField()
    category = models.ForeignKey('products.Category', null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    request = models.BooleanField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name