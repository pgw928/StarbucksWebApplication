from django.db import models
from accounts.models import User


# coffee,desserts,goods 모델 추가 김은수
class Coffee(models.Model):
    text = models.CharField(max_length=100)
    cd = models.IntegerField()
    name = models.CharField(max_length=40)
    allergy = models.CharField(max_length=100, blank=True, null=True)
    kcal = models.IntegerField()
    sat_fat = models.IntegerField(db_column='sat_FAT')  # Field name made lowercase.
    protein = models.IntegerField()
    fat = models.IntegerField()
    trans_fat = models.IntegerField(db_column='trans_FAT')  # Field name made lowercase.
    sodium = models.IntegerField()
    sugars = models.IntegerField()
    cholesterol = models.IntegerField()
    chabo = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Coffee'

    def __str__(self):
        return self.name


class Desserts(models.Model):
    text = models.CharField(max_length=100)
    cd = models.IntegerField()
    name = models.CharField(max_length=40)
    gram = models.IntegerField()
    allergy = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Desserts'

    def __str__(self):
        return self.name


class Goods(models.Model):
    text = models.CharField(max_length=100)
    cd = models.IntegerField()
    name = models.CharField(max_length=40)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Goods'

    def __str__(self):
        return self.name


class Carts(models.Model):
    identity = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField('상품명', max_length=40, null=True)
    price = models.IntegerField('가격', default=0)
    quantity = models.IntegerField('수량', default=0)
    total = models.IntegerField('총가격', default=0)
    cd = models.IntegerField('cd', null=True)
    category = models.CharField('카테고리', max_length=20, null=True)

    def __str__(self):
        return self.name


class StarbucksAddress(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'starbucks_address'
