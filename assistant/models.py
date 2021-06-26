from django.db import models

from account.models import User


# Create your models here.


class Patient(models.Model):
    # Gander Choices
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100, blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    sex = models.CharField(max_length=25, choices=CHOICES, default="Male")
    phone = models.CharField(max_length=25, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True)
    diagnosis = models.CharField(max_length=200, blank=True)
    professor_surgeon_consultant = models.CharField(max_length=200, blank=True)
    assign_doctor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_of_admission = models.DateTimeField(auto_now_add=True)
    date_of_discharge = models.DateTimeField(null=True, blank=True)

    # image field for pfp

    def __str__(self):
        return self.name


class Assign(models.Model):
    """
    Assign Lab or Surgery
    """
    CHOICES = (
        ('Lab', 'Lab'),
        ('Surgery', 'Surgery'),
        ('Other', 'Other'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    categories = models.CharField(max_length=20, choices=CHOICES, default="Lab")
    name = models.CharField(max_length=150, blank=True)
    indication = models.CharField(max_length=250, blank=True, null=True)
    referred_by = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    finishing_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.categories + " for " + self.patient.name


class MediaImage(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.assign.categories + " Images for " + self.assign.patient.name


class MediaVideo(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/%Y/%m/%d/')

    def __str__(self):
        return self.assign.categories + " Video for " + self.assign.patient.name


class MediaDocument(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')

    def __str__(self):
        return self.assign.categories + " Document for " + self.assign.patient.name
