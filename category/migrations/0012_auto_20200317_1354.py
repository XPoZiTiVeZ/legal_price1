# Generated by Django 2.2.9 on 2020-03-17 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_category_isoriginal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='count',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='works',
            name='specialist_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='specialist_type', to='category.Specialist'),
        ),
    ]
