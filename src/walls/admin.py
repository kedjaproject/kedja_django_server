from django.contrib import admin

from walls import models

# Register your models here.


from walls.forms import RoleForm

admin.site.register(models.Collection)
admin.site.register(models.Card)


class WallRoleInline(admin.TabularInline):
    model = models.WallRole
    extra = 1
    form = RoleForm


@admin.register(models.Wall)
class WallAdmin(admin.ModelAdmin):
    inlines = (WallRoleInline,)
