from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.



class Job(models.Model):
    class JobTypeChoice(models.TextChoices):
        FULL_TIME = 'FT', _('Full time')
        PART_TIME = 'PT', _('Part time')

    title = models.CharField(max_length=1000)
    # location

    # Old way
    # FT = 'ft'
    # PT = 'pt'
    # job_type_choices = [
    #     ('', 'Unknown Yet'),
    #     (FT, 'Full time'),
    #     (PT, 'Part time'),
    # ]

    # job_type = models.CharField(max_length=2, choices=job_type_choices, default=FT)
    job_type = models.CharField(max_length=2, choices=JobTypeChoice.choices, default=JobTypeChoice.FULL_TIME)
    description = models.TextField(max_length=1000, default='', blank=True)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    # category =
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
