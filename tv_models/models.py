from django.db import models
from django.urls import reverse


# Create your models here.
class TVModel(models.Model):
    S_SIZE = (
        ('32', '32'),
        ('40', '40'),
        ('43', '43'),
        ('49', '49'),
        ('55', '55'),
    )
    Year = (('2018', '2018'),
            ('2017', '2017'),
            ('2016', '2016'),
            ('2019', '2019'))
    HDR = (('yes', 'Yes'),
           ('No', 'No'))
    OS = (('Tizen', 'Tizen'),
          ('Orsay', 'Orsay'),)
    RESOLUTION = (('FHD', 'FHD'), ('UHD', 'UHD'))

    title = models.CharField(max_length=15)
    model_year = models.CharField(max_length=4, choices=Year)
    screen_size = models.CharField(max_length=2, choices=S_SIZE)
    resolution = models.CharField(max_length=3, choices=RESOLUTION)
    hdr = models.CharField(max_length=3, choices=HDR)
    system_os = models.CharField(max_length=8, choices=OS)
    content = models.TextField(max_length=255, default='Describe key features')
    manual = models.URLField(verbose_name='here lies url', blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tv_models-tvmodel_detail', kwargs=({'pk': self.pk}))
