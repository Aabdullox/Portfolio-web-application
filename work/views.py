from django.shortcuts import render
from contact.forms import ContactForm
from article.models import Article
from teacher.models import Teacher
from work.models import Work

def home(request):
    articles = Article.objects.all()
    teachers = Teacher.objects.all()
    works = Work.objects.all()
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'articles': articles,
        'teachers': teachers,
        'works' : works
    }
    return render(request, "index.html", context=context)
