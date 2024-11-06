# Generated by Django 5.0.7 on 2024-11-06 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='profile',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='institution',
            new_name='institution_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='github',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='name',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='proficiency_level',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='nationality',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AddField(
            model_name='skill',
            name='level',
            field=models.CharField(default='Beginner', max_length=50),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(default='Unknown Skill', max_length=50),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='CV.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='skill',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='CV.profile'),
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_name', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='CV.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(default='No description provided')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='CV.profile')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='CV.user'),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]
