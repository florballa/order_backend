from django.db import models


class Costumer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
