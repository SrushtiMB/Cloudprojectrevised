from django.db import models

# Create your models here.

class Student(models.Model):
	studentId = models.CharField(max_length = 20)
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	eMail = models.EmailField()
	mailingAddress = models.CharField(max_length = 120)
	gpa = models.IntegerField()
	class Meta:
		db_table = "student"