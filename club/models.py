from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/club_pics/', default='images/club_pics/default.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubs"
        ordering = ['name']

