# Generated by Django 4.2 on 2024-03-30 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_interestd_profile_interested_profile_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='cellphone',
            new_name='personal_email',
        ),
        migrations.AddField(
            model_name='profile',
            name='specializations',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
