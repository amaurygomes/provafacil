from django.shortcuts import render, redirect
from .models import Question
from .filters import QuestionFilter


def index(request):
    filtro = None
    if 'q' in request.GET:
        filtro = QuestionFilter(request.GET, queryset=Question.objects.filter(question_text__icontains=request.GET['q']))

    return render(request, 'index.html', {'filtro': filtro})


def cadastrar(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')        
       
        Question.objects.create(question_text=question, answer_text=answer)              
     
        return redirect('lista')  


    return render(request, 'cadastrar.html')

def lista(request):
   
    return render(request, 'lista.html')