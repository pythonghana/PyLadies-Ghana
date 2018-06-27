# Generated by Django 2.0.1 on 2018-04-20 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='name',
            new_name='sponsor_name',
        ),
        migrations.RenameField(
            model_name='sponsor',
            old_name='url',
            new_name='sponsor_url',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='contact_email',
            field=models.EmailField(default='', help_text='We’ll keep it secret, for internal use only.', max_length=1024),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='contact_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='category',
            field=models.CharField(choices=[('Bronze', 'Bronze - $500'), ('Silver', 'Silver - $1000'), ('Gold', 'Gold - $2500'), ('Diamond', 'Diamond - $3500'), ('Other', 'Other')], max_length=15),
        ),
    ]
