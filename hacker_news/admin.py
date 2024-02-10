from django.contrib import admin

from .models import *

admin.site.register(AccountsInvitation)
admin.site.register(AccountCustomUser)
admin.site.register(AccountsEmailVerification)
admin.site.register(AccountPasswordResetRequest)
admin.site.register(AuthPermission)
admin.site.register(AuthGroup)
