# Generated by Django 2.0.2 on 2018-03-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20180317_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='regno',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
