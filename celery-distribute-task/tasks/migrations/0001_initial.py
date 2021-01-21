# Generated by Django 2.2.9 on 2020-08-18 07:05

import core.utils
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
                ('done_time', models.DateTimeField(null=True)),
                ('node', models.PositiveSmallIntegerField(default=core.utils.node_generator)),
            ],
        ),
    ]