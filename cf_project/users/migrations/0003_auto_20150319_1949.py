# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150318_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name=b'Email', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name=b'First Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Last Name', blank=True),
            preserve_default=True,
        ),
    ]
