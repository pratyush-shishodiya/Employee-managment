# Generated by Django 4.0.6 on 2022-07-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_alter_employee_hire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
