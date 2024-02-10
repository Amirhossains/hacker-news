from django.db import models

from hacker_news.models import AccountCustomUser


class NewsItem(models.Model):
    # parent = models.ForeignKey(to='self', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    up_votes = models.IntegerField(verbose_name='up votes')
    down_votes = models.IntegerField(verbose_name='down votes')
    is_ask = models.BooleanField(verbose_name='is ask', default=False)
    is_show = models.BooleanField(verbose_name='is show', default=True)
    points = models.IntegerField(verbose_name='points', blank=True)
    num_comments = models.IntegerField(verbose_name='num comments', blank=True)
    left = models.IntegerField(verbose_name='left', blank=True, null=True)
    right = models.IntegerField(verbose_name='right', blank=True, null=True)
    tree_id = models.IntegerField(verbose_name='tree id', blank=True, null=True)
    level = models.IntegerField(verbose_name='level', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)
    indexes = [
        models.Index(fields=['points', 'created_at']),
        models.Index(fields=['id', 'created_at']),
        models.Index(fields=['created_at', 'id'])
    ]

    def __str__(self):
        return f'{self.user} {self.up_votes} {self.down_votes}'


class NewsVote(models.Model):
    item = models.ForeignKey(to=NewsItem, on_delete=models.CASCADE)
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(verbose_name='vote')
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.item}  {self.user} {self.vote}'


class NewsStory(models.Model):
    item_ptr = models.OneToOneField(primary_key=True, to=NewsItem, on_delete=models.CASCADE)
    # duplicate_of = models.ForeignKey(to='self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name='title', max_length=32)
    text = models.TextField(verbose_name='text', blank=True)
    url = models.CharField(verbose_name='url', max_length=50, blank=True, null=True)
    do_mail = models.CharField(verbose_name='do main', max_length=32, blank=True, null=True)
    indexes = [
        models.Index(fields=['do_mail', 'duplicate_of'])
    ]

    def __str__(self):
        return f'{self.item_ptr} {self.title}'


class NewsComment(models.Model):
    item_ptr = models.OneToOneField(primary_key=True, to=NewsItem, on_delete=models.CASCADE)
    to_story = models.ForeignKey(to=NewsStory, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='text')

    def __str__(self):
        return f'{self.item_ptr} {self.to_story} {self.text}'
