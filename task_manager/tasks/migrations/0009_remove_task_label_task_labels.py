# Generated by Django 5.1 on 2024-10-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0001_initial'),
        ('tasks', '0008_alter_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='label',
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='task_labels', to='marks.mark'),
        ),
    ]
