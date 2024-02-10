from django.db import models

from hacker_news.models import AccountCustomUser


class DjangoContentType(models.Model):
    app_label = models.CharField(verbose_name='app label', max_length=32)
    model = models.CharField(verbose_name='model', max_length=32)
    # indexes = [
    #     models.Index(['model', 'app_label'])
    # ]

    def __str__(self):
        return f'{self.app_label}  {self.model}'


class DjangoAdminLog(models.Model):
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    content_type = models.ForeignKey(to=DjangoContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_repr = models.CharField(verbose_name='object repr', max_length=32)
    change_message = models.TextField(verbose_name='change message')
    object_id = models.TextField(verbose_name='object id', blank=True, null=True)
    action_flag = models.SmallIntegerField(verbose_name='action flag')
    action_time = models.DateTimeField(verbose_name='action time', blank=True, null=True)

    def __str__(self):
        return f'{self.user}  {self.object_repr}'
