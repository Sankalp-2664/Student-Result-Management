# Generated by Django 5.1.2 on 2024-10-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
