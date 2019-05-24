# Generated by Django 2.0.6 on 2019-05-22 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NTWebsite', '0035_auto_20190520_1758'),
        ('NTNotification', '0013_auto_20190522_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name': '通知信息', 'verbose_name_plural': '通知信息'},
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='CObject',
            new_name='CommentInfo',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='RDObject',
            new_name='RollCallDialogue',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='RObject',
            new_name='RollCallInfo',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='TAObject',
            new_name='TopicInfo',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='CAObject',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='LObject',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='RPObject',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='TPObject',
        ),
        migrations.AddField(
            model_name='notice',
            name='UserLink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LObject', to='NTWebsite.UserLink', verbose_name='被关注者'),
        ),
    ]
