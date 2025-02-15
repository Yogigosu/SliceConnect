 

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informations', '0001_initial'),
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.CharField(blank=True, default='', max_length=252, null=True)),
                ('min_serve_time', models.IntegerField(default=30, verbose_name='Minimum Serve Time')),
                ('min_order_tk', models.FloatField(default=150.0, verbose_name='Minimum Order')),
                ('service_charge', models.FloatField(default=30.0, verbose_name='Service Charge')),
                ('vat_tax', models.FloatField(blank=True, default=0.0, verbose_name='Vat/Tax')),
                ('address', models.CharField(max_length=1024)),
                ('environment', models.CharField(max_length=512)),
                ('map_embed_url', models.TextField(default='https://maps.google.com/')),
                ('logo', models.ImageField(blank=True, height_field='logo_height_field', null=True, upload_to='restaurant_logo/', verbose_name='logo', width_field='logo_width_field')),
                ('logo_height_field', models.IntegerField(default=0)),
                ('logo_width_field', models.IntegerField(default=0)),
                ('pp', models.ImageField(blank=True, height_field='pp_height_field', null=True, upload_to='restaurant_pp/', verbose_name='profile photo', width_field='pp_width_field')),
                ('pp_height_field', models.IntegerField(default=0)),
                ('pp_width_field', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('is_orderable', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extra_info', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informations.City')),
                ('food_items', models.ManyToManyField(blank=True, to='foods.Food')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ServiceTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_at', models.TimeField(blank=True, default='08:00:00')),
                ('close_at', models.TimeField(blank=True, default='20:00:00')),
                ('saturday', models.BooleanField(blank=True, default=True)),
                ('sunday', models.BooleanField(blank=True, default=True)),
                ('monday', models.BooleanField(blank=True, default=True)),
                ('tuesday', models.BooleanField(blank=True, default=True)),
                ('wednesday', models.BooleanField(blank=True, default=True)),
                ('thursday', models.BooleanField(blank=True, default=True)),
                ('friday', models.BooleanField(blank=True, default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.FloatField(blank=True, default=0.0)),
                ('price', models.FloatField(blank=True, default=0.0)),
                ('service', models.FloatField(blank=True, default=0.0)),
                ('environment', models.FloatField(blank=True, default=0.0)),
                ('reviewed_people_no', models.IntegerField(blank=True, default=0)),
                ('average', models.FloatField(blank=True, default=0.0)),
                ('status', models.CharField(blank=True, default='N/A', max_length=50, null=True)),
                ('star1', models.CharField(default='fa-star-o text-secondary', max_length=50)),
                ('star2', models.CharField(default='fa-star-o text-secondary', max_length=50)),
                ('star3', models.CharField(default='fa-star-o text-secondary', max_length=50)),
                ('star4', models.CharField(default='fa-star-o text-secondary', max_length=50)),
                ('star5', models.CharField(default='fa-star-o text-secondary', max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
            ],
        ),
    ]
