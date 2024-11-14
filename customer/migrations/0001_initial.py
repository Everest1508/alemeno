# Generated by Django 5.1.3 on 2024-11-13 15:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+91xxxxxxxxxx'. Up to 15 digits allowed.", regex='^[+]{1}(?:[0-9\\-\\(\\)\\/\\.]\\s?){6, 15}[0-9]{1}$')])),
                ('age', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0, message='Age must be positive'), django.core.validators.MaxValueValidator(100, message='Age must be less than or equal to 100')], verbose_name='Age')),
                ('monthly_salary', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0, message='Monthly salary cannot be negative')], verbose_name='Monthly Salary')),
                ('approved_limit', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0, message='Approved limit cannot be negative')], verbose_name='Approved Limit')),
                ('current_debt', models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0, message='Current debt cannot be negative')], verbose_name='Current Debt')),
            ],
        ),
    ]