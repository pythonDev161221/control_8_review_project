# Generated by Django 4.0.3 on 2022-03-05 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_review_evaluation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'permissions': [('can_moderate', 'может модерировать')]},
        ),
    ]