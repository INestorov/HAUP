# Generated by Django 3.2.3 on 2021-06-12 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210612_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classification',
            options={'ordering': ['year', 'tile']},
        ),
        migrations.AddField(
            model_name='classification',
            name='contains_greenery',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]