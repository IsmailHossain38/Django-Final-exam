# Generated by Django 5.0 on 2024-01-16 13:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='accounts/image/')),
                ('date_of_birth', models.DateField()),
                ('qualification', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=12)),
                ('admin_approval', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userinformation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
