from django.db import models

# Create your models here.

class Categories(models.Model):
    categoryid = models.IntegerField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    categorydescription = models.CharField(db_column='categoryDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categories'

class Product(models.Model):
    maker = models.CharField(max_length=1, blank=True, null=True)
    model = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'

class Printer(models.Model):
    model = models.IntegerField(primary_key=True)
    color = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    maker = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'printer'

class Pc(models.Model):
    model = models.IntegerField(primary_key=True)
    speed = models.FloatField(blank=True, null=True)
    ram = models.IntegerField(blank=True, null=True)
    hd = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    maker = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pc'

class Laptop(models.Model):
    model = models.IntegerField(primary_key=True)
    speed = models.FloatField(blank=True, null=True)
    ram = models.IntegerField(blank=True, null=True)
    hd = models.IntegerField(blank=True, null=True)
    screen = models.FloatField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    maker = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laptop'