# Generated by Django 4.0 on 2022-02-16 19:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_feedback_contact_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('firstname', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('profile_pic', models.FileField(default='static/user.png', null=True, upload_to='static/author_profile')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('created_time', models.TimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]