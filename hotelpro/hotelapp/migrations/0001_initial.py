# Generated by Django 4.1.7 on 2023-06-01 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pic')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('des', models.CharField(max_length=100)),
            ],
        ),
    ]