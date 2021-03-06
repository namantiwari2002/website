# Generated by Django 2.2.6 on 2020-02-24 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('is_merchant', models.BooleanField(default=False)),
                ('department', models.CharField(choices=[('CE', 'Chemical Engineering'), ('BioTech', 'Biotechnology'), ('Civil', 'Civil Engineering'), ('CSE', 'Computer Science and Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('EEE', 'Electronics and Electrical Engineering'), ('EP', 'Engineering Physics'), ('MnC', 'Mathematics and Computing'), ('Mech', 'Mechanical Engineering'), ('Design ', 'Design '), ('BnB', 'Biosciences and Bioengineering'), ('None', 'None')], default='None', max_length=120)),
                ('club', models.CharField(choices=[('Alcher', 'Alcheringa'), ('Cadence', 'Cadence'), ('AnR', 'Anchorenza and RadioG'), ('Fine Arts', 'Fine Arts'), ('Montage', 'Montage'), ('Lumiere', 'Lumiere'), ('Octaves', 'Octaves'), ('Expressions', 'Expressions'), ('LitSoc-DebSoc', 'LitSoc-DebSoc'), ('Aeromodelling', 'Aeromodelling'), ('Astronomy', 'Astronomy'), ('Coding', 'Coding'), ('CnA', 'Consulting and Analytics'), ('Electronics', 'Electronics'), ('Prakriti', 'Prakriti'), ('FnE', 'Finance and Economics'), ('Robotics', 'Robotics '), ('ACUMEN', 'ACUMEN'), ('TechEvince', 'TechEvince'), ('Green Automobile', 'Green Automobile'), ('EDC', 'Entrepreneurial Development Cell'), ('Udgam', 'Udgam'), ('Techniche', 'Techniche'), ('None', 'None')], default='None', max_length=120)),
                ('batch', models.CharField(choices=[('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('None', 'None')], default='None', max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.CharField(max_length=10)),
                ('house_no', models.CharField(max_length=120)),
                ('area', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('landmark', models.CharField(blank=True, max_length=120, null=True)),
                ('name', models.CharField(max_length=120)),
                ('mobile_no', models.CharField(max_length=10)),
                ('alternate_no', models.CharField(blank=True, max_length=10, null=True)),
                ('address_type', models.CharField(choices=[('H', 'Home Address'), ('W', 'Work/Office Address')], default='H', max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
