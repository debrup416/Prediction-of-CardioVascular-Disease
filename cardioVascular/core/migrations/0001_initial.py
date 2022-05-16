# Generated by Django 4.0.4 on 2022-05-16 11:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cardioVascular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('cp', models.IntegerField(choices=[(0, 'Typical Angina'), (1, 'Aypical Angina'), (2, 'Non-anginal Pain'), (3, 'Asymtomatic')])),
                ('trestbps', models.IntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(94)])),
                ('chol', models.IntegerField(validators=[django.core.validators.MaxValueValidator(564), django.core.validators.MinValueValidator(126)])),
                ('fbs', models.IntegerField(choices=[(0, 'Greater than 120'), (1, 'Less than 120')])),
                ('restecg', models.IntegerField(choices=[(0, 'Normal'), (1, 'Having'), (2, 'Probable')])),
                ('thalach', models.IntegerField(validators=[django.core.validators.MaxValueValidator(202), django.core.validators.MinValueValidator(71)])),
                ('exang', models.IntegerField(choices=[(0, 'Yes'), (1, 'No')])),
                ('oldpeak', models.DecimalField(decimal_places=12, max_digits=24, validators=[django.core.validators.MaxValueValidator(6.2), django.core.validators.MinValueValidator(0)])),
                ('slope', models.IntegerField(choices=[(0, 'Up'), (1, 'Flat'), (2, 'Down')])),
                ('ca', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('thal', models.IntegerField(choices=[(0, 'Normal'), (1, 'Fixed'), (2, 'Rever')])),
            ],
        ),
    ]