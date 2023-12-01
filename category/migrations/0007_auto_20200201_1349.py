# Generated by Django 2.2.9 on 2020-02-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20200121_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='works',
            field=models.ManyToManyField(related_name='works', to='category.Works'),
        ),
    ]