# Generated by Django 2.1.5 on 2019-02-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(db_index=True, default='admin', max_length=150),
        ),
    ]
