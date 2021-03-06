# Generated by Django 3.2.12 on 2022-02-24 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(db_column='author', default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Programming', 'Programming'), ('Health', 'Health'), ('Environment', 'Environment'), ('Business', 'Business'), ('Style', 'Style'), ('Travel', 'Travel')], default='Technology', max_length=50),
        ),
    ]
