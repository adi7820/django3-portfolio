from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)
    image = models.ImageField(upload_to='personal_portfolio/images/')
    url = models.URLField(blank=True)
    upload = models.FileField(upload_to='personal_portfolio/uploads/', blank=True)

    def __str__(self):
        return self.title
