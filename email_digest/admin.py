from django.contrib import admin

from .models import *

admin.site.register(EmailDigestSubscription)
admin.site.register(EmailDigestEmailDigest)
admin.site.register(EmailDigestUnsubscription)
admin.site.register(EmailDigestEmailDigestStories)
admin.site.register(EmailDigestUserSubscription)
admin.site.register(EmailDigestAnonymousSubscription)