from django.db import models

from account.models import User


# Create your models here.


class Patient(models.Model):
    # Gander Choices
    CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=100, blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    sex = models.CharField(max_length=3, choices=CHOICES, default="M")
    phone = models.CharField(max_length=25, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True)
    diagnosis = models.CharField(max_length=200, blank=True)
    prof_surgeon_consultant = models.CharField(max_length=200, blank=True)
    assign_doctor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_of_admission = models.DateTimeField(auto_now_add=True)
    date_of_discharge = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class CategoriesInfo(models.Model):
    # Info Types
    CHOICES = (
        ('L', 'Lab'),
        ('S', 'Surgery'),
        ('O', 'Other'),
    )

    type = models.CharField(max_length=3, choices=CHOICES, default="L")
    type_name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "CategoriesInfo"

    def __str__(self):
        return self.type_name + "--" + self.type


class Assign(models.Model):
    """
    Assign Lab or Surgery
    """

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    categories_info = models.ForeignKey(CategoriesInfo, on_delete=models.CASCADE)
    specimen = models.CharField(max_length=150, blank=True)
    investigation = models.CharField(max_length=250, blank=True)
    referred_by = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    finishing_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.categories_info.type_name + " for " + self.patient.name


class MediaImage(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.assign.categories_info.type_name + " Images for " + self.assign.patient.name


class MediaVideo(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/%Y/%m/%d/')

    def __str__(self):
        return self.assign.categories_info.type_name + " Video for " + self.assign.patient.name


class MediaDocument(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')

    def __str__(self):
        return self.assign.categories_info.type_name + " Document for " + self.assign.patient.name
