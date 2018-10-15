# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'website', 'phone')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-user')
        return queryset

    user_info.short_description = 'Short stuff'


admin.site.site_header = "Site Header"
admin.site.site_title = "Site title"

admin.site.register(UserProfile, UserProfileAdmin)