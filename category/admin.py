from django.contrib import admin

from .models import Category, Works, Specialist, ChangeLog


class WorksAdmin(admin.ModelAdmin):

      list_display = ('name', 'specialist_type', 'hours', 'count' )
      fields = ('name', 'specialist_type', 'hours', 'count')


class CategoryAdmin(admin.ModelAdmin):
      list_display = ('name', )
      fields = ('name', )

class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate')
    fields = ('name', 'rate' )
admin.site.register(Works, WorksAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
