# Generated by Django 4.1.3 on 2023-08-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('invoice_no', models.IntegerField()),
                ('phone_no', models.IntegerField()),
                ('exame_namee', models.CharField(max_length=200)),
                ('exam_link', models.URLField(max_length=1000)),
            ],
        ),
    ]
