# Generated by Django 3.0.2 on 2020-05-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FakeNewsApp', '0008_auto_20200213_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
    ]
