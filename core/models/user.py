from django.contrib.auth import models as auth_models
from django.db import models


class UserManager(auth_models.BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The given email address must be set")
        email = UserManager.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    ###########################################################################
    def create_superuser(self, email, password, **extra_fields):
        superuser = self.create_user(email, password, **extra_fields)
        superuser.is_staff = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser


###############################################################################
###############################################################################
class User(auth_models.AbstractBaseUser):
    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")
    email = models.EmailField(unique=True, db_index=True)
    bio = models.TextField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    ###########################################################################
    ###########################################################################
    USERNAME_FIELD = "email"
    objects = UserManager()

    class Meta:
        app_label = "core"
        indexes = [
            models.Index(fields=['id', ]),
        ]

    def has_perm(self):
        return self.is_staff

    def has_module_perms(self):
        return self.is_staff

