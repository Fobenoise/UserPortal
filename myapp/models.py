from django.db import models
from sqlparse import formatter



class RoleProfile(models.Model):
    name = models.CharField(max_length=100)
            
    def __str__(self):
        return self.name
    
    
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(RoleProfile, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
# class UserRoles(models.Model):
#     ROLE_CHOICES = [
#         ('admin', 'Admin'),
#         ('standard', 'Standard User'),
#         ('guest', 'Guest'),
#     ]

#     name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

#     def __str__(self):
#         return self.get_name_display()

#     class Meta:
#         # Specify that the model belongs to the 'roles' app and set the table name
#         db_table = 'role'
#         app_label = 'roles