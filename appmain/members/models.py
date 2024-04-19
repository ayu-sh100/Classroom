from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
       return self.name


class Organization(models.Model):
    orgname = models.CharField(max_length=50)
    domainname = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.CharField(max_length=50)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    userid = models.IntegerField(null=True,default=None)
    
    role = models.ManyToManyField(Role,blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    org = models.ForeignKey(Organization,default=None,on_delete=models.CASCADE,null=True,blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]

  

