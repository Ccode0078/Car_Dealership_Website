# Generated by Django 5.1.2 on 2024-10-31 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default=' ', upload_to=''),
            preserve_default=False,
        ),
    ]
