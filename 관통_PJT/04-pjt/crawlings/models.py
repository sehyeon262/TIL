from django.db import models

# Create your models here.
class Stock(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=20)
    comment=models.TextField()
    stored_at=models.DateTimeField(auto_now_add=True)


