from django.contrib import admin

# Register your models here.
from to_do_list_app.models import List, Item


class ItemInLine(admin.StackedInline):
    model = Item
    extra = 1


class ListAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
    ]
    inlines = [ItemInLine]


admin.site.register(List, ListAdmin)
