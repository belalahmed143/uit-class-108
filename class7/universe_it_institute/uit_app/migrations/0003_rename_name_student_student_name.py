# Generated by Django 4.1.2 on 2022-10-31 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uit_app', '0002_information'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='student_name',
        ),
    ]
