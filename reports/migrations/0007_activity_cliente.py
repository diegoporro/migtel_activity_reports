# Generated by Django 4.2 on 2023-04-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_alter_activity_person2_alter_activity_person3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='Cliente',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]