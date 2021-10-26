from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Quiz, Question, Answer, Person, QuizRequest, QuizResponse

# Register your models here.
# refs
# readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']
# fields = ['name', 'quantity', 'unit', 'directions',]
# readonly_fields = ['timestamp', 'updated']
# raw_id_fields = ['user']
# search_fields = ['name', 'description', ]

User = get_user_model()

def calc_number():
  try:
    num = Question.objects.latest('created_date')
  except Question.DoesNotExist:
    return 0
  return num.question_number + 1

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0
    fields = ['answer', 'answer_text']


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0
    

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'answer', 'id', 'get_question_number', 'get_question_text']

    def get_question_text(self, obj):
        return obj.question.question_text
    get_question_text.short_description = 'Question Text'
    def get_question_number(self, obj):
        return obj.question.question_number
    get_question_number.short_description = 'Question Number'
    
    
    # def get_question_id(self, obj):
    #     return obj.question.question_id
    # get_question_id.admin_order_field = 'question_id'
    # get_question_number.short_description = 'Question Number'

    def get_ordering(self, request):
        return ['question_id', 'id']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['question_number', 'question_text', 'correct_answer', 'quiz']

    def get_changeform_initial_data(self, request):
        return {"question_number": calc_number}

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

class PersonAdmin(admin.ModelAdmin):
    model = Person

class QuizRequestAdmin(admin.ModelAdmin):
    model = QuizRequest

class QuizResponseAdmin(admin.ModelAdmin):
    model = QuizResponse

admin.site.register(QuizResponse, QuizResponseAdmin)
admin.site.register(QuizRequest, QuizRequestAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
 
# Register your models here.