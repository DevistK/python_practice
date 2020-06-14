from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Card(models.Model):

    choice1 = '카드발급'
    choice2 = '카드분실'
    choice3 = '카드재발급'
    TITLE_IN_CHOICES = [
        (choice1, '카드발급'),
        (choice2, '카드분실'),
        (choice3, '카드재발급'),
    ]

    owner = models.ForeignKey(User, related_name='cards', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=60, choices=TITLE_IN_CHOICES)
    cardInfo = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    report = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create']