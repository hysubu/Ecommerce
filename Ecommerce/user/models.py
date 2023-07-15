from django.db import models

# Create your models here.

# class Choice(models.Model): 
#     CHOICE_STATE = ((
#         ("ODISHA",'ODISHA'),
#         ("KARNATAKA",'KARNATAKA'),
#         ("PUNJAB",'PUNJAB'),
#         ("ANDHRA PRADES",'ANDHRA PRADESH'),
#         ("ASSAM",'ASSAM'),
#         ("TAMILNADU",'TAMILNADU'),
#         ("BIHAR",'RAJASTAN'),
#         ("DELHI",'DELHI'),
#     ))



class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    contact_number = models.IntegerField(unique=True)
    profile_photo = models.FileField(upload_to="profile")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.TextField()
    password_key = models.TextField()


    def __str__(self):
        return self.first_name + " " + self.last_name 

class Address(models.Model):

    CHOICE_STATE = ((
        ("ODISHA",'ODISHA'),
        ("KARNATAKA",'KARNATAKA'),
        ("PUNJAB",'PUNJAB'),
        ("ANDHRA PRADES",'ANDHRA PRADESH'),
        ("ASSAM",'ASSAM'),
        ("TAMILNADU",'TAMILNADU'),
        ("BIHAR",'RAJASTAN'),
        ("DELHI",'DELHI'),
    ))
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=CHOICE_STATE,max_length=100)
    pincode = models.IntegerField()
    area = models.TextField()
    contact_number = models.IntegerField()

    # def __str__(self):
    #     return super().self.first_name +  self.last_name