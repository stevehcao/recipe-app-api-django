from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.conf import settings


# This usermanager class is only for altering create_user or create_superuser
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # **extra_fields, takes extra functions passed in to extra_fields
        # add new fields more flexible
        """Creates and saves a new User"""
        if not email:
            raise ValueError("Users must have valid email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        # using=self._db is for handling different database, can look up later
        # can normally just  do user.save()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser from the commandline"""
        # does not need to worry about extra_fields because creating superuser from the commandline
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    # extends Django user model and we can customize it
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)
    # foreign key to user model
    # best practice is grabbing auth user from settings
    # ForeignKey(model, what happens when you delete)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # string representation
    def __str__(self):
        return self.name