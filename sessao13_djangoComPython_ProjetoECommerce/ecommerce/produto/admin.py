from django.contrib import admin
from django.db import models
from .models import Produto, Variacao

class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
