from django.contrib import admin
from treemenu.models import MenuItem, Menu


# class MenuItemAdmin(admin.ModelAdmin):
#     fields = ('title', 'link_url')

admin.site.register(Menu)
admin.site.register(MenuItem)
