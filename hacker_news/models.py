from django.contrib.auth.models import User
from django.db import models

from my_content.models import DjangoContentType


class AccountsInvitation(models.Model):
    invite_code = models.IntegerField(verbose_name='invite code')
    invited_email_address = models.CharField(verbose_name='invited email address', max_length=32, blank=True)
    num_signups = models.IntegerField(verbose_name='num signups', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.invite_code}'


class AccountCustomUser(models.Model):
    # user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    used_invitation = models.ForeignKey(to=AccountsInvitation, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(verbose_name='user name', max_length=32)
    email = models.CharField(verbose_name='email', max_length=32)
    password = models.CharField(verbose_name='password', max_length=12)
    first_name = models.CharField(verbose_name='first name', max_length=20, blank=True, null=True)
    last_name = models.CharField(verbose_name='last name', max_length=20, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='is active', default=False)
    is_staff = models.BooleanField(verbose_name='is staff', default=False)
    is_superuser = models.BooleanField(verbose_name='is superuser', default=False)
    last_login = models.DateTimeField(verbose_name='last login', blank=True, null=True)
    karma = models.IntegerField(verbose_name='karma', default=0, blank=True, null=True)
    about = models.TextField(verbose_name='about', blank=True)
    level = models.IntegerField(verbose_name='level')
    left = models.IntegerField(verbose_name='left', blank=True, null=True)
    right = models.IntegerField(verbose_name='right', blank=True, null=True)
    tree_id = models.IntegerField(verbose_name='tree id', blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)

    def __str__(self):
        return f'{self.username}  {self.is_staff}'


class AccountsEmailVerification(models.Model):
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    verified = models.BooleanField(verbose_name='verified', default=False)
    verified_at = models.DateTimeField(verbose_name='verified at', blank=True, null=True)
    verification_code = models.CharField(verbose_name='verification code', max_length=32)
    email = models.CharField(verbose_name='email', max_length=32)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.user}  {self.verified}'


class AccountPasswordResetRequest(models.Model):
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    verified_code = models.CharField(verbose_name='verified code', max_length=32)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.user}  {self.verified_code}'


class AuthPermission(models.Model):
    custom_user = models.ManyToManyField(to=AccountCustomUser)
    content_type = models.ForeignKey(to=DjangoContentType, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='name', max_length=32)
    codename = models.CharField(verbose_name='code name', max_length=32)
    # indexes = [
    #     models.Index([content_type, name])
    # ]

    def __str__(self):
        return f'{self.content_type}  {self.name}'


class AuthGroup(models.Model):
    name = models.CharField(verbose_name='name', max_length=32)
    permission = models.ManyToManyField(to=AuthPermission)
    custom_user = models.ManyToManyField(to=AccountCustomUser)

    def __str__(self):
        return self.name
