from django.contrib import admin
from .models import ExamStructure, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'text', 'answer')
    list_display_links = ('id', 'text')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(ExamStructure)
class ExamStructureAdmin(admin.ModelAdmin):
    list_display = ('certification', 'version', 'num_questions', 'total_points', 'passing_score', 'minutes', 'minutes_extended')
