from django.contrib import admin

from walls import models

# Register your models here.


from walls.forms import MembershipForm

admin.site.register(models.Collection)
admin.site.register(models.Card)


class WallMembershipInline(admin.TabularInline):
    model = models.WallMembership
    extra = 1
    form = MembershipForm


@admin.register(models.Wall)
class WallAdmin(admin.ModelAdmin):
    inlines = (WallMembershipInline,)
