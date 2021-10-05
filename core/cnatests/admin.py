from django.contrib import admin
from django.contrib.auth import  get_user_model
from .models import Test, Question, TestTaker, TestResponse, Answer
# Register your models here.

User = get_user_model()

class QuestionInLines(admin.StackedInline):
    model = Question
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    # inlines = [QuestionInLine]
    list_display = ['test', 'question_number']
    readonly_fields = ['timestamp', 'updated']

class TestAdmin(admin.ModelAdmin):
    inlines = [QuestionInLines]
    list_display = ['title']

admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
