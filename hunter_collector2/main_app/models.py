from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# WEAPON_CHOICES= (
#     ('great_sword', 'Great Sword'),
#     ('sword_&_shield', 'Sword & Shield'),
#     ('dual_blades', 'Dual Blades'),
#     ('long_sword', 'Long Sword'),
#     ('hammer', 'Hammer'),
#     ('hunting_horn', 'Hunting Horn'),
#     ('lance', 'Lance'),
#     ('gunlance', 'Gunlance'),
#     ('switch_axe', 'Switch Axe'),
#     ('charge_blade', 'Charge Blade'),
#     ('insect_glaive', 'Insect Glaive'),
#     ('bow', 'Bow'),
#     ('light_bowgun', 'Light Bowgun'),
#     ('heavy_bowgun', 'Heavy Bowgun')
# )

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    rarity = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('weapons_detail', kwargs={'pk': self.id})

class Hunter(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField()
    gender = models.CharField(max_length=100)
    favorite_meal = models.CharField(max_length=100)
    weapons = models.ManyToManyField(Weapon)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'hunter_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    hunter = models.ForeignKey(Hunter, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for hunter_id: {self.hunter_id} @{self.url}"