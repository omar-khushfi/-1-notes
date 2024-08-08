from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
@login_required
def home(request):
    user=request.user
    notes=Note.objects.filter(user=user)
    context={
        'notes':notes,
        }
    
    return render(request,"html/home.html",context)


@method_decorator(login_required,name='dispatch')
class add_note(View):
    def post(self,request):
        title=request.POST["title"]
        content=request.POST["content"]
        user=request.user
        if title!="" and content!="":
            note=Note(title=title,content=content,user=user)
            note.save()
        # return render(request,"html/home.html",context)
        return redirect(reverse('home'))
        

    def get(self,request):
        return render(request,'html/note.html')

@method_decorator(login_required,name='dispatch')
class note(View):
    def post(self,request,pk):
        title=request.POST["title"]
        content=request.POST["content"]
        note=Note.objects.get(pk=pk)
        if title!="" and content!="":
            note.title=title
            note.content=content
            note.save()
        return redirect(reverse('home'))
    def get(self,request,pk):
        note=Note.objects.get(pk=pk)
        return render(request,"html/note.html",{'note':note})
    
@login_required 
def note_delete(request,pk):
        note=Note.objects.get(pk=pk)
        note.delete()
        user=request.user
        notes=Note.objects.filter(user=user)
        context={
        'notes':notes,
        }
        return render(request,"html/home.html",context)
        
        
      
class Register(CreateView):
    template_name='registration/signin.html'
    model=User
    form_class=UserCreationForm
    success_url= reverse_lazy('login') 

    def form_valid(self, form):
        # يتم الحفظ قبل تسجيل الدخول حتى نكون لدينا كائن المستخدم
        response = super().form_valid(form)
        # تسجيل الدخول تلقائيًا للمستخدم
        user = self.object
        login(self.request, user)
        # تحويل إلى صفحة البروفايل (الملف الشخصي)
        return redirect(reverse('home'))

