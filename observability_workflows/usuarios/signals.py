"""
signals documentation: https://docs.djangoproject.com/en/4.2/topics/signals/
trigger hooks pre/post actions 
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from usuarios.models import DatosUsuarios



@receiver(post_save, sender=User)
def create_data_users(sender, instance, created, **kwargs):
    DatosUsuarios.objects.create(usuario=instance)
    print('New user successfully created!')
    
# @receiver(post_save, sender=User)
# def update_data_users(sender, instance, created, **kwargs):
    
#     if created == False:
#         instance.datosusuario.save()
#         print('User updated successfully!')