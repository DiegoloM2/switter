from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.urls import reverse

import uuid


class CustomUserManager(BaseUserManager): 

    #This function takes in as parameters only the required fields.
    def create_user(self, email, password):
        if not email: 
            raise ValueError("Users must have an email address")

        user = self.model(
            email = self.normalize_email(email), #this makes all email lowercase to be stored
        )
        user.set_password(password)
        user.save(using = self._db)

        return user
        
    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user


#AbstractBaseUser provides core implementation
#of user model, including hashed passwords and 
#tokenized password resets.


class CustomUser(AbstractBaseUser, PermissionsMixin): 

    #We want a custom id because an auto increasing id is a security liability since it 
    # gives hackers database information
    id = models.UUIDField( # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    #email field - we don't wsant username
    email = models.EmailField(max_length=60, unique = True) 
    
    #Required fields for AbstractBaseUser
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    last_login = models.DateTimeField(verbose_name = "last login", auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    #profilePic FIELD:
    profilePic = models.ImageField(upload_to = "profiles/", blank = True) 


    #Set this to whatever you want the user to be able to login with
    USERNAME_FIELD = 'email'
    

    #Set the user manager to the one created above.
    objects = CustomUserManager()

    def __str__(self): 
        return self.email

    def has_perm(self, perm, obj = None): #gets permissions for user
        return self.is_admin
    
    def has_module_perms(self, app_label): #gets module permissions
        return self.is_admin

    def get_absolute_url(self):
        return reverse("profile", args = [str(self.id)])