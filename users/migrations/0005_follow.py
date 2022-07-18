# Generated by Django 4.0.6 on 2022-07-18 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_created_at_user_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='users.user')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='users.user')),
            ],
            options={
                'db_table': 'follows',
            },
        ),
    ]
