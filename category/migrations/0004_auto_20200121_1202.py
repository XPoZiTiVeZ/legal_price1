# Generated by Django 2.2.9 on 2020-01-21 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20200121_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='works',
            name='specialist_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialist_type', to='category.Specialist'),
        ),
    ]
