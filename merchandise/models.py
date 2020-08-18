from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class League(models.Model):

    name = models.CharField(max_length=254)
    font_awesome = models.CharField(max_length=254,
                                    default='fas fa-football-ball')

    def __str__(self):
        return self.name


class Team(models.Model):
    division = models.ForeignKey('League', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    nickname = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Merchandise(models.Model):
    league = models.ForeignKey('League', null=True, blank=True,
                               on_delete=models.SET_NULL)
    team = models.ForeignKey('Team', null=True, blank=True,
                             on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    game_used = models.BooleanField(default=False, null=True, blank=False)
    signed = models.BooleanField(default=False, null=True, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock = models.IntegerField(validators=[MinValueValidator(1),
                                MaxValueValidator(100)], default=1,
                                null=True, blank=True)

    def __str__(self):
        return self.name
