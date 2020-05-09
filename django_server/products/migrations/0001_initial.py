# Generated by Django 3.0 on 2020-04-25 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ProductName', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(help_text='Description', max_length=100)),
            ],
        ),
    ]