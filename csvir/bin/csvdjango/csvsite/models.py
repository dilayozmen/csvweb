from django.db import models

# Create your models here.
class CsvData(models.Model):
    states=(('acik','açık'),('kapali','kapalı'))
    adres=models.CharField(max_length=10)
    #durum variable has two options that are açık and kapalı
    durum=models.CharField(max_length=10,choices=states)
    hedef_adres=models.CharField(max_length=50)
    zaman=models.DateTimeField()
    class Meta:
        abstract=True
