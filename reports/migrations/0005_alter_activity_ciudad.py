# Generated by Django 4.2 on 2023-04-26 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_activity_person1_activity_person2_activity_person3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='Ciudad',
            field=models.CharField(choices=[('CCS', 'Caracas'), ('GUA', 'Guatire-Guarenas'), ('CAU', 'Caucagua'), ('HIG', 'Higuerote')], max_length=20),
        ),
    ]
