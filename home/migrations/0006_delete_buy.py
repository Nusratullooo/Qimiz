from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_buy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Buy',
        ),
    ]
