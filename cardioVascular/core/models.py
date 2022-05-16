from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
SEX_CHOICES = (
    (0,"Male"),
    (1,"Female"),
)

CP_CHOICES=(
    (0,'Typical Angina'),
    (1,'Aypical Angina'),
    (2,'Non-anginal Pain'),
    (3,'Asymtomatic'),
)

FBS_CHOICES=(
    (0,'Greater than 120'),
    (1,'Less than 120'),
)

ECG_CHOICES=(
    (0,'Normal'),
    (1,'Having'),
    (2,'Probable'),  
)

EX_CHOICES=(
    (0,'Yes'),
    (1,'No'),  
)

SLOPE_CHOICES=(
    (0,'Up'),
    (1,'Flat'),
    (2,'Down'),  
)

THAL_CHOICES=(
    (0,'Normal'),
    (1,'Fixed'),
    (2,'Rever'),  
)


class cardioVascular(models.Model):
    age=models.IntegerField()
    sex=models.IntegerField(choices=SEX_CHOICES)
    cp=models.IntegerField(choices=CP_CHOICES)
    trestbps=models.IntegerField(
        validators=[
            MaxValueValidator(200),
            MinValueValidator(94)
        ]
     )
    chol=models.IntegerField(
        validators=[
            MaxValueValidator(564),
            MinValueValidator(126)
        ]
     )	
    fbs=models.IntegerField(choices=FBS_CHOICES)	
    restecg=models.IntegerField(choices=ECG_CHOICES)	
    thalach=models.IntegerField(
        validators=[
            MaxValueValidator(202),
            MinValueValidator(71)
        ]
     )	
    exang=models.IntegerField(choices=EX_CHOICES)
    oldpeak=models.DecimalField(max_digits=24,decimal_places=12,
        validators=[
            MaxValueValidator(6.2),
            MinValueValidator(0)
        ]
     )	
    slope=models.IntegerField(choices=SLOPE_CHOICES)
    ca=models.IntegerField(
        validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ]
     )
    thal=models.IntegerField(choices=THAL_CHOICES)	

