# Generated by Django 4.0.3 on 2022-03-05 06:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_review_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='evaluation',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]