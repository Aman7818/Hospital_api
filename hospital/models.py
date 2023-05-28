from django.db import models

class Doctor(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Patient(models.Model):
    phone_number = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    STATUS_CHOICES = (
        ('Negative', 'Negative'),
        ('Travelled-Quarantine', 'Travelled-Quarantine'),
        ('Symptoms-Quarantine', 'Symptoms-Quarantine'),
        ('Positive-Admit', 'Positive-Admit'),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
