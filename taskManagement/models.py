from django.db import models


# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    ]
    title = models.CharField(max_length=50)
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES, default='LOW')
    done = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.priority} - {self.created.strftime("%m/%d/%Y")} done : {self.done}'
