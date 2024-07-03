from django.db import models


class CsvData(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.name
