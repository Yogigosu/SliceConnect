 
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, default='', max_length=128)),
                ('quantities', models.CharField(blank=True, default='', max_length=512)),
                ('subtotal', models.FloatField(blank=True, default=0.0)),
                ('total', models.FloatField(blank=True, default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(blank=True, default=False)),
                ('products', models.ManyToManyField(blank=True, to='foods.Food')),
                ('restaurant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(blank=True, default=0.0)),
                ('key', models.CharField(blank=True, default='', max_length=100)),
                ('used', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, default='', max_length=256)),
                ('order_no', models.CharField(blank=True, default='', max_length=256)),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=20)),
                ('shipping_address', models.CharField(default='', max_length=200)),
                ('status', models.BooleanField(blank=True, default=False)),
                ('payment_status', models.BooleanField(blank=True, default=False)),
                ('shipping_charge', models.FloatField(blank=True, default=30.0)),
                ('order_type', models.CharField(choices=[('home', 'Home'), ('hestaurant', 'Restaurant')], default='home', max_length=100)),
                ('payment_method', models.CharField(choices=[('pod', 'Pay On Delivery'), ('bkash', 'bKash'), ('dbbl', 'DBBL')], default='pod', max_length=100)),
                ('expected_time', models.TimeField(blank=True, default='', null=True)),
                ('discount', models.FloatField(blank=True, default=0.0)),
                ('cost', models.FloatField(blank=True, default=0.0)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Cart')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
