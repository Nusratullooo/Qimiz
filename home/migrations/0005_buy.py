from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
                ('topping', models.CharField(max_length=20)),
                ('crust', models.CharField(max_length=20)),
                ('qty', models.CharField(max_length=20)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
