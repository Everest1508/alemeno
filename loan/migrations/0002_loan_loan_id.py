# Generated by Django 5.1.3 on 2024-11-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='loan_id',
            field=models.IntegerField(null=True),
        ),
    ]
