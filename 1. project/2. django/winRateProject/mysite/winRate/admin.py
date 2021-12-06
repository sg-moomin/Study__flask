from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    # search_fields : 검색조건
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)

# Register your models here.
