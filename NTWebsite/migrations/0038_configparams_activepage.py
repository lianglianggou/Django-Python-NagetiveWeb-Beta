# Generated by Django 2.0.6 on 2019-06-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NTWebsite', '0037_auto_20190522_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='configparams',
            name='ActivePage',
            field=models.CharField(default='ActivePage.html', max_length=100, verbose_name='激活跳转页'),
        ),
    ]