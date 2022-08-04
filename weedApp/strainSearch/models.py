from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class strains(models.Model):
    strainName = models.CharField(max_length=255)
    strainType = models.CharField(max_length=255)
    strainRating = models.DecimalField(max_digits=2, decimal_places=1, null=True,blank=True)
    strainEffefts = models.CharField(max_length=255, blank=True, null=True)
    strainFlavor = models.CharField(max_length=255, blank=True, null=True)
    strainDescription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.strainName

    class Meta:
        db_table = 'strain'
        verbose_name = 'strain'