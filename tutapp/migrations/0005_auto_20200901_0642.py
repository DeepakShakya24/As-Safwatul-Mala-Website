# Generated by Django 2.2.5 on 2020-09-01 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutapp', '0004_auto_20200901_0638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audioclip',
            options={'ordering': ('title',)},
        ),
    ]