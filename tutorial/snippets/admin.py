from django.contrib import admin

# Register your models here.

from .models import Snippet

def getFieldsModel(model):
    return [field.name for field in model._meta.get_fields()]

class SnippetAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(Snippet)

admin.site.register(Snippet, SnippetAdmin)