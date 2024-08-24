from django.db import models

# from django.forms import ModelForm
# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    dob = models.DateField(null=True)
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Dept(models.Model):
    dName=models.CharField(max_length=255, verbose_name='DeptName')
    HOD=models.CharField(max_length=255)

    def __str__(self):
        return self.dName

class Emp(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    eName=models.CharField(max_length=255)
    deptID=models.ForeignKey(Dept, on_delete=models.CASCADE)
    gender=models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    # gender = ModelForm.ChoiceField(choices=GENDER_CHOICES, widget=models.RadioSelect())

    def __str__(self):
        return self.eName


class Master(models.Model):
    name = models.CharField(max_length=100)


class Detail(models.Model):
    master = models.ForeignKey(Master, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

