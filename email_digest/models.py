from django.db import models

from hacker_news.models import AccountCustomUser
from news.models import NewsStory


class EmailDigestSubscription(models.Model):
    frequency = models.CharField(verbose_name='frequency', max_length=42)
    weekly_weekday = models.CharField(verbose_name='weekly weekday', max_length=32, blank=True, null=True)
    verified_email = models.CharField(verbose_name='verified email', max_length=32, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='is active', default=True)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.frequency}'


class EmailDigestEmailDigest(models.Model):
    frequency = models.CharField(verbose_name='frequency', max_length=32)
    weekly_weekday = models.CharField(verbose_name='weekly weekday', max_length=32, blank=True)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.frequency} {self.weekly_weekday}'


class EmailDigestUnsubscription(models.Model):
    from_digest = models.ForeignKey(to=EmailDigestEmailDigest, on_delete=models.CASCADE, blank=True, null=True)
    subscription = models.ForeignKey(to=EmailDigestSubscription, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.from_digest} {self.subscription}'


class EmailDigestEmailDigestStories(models.Model):
    email_digest = models.ForeignKey(to=EmailDigestEmailDigest, on_delete=models.CASCADE)
    story = models.ForeignKey(to=NewsStory, on_delete=models.CASCADE)
    # Indexes = [
    #     models.Index(['story', 'email_digest'])
    # ]

    def __str__(self):
        return f'{self.email_digest}  {self.story}'


class EmailDigestUserSubscription(models.Model):
    subscription = models.OneToOneField(to=EmailDigestSubscription, primary_key=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subscription}  {self.user}'


class EmailDigestAnonymousSubscription(models.Model):
    subscription_ptr = models.OneToOneField(to=EmailDigestSubscription, on_delete=models.CASCADE, primary_key=True)
    logged_in_user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    verified = models.BooleanField(verbose_name='verified', default=False)
    verified_at = models.DateTimeField(verbose_name='verified at', blank=True, null=True)
    verified_code = models.CharField(verbose_name='verified code', max_length=21)
    email = models.CharField(verbose_name='email', max_length=32, blank=True)

    def __str__(self):
        return {self.verified}
