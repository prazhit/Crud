from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()

    edu_choices = (
        ('SLC','S.L.C'),
        ('+2','+2'),
        ('Bachelor','Bachelor'),
        ('Master','Master')

        )
    education_level = models.CharField(max_length=200, choices=edu_choices)

    work_choices = (
        ('6 months','6 months'),
        ('1 year','1 year'),
        ('2 years or more','2 years or more')
    )
    work_experience = models.TextField(max_length=200, choices=work_choices)

    def __str__(self):
        return self.name
