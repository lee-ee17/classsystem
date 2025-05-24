from django.contrib import admin
from .models import Question      # ← 導入 Question

@admin.register(Question)         # ← 註冊到 Admin
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('key', 'text', 'tag')