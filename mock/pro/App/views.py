from django.shortcuts import render,redirect
from .forms import studentform
from .models import student
# Create your views here.
def home(request):
    students=student.objects.all()
    return render(request,'home.html')
def Student_details(request):
    if request.method=='POST':
        form =studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')
    else:
        form=studentform()
    return render(request,'student.html',{'form':form})
