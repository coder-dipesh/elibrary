# Generated by Django 4.0 on 2022-02-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_category_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
