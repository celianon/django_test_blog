# Generated by Django 2.1.5 on 2019-02-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190224_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='author',
            field=models.CharField(db_index=True, default='anonamuse', max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(db_index=True, default='anonamuse', max_length=150),
        ),
    ]
