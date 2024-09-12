from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class Bground(models.Model):
    img_bg = models.ImageField(upload_to='bgpic')

    def __str__(self):
        return f"Bground object {self.id}"


class Foods(models.Model):
    food_name = models.CharField(max_length=250)
    food_img = models.ImageField(upload_to='foodimg')
    food_desc = models.TextField()

    def __str__(self):
        return self.food_name


