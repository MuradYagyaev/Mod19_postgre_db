from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=5.00)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


class Test_table(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    production = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lesson1_test_table'


class Test_table2(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    production_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lesson1_test_table2'
