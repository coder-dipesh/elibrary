# Generated by Django 4.0 on 2022-02-09 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=200, null=True)),
                ('book_price', models.FloatField()),
                ('stock', models.IntegerField(null=True)),
                ('book_image', models.ImageField(upload_to='static/uploads')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.category')),
            ],
        ),
    ]
