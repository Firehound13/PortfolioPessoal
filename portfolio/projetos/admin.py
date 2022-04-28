from django.contrib import admin
from .models import Projeto

# Register your models here.
class ListandoProjetos(admin.ModelAdmin):
    """
    Classe para mudar o layout da listagem de projetos
    """
    list_display = ('id', 'nome_projeto', 'linguagem')
    list_display_links = ('id', 'nome_projeto')
    search_fields = ('nome_projeto', 'detalhes_projeto')
    list_filter = ('cliente',)
    list_per_page = 1

admin.site.register(Projeto, ListandoProjetos)
