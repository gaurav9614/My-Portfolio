# Generated by Django 3.1.4 on 2020-12-11 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='decription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='portfolio/images/'),
        ),
    ]