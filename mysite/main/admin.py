from django.contrib import admin
from.models import Refeicoe, Comida, CustomUser
from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import admin

class CustomUserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'balance', 'marcacoes')
    search_fields = ('email', 'username')

    filter_horizontal = ()
    list_filter = ('email', 'username')
    fieldsets = ()

admin.site.site_header = "Administração"

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Comida)
admin.site.register(Refeicoe)

