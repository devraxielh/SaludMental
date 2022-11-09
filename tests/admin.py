from django.contrib import admin
from django.contrib import messages
from .models import Test

admin.site.site_header = "Software de Test de Salud Mental"
admin.site.site_title = "Portal de Test de Salud Mental"
admin.site.index_title = "Bienvenidos al portal de administración"

# Register your models here.

class TestAdmin(admin.ModelAdmin):
  search_fields = ['nombre', 'descripcion']
  list_display = ['nombre', 'descripcion','image_tag']
  list_filter = ['nombre']
  #list_editable = ['nombre']
  #list_display_links = None
  list_per_page: 6
  fields = ['nombre', 'descripcion','upload']
  ordering = ['-nombre',]

def rate_five_stars(modeladmin, request, queryset):
  queryset.update(rating=5.0)
  messages.success(request, "Se calificó con 5 estrellas")

admin.site.add_action(rate_five_stars, "Calificar con 5 estrellas")
admin.site.register(Test, TestAdmin)