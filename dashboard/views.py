from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from .filters import QuestionFilter
from django.core.paginator import Paginator, PageNotAnInteger


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
     
        return redirect('questions')  


    return render(request, 'cadastrar.html')


def questions(request):
    questions = Question.objects.all().order_by('-id')
    paginator = Paginator(questions, 5)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'question_list.html', {'questions': questions})
    
    
def question_edit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        question.question_text = request.POST.get('question')
        question.answer_text = request.POST.get('answer')
        question.save()
        return redirect('questions')
    return render(request, 'question_edit.html', {'question': question})
    
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        question.delete()
        return redirect('questions')