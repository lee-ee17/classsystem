# recommend/views.py
from django.shortcuts import render, redirect
from .models import Question

def quiz_view(request):
    # 直接取出所有题，按 id 排序
    questions = Question.objects.all().order_by('id')
    return render(request, 'recommend/quiz.html', {
        'questions': questions
    })

def result_view(request):
    # 只接受 POST，非 POST 就重定向回 quiz
    if request.method != 'POST':
        return redirect('recommend:quiz')

    # 简单把表单答案抽出来（csrfmiddlewaretoken 会被忽略）
    answers = {k: v for k, v in request.POST.items() if k != 'csrfmiddlewaretoken'}

    # 把答案传给 recommend/result.html
    return render(request, 'recommend/result.html', {
        'answers': answers
    })
