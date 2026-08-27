from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'text', 'answer')
    list_display_links = ('id', 'text')
    list_editable = ('order',)
    ordering = ('order',)
