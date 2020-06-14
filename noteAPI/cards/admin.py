from django.contrib import admin
from .models import Card
# Register your models here.


class cardAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'cardInfo', 'create', 'report']
    list_filter = ('title', )


admin.site.register(Card, cardAdmin)