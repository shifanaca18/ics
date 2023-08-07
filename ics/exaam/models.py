from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=120)
    invoice_no=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=20)
    exame_namee=models.CharField(max_length=200)
    exam_link=models.URLField(max_length=1000)
