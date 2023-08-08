from django.db import models

class trained_model(models.Model):
    name = models.CharField(max_length=100)
    model_data = models.BinaryField()
    scaler_data = models.BinaryField()