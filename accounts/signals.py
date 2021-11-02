from accounts.models import *
from school_apps.admissions.models import Student
from django.dispatch import receiver
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance) 
    if instance.is_student==True:
        Student.objects.create(user=instance)
        

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()