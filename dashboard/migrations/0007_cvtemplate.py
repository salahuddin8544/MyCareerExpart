# Generated by Django 4.2 on 2024-04-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_job_experience_job_specializations_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CvTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('resume', models.FileField(blank=True, null=True, upload_to='avatars/')),
            ],
        ),
    ]
