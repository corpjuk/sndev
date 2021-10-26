from django.shortcuts import render, get_object_or_404

from cnatests.models import Quiz

# Create your views here.
def question_list_view(request):
    # .all is not right here
    # qs = Quiz.objects.filter(user=request.user)
    qs = Quiz.objects.all()
    obj = get_object_or_404(Quiz, title="CNA Assessment")
    context = {
        'object_list': qs,
        'object': obj
    }
    return render(request, "CNA/list.html", context)

def question_detail_view(request):
    obj = get_object_or_404(Quiz, id=id)
    context = {
        'object': obj
    }
    return render(request, "CNA/detail.html", context)

def quiz_view(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Quiz.objects.all()
        score=0
        wrong=0
        blank=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.answer)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'blank':blank,
            'percent':percent,
            'total':total
        }
        return render(request,'CNA/result.html',context)
    else:
        questions=Quiz.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'CNA/assessment.html',context)

def add_question_view(request):
    pass