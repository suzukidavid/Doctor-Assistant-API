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

    registration_number = models.CharField(max_length=50, blank=True, default='00000')
    name = models.CharField(max_length=100, blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    sex = models.CharField(max_length=25, choices=CHOICES, default="Male")
    phone = models.CharField(max_length=25, blank=True, null=True)
    profile_image = models.ImageField(upload_to='photos/patient/', default='photos/patient/avatar.png')
    address = models.CharField(max_length=200, blank=True)
    professor_surgeon_consultant = models.CharField(max_length=200, blank=True)
    assign_doctor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_of_admission = models.DateTimeField(null=True, blank=True)
    date_of_discharge = models.DateTimeField(null=True, blank=True)

    # image field for pfp

    def __str__(self):
        return self.name


class DiseaseLibrary(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    umls = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis_name = models.ManyToManyField(DiseaseLibrary, blank=True,
                                            related_name='diagnosis_name')
    T = models.CharField(max_length=20, blank=True, null=True)
    N = models.CharField(max_length=20, blank=True, null=True)
    M = models.CharField(max_length=20, blank=True, null=True)
    Stage = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Diagnosis"

    def __str__(self):
        return self.patient.name


class Examination(models.Model):
    """
    Patient Surgery Model

    Auto Field
    """
    primary_site = models.TextField(blank=True, null=True)
    nack_node = models.CharField(max_length=50, blank=True, null=True)
    other_site = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.primary_site


class Investigation(models.Model):
    """
    Patient Surgery Model
    """

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    reports = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    referred_by = models.CharField(max_length=50, blank=True, null=True)  # No Need
    receive_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Surgery(models.Model):
    """
    Patient Surgery Model
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    date_of_surgery = models.DateTimeField(null=True, blank=True)
    name_of_surgery = models.CharField(max_length=150, blank=True)
    indication = models.CharField(max_length=250, blank=True, null=True)
    findings = models.TextField(blank=True, null=True)

    # referred_by = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name_of_surgery


class HistoryOfCTRTCCTROther(models.Model):
    """
    Model History Of CT/RT/CCTR/Other for History Model

    """
    CHOICES = (
        ('CT', 'CT'),
        ('RT', 'RT'),
        ('CCRT', 'CCRT'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=20, choices=CHOICES, default="CT")
    dose = models.CharField(max_length=255, blank=True, null=True)  # Auto Field
    time_start = models.DateTimeField(blank=True, null=True)
    time_end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class FamilyHistory(models.Model):
    """
    Model Family History for History Model

    """
    relation_name = models.CharField(max_length=50, blank=True, null=True)
    illness = models.ManyToManyField(DiseaseLibrary, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.relation_name


class History(models.Model):
    """
    Patient History Model
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    history_of_present_illness = models.ManyToManyField(DiseaseLibrary, blank=True,
                                                        related_name='history_of_present_illness')  # Auto Suggest Field
    past_surgical_history = models.TextField(blank=True, null=True)  # Auto Suggest Field
    history_of_ct_rt_ccrt_other = models.ManyToManyField(HistoryOfCTRTCCTROther, blank=True,
                                                         related_name='history_of_ct_rt_ccrt_other')  # Auto Suggest Field
    co_morbidities = models.ManyToManyField(DiseaseLibrary, blank=True,
                                            related_name='co_morbidities')  # Auto Suggest Field
    family_history = models.ManyToManyField(FamilyHistory, blank=True,
                                            related_name='family_history')
    others = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.patient.name


class FollowUp(models.Model):
    """
    Follow up for patients
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    complaint = models.TextField(blank=True, null=True)  # Auto Suggest Field
    findings = models.TextField(blank=True, null=True)  # Auto Suggest Field
    investigation = models.TextField(blank=True, null=True)  # Auto Suggest Field Foreign key to Investigation table

    def __str__(self):
        return self.complaint


""" Media Models """


class InvestigationImage(models.Model):
    """
    Image for Investigation Model
    """
    assign = models.ForeignKey(Investigation, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/investigation/%Y/%m/%d/')


class InvestigationVideo(models.Model):
    """
    Video for Investigation Model
    """
    assign = models.ForeignKey(Investigation, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/investigation/%Y/%m/%d/')


class InvestigationDocument(models.Model):
    """
    Video for Investigation Model
    """
    assign = models.ForeignKey(Investigation, on_delete=models.CASCADE)
    document = models.FileField(upload_to='document/investigation/%Y/%m/%d/')


class SurgeryImage(models.Model):
    """
    Image for Surgery Model
    """
    assign = models.ForeignKey(Surgery, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/surgery/%Y/%m/%d/')


class SurgeryVideo(models.Model):
    """
    Video for Surgery Model
    """
    assign = models.ForeignKey(Surgery, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/surgery/%Y/%m/%d/')


class SurgeryDocument(models.Model):
    """
    Video for Surgery Model
    """
    assign = models.ForeignKey(Surgery, on_delete=models.CASCADE)
    document = models.FileField(upload_to='document/surgery/%Y/%m/%d/')


class FollowUpImage(models.Model):
    """
    Image for Follow Up Model
    """
    assign = models.ForeignKey(FollowUp, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/follow_up/%Y/%m/%d/')


class FollowUpVideo(models.Model):
    """
    Video for Follow Up Model
    """
    assign = models.ForeignKey(FollowUp, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/follow_up/%Y/%m/%d/')


class FollowUpDocument(models.Model):
    """
    Video for Follow Up Model
    """
    assign = models.ForeignKey(FollowUp, on_delete=models.CASCADE)
    document = models.FileField(upload_to='document/follow_up/%Y/%m/%d/')
