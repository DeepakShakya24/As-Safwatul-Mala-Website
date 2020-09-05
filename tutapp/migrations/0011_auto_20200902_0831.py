# Generated by Django 2.2.5 on 2020-09-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutapp', '0010_auto_20200901_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advancetilawah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tilawah_title', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('tilawah_audio_file', models.FileField(blank=True, default='', upload_to='')),
                ('pub_date', models.DateField(null=True)),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Jazariyyah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jazariyyah_title', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('jazariyaah_audio_file', models.FileField(blank=True, default='', upload_to='')),
                ('pub_date', models.DateField(null=True)),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='audioclip',
            options={'ordering': ['pub_date']},
        ),
        migrations.AlterModelOptions(
            name='tajweed2',
            options={'ordering': ['pub_date']},
        ),
        migrations.AlterModelOptions(
            name='tajweed3',
            options={'ordering': ['pub_date']},
        ),
        migrations.AddField(
            model_name='tajweed2',
            name='pub_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tajweed3',
            name='pub_date',
            field=models.DateField(null=True),
        ),
    ]