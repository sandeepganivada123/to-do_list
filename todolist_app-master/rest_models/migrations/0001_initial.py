# Generated by Django 2.1.7 on 2020-09-28 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Task', max_length=50)),
                ('done', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Tasks',
            },
        ),
    ]
