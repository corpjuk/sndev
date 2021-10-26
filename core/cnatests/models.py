from django.db import models
from django.urls import reverse
from django.conf import settings
import uuid
# from .utils import calc_number
 
User = settings.AUTH_USER_MODEL
# Create your models here.


answers = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D")
)

# Django Docs for UUID Field
# Note that a callable (with the parentheses omitted) is passed to default, not an instance of UUID.
# https://docs.djangoproject.com/en/3.2/ref/models/fields/#uuidfield
# 
# Lookups on PostgreSQL
# Using iexact, contains, icontains, startswith, istartswith, endswith, or iendswith 
# lookups on PostgreSQL don’t work for values without hyphens, 
# because PostgreSQL stores them in a hyphenated uuid datatype type.

class Person(models.Model):
    
    email = models.CharField(max_length=100,null=True,blank=True,unique=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.email
    

class Quiz(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("CNA:detail", kwargs={"id": self.id })
    # def get_questions_children(self):
    #     return self.question_set.all()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'quiz'
        verbose_name_plural = 'quizzes'



class QuizRequest(models.Model):
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

class QuizResponse(models.Model):
    key = models.ForeignKey(QuizRequest, on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Question(models.Model):
    # related_name="questions"
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200, blank=False, null=False)
    question_number = models.IntegerField(null=False, blank=False, unique=True)
    #must add validation to default answer
    correct_answer = models.CharField(choices=answers, max_length=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.initial['question_number'] = calc_question_number

    def get_answers_children(self):
        # return self.answers
        return self.answers.all()

    def __str__(self):
         return f"Question {self.question_number}"

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'
        ordering = ['question_number']

class Answer(models.Model):
    #related_name="answers"
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    answer = models.CharField(choices=answers, max_length=50)
    answer_text = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'
        unique_together = [
            ("question", "answer"),
        ]

# class QuizTakerModel(models.Model):
#     user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
#     name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     FirstAttemptLink = models.CharField(max_length=200, null=True)
#     SecondAttemptLink = models.CharField(max_length=200, null=True)
#     NthAttemptLink = models.CharField(max_length=200, null=True)
#     FirstAttemptTimeStamp = models.DateTimeField(auto_now_add=True)
#     SecondAttemptTimeStamp = models.DateTimeField(auto_now_add=True)
#     NthAttemptTimeStamp = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now_add=True)

    # question = models.TextField(null=True)
    # optionA = models.CharField(max_length=200,null=True)
    # optionB = models.CharField(max_length=200,null=True)
    # optionC = models.CharField(max_length=200,null=True)
    # optionD = models.CharField(max_length=200,null=True)
    # answer = models.CharField(max_length=200,null=True)

    # we don't need these in the QuizModel
    # score = models.IntegerField(MinValueValidator=0, MaxValueValidator=67)
    # score_as_float = models.DecimalField(max_digits=None, decimal_places=None)
    
    # def get_absolute_url(self):
    #     return reverse("CNA:detail", kwargs={"id": self.id })
    # def get_edit_url(self):
    #     return reverse("CNA:update", kwargs={"id": self.id})
