# Generated by Django 3.0.3 on 2020-03-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200308_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='wolf-logo_D5.png', upload_to='project_pics'),
        ),
    ]