from django.contrib import admin
from .models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('tagname',)
    # list_dispaly 로 페이지에 나타나는 필드를 제어 한다.
    pass


admin.site.register(Tag, TagAdmin)
