# Generated by Django 5.0.1 on 2024-01-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_userinformation_admin_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='qualification',
            field=models.CharField(choices=[('HSC_Passed', 'HSC Passed'), ('Diploma_in_Computer', 'Diploma in Computer'), ('BBA', 'BBA'), ('MBA', 'MBA'), ('English', 'English'), ('Accounting', 'Accounting')], max_length=100),
        ),
    ]
