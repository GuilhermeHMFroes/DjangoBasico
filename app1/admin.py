from django.contrib import admin

from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','estoque')
    search_fields = ('nome',)

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente)

# Register your models here.
