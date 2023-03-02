from django.contrib import admin

# Register your models here.
from .models import *

class design_admin(admin.ModelAdmin):
    list_display=('company', 'email','file')

class prototype_admin(admin.ModelAdmin):
    list_display=('company', 'email','file')

class styling_admin(admin.ModelAdmin):
    list_display=('company', 'email','file')

class cae_admin(admin.ModelAdmin):
    list_display=('company', 'email','file')

admin.site.register(Styling, styling_admin)
admin.site.register(Design,design_admin)
admin.site.register(Prototype, prototype_admin)
admin.site.register(CAE, cae_admin)


