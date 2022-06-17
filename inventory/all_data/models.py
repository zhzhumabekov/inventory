from django.db import models


class Computer(models.Model):
    """Модель компьютера"""
    inventary_number = models.IntegerField()
    serial_number = models.IntegerField()
    computer_name = models.CharField(max_length=200)


class Person(models.Model):
    """Модель персонала"""
    name = models.CharField(max_length=200)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE,)
