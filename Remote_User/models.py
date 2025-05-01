from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class predict_web_classification(models.Model):

    Fid= models.CharField(max_length=3000)
    Protocol= models.CharField(max_length=3000)
    Flag= models.CharField(max_length=3000)
    Packet= models.CharField(max_length=3000)
    Sender_ID= models.CharField(max_length=3000)
    Receiver_ID= models.CharField(max_length=3000)
    Source_IP_Address= models.CharField(max_length=3000)
    Destination_IP_Address= models.CharField(max_length=3000)
    Source_Port= models.CharField(max_length=3000)
    Destination_Port= models.CharField(max_length=3000)
    Packet_Size= models.CharField(max_length=3000)
    Prediction= models.CharField(max_length=3000)
    Url= models.CharField(max_length=30000)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



