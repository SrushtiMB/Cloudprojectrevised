from django.forms import ModelForm
from WebApp1.models import Student

class StudentForm(ModelForm):
	class Meta:
		model = Student
		#fields = ("studentId","firstName","lastName","eMail","mailingAddress","gpa")
		fields = "__all__"