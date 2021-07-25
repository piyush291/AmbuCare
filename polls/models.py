from django.db import models
from hospital.models import H_Details


# Create your models here.
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class feedback_hospital(models.Model):
    user=models.ForeignKey(H_Details, on_delete=models.CASCADE)
    good_votes = models.IntegerField()
    average_votes = models.IntegerField()
    bad_votes = models.IntegerField()

    def total_good_votes(self):
        return self.good_votes.count()

    def total_average_votes(self):
        return self.average_votes.count()

    def total_bad_votes(self):
        return self.bad_votes.count()
