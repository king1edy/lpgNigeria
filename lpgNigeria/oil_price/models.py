from django.db import models


# Create your models here.
class OilPrice(models.Model):
    date = models.DateField(auto_created=None)
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=18, decimal_places=2)

    def __self__(self):
        return "{}-{}-{}".format(self.date, self.company, self.price)
