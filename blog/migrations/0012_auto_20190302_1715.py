# Generated by Django 2.1.7 on 2019-03-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190302_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
