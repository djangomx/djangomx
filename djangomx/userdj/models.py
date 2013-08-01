#coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.safestring import mark_safe
import urllib
import hashlib

class UserManager(BaseUserManager):
    '''
    Manager for custom user account
    '''
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('El usuario debe tener un username')

        if not email:
            raise ValueError('El usuario debe tener un email')

        user = self.model(
            username = username,
            email = UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # This create a superuser with username, email, password
    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        user.is_active = True
        return user


class User(AbstractBaseUser):
    '''
    User custom for the site
    '''
    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.CharField(max_length=60, unique=True, db_index=True)
    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u"Fecha de creación")
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    class Meta:
        verbose_name = "Usuario"

    def __unicode__(self):
        return "%s" % (self.username,)

    def get_full_name(self):
        # The user is identified by their username
        return "%s" % (self.username,)

    def get_short_name(self):
        # The user is identified by their username
        return "%s" % (self.username,)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def image(self, size="64"):
        """
        Image default gravatar
        """
        gravatar_url = "https://www.gravatar.com/avatar.php?"
        gravatar_url += urllib.urlencode({
            'gravatar_id': hashlib.md5(self.email).hexdigest(),
            'size': str(size)
        })

        return mark_safe(
            '<a href="{0}" target="_blank" class="with-tooltip" title="Update your gravatar">'
            '<img src="{0}" alt="gravatar for {1}" class="user-icon" /></a>'.format(gravatar_url, self.username)
        )