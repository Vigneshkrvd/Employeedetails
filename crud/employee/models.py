from django.db import models

class Employee(models.Model):
    empid=models.CharField(max_length=20)
    empname=models.CharField(max_length=20)
    email=models.EmailField()
    empcontact=models.CharField(max_length=20)

    def __str__(self):
        return "%s" %(self.empname)

    class meta:
        db_table="employee"