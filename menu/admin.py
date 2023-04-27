from django.contrib import admin

from menu.models import MenuNode

class MenuNodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'level']
    search_fields = ['name', 'level']
    ordering = ['level']

    class MenuNodeInLine(admin.TabularInline):
        model = MenuNode
        extra = 1

    inlines = [MenuNodeInLine]

admin.site.register(MenuNode, MenuNodeAdmin)
