from django.db import models

# Create your models here.



class Job(models.Model):
    title = models.CharField(max_length=1000)
    # location
    FT = 'ft'
    PT = 'pt'
    job_type_choices = [
        ('', 'Unknown Yet'),
        (FT, 'Full time'),
        (PT, 'Part time'),
    ]

    # job_choices = [
    #     (Full_time, 'Full time'),
    #     ('Part time', 'Part time')
    # ]

    job_type = models.CharField(max_length=2, choices=job_type_choices, default=FT)
    description = models.TextField(max_length=1000, default='')
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    # category =
    experience = models.IntegerField(default=1)
