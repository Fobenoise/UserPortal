from django.db import models
from sqlparse import formatter



class RoleProfile(models.Model):
    name = models.CharField(max_length=100)
            
    def __str__(self):
        return self.name    
    
class Equipment(models.Model):
    kind = models.CharField(max_length=100, null=True, blank=False, default="")
    brand = models.CharField(max_length=100)
    modelname = models.CharField(max_length=100, null=True, blank=False, default="")
    availability = \
        models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)
    
    def __str__(self):
        return self.kind + " | " + self.brand + " | " + self.modelname
    
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    role = models.ForeignKey(RoleProfile, null=True, \
        blank=True, on_delete=models.SET_NULL)
    
    eqitem = models.ForeignKey(Equipment, null=True, \
        blank=True, default="", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name + " | " + (self.email)
    

    
