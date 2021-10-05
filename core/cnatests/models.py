from django.db import models
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL

ANSWER_CHOICES = (
  ("A", "A"),
  ("B", "B"),
  ("C", "C"),
  ("D", "D"),
)

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200, blank=False, null=False)
    question_number = models.IntegerField()
    #must add validation to default answer
    correct_answer = models.CharField(max_length=1)
    answer_a = models.CharField(max_length=200)
    answer_b = models.CharField(max_length=200)
    answer_c = models.CharField(max_length=200)
    answer_d = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class TestTaker(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    FirstAttemptLink = models.CharField(max_length=200, null=True)
    SecondAttemptLink = models.CharField(max_length=200, null=True)
    NthAttemptLink = models.CharField(max_length=200, null=True)
    FirstAttemptTimeStamp = models.DateTimeField(auto_now_add=True)
    SecondAttemptTimeStamp = models.DateTimeField(auto_now_add=True)
    NthAttemptTimeStamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)



class TestResponse(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    testTaker = models.ForeignKey(TestTaker, on_delete=models.CASCADE)
    grade = models.IntegerField()
    
class Answer(models.Model):
    testTaker = models.ForeignKey(TestTaker, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test_response = models.ForeignKey(TestResponse, on_delete=models.CASCADE)
    correct = models.BooleanField(blank=True, null=True)
    answer = models.CharField(
        max_length = 1,
        choices = ANSWER_CHOICES,
        null=False,
        default = 'A'
        )

