from django.db import models
from faker import Faker
import random

fake=Faker()


# Create your models here.
class StudentCon(models.Model):
    first_name=models.CharField(max_length=50,default=fake.first_name())
    last_name=models.CharField(max_length=50,default=fake.last_name())
    phone_nu=models.CharField(max_length=50,default=str(random.randint(8000000000,9000000000)))
    dob=models.DateField(default=fake.date())
    country=models.CharField(max_length=50,default=fake.country())
    status=models.BooleanField(default=False)
    password=models.CharField(max_length=55,default='None')
# s=Student(first_name='abc',last_name='zxc',phone_nu=123458,dob='2009-07-07',country='india',status=0)

    class Meta:
        db_table='Student_info'
