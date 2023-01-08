from pprint import pprint

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView

from .models import Armwrestler,Trainer
from .forms import TrainerForm

# Create your views here.



def list_of_trainers(request):
    return render(request,'main/trainers.html',{
        "trs": Trainer.objects.all()
    })

def index(request):
    if request.method == 'GET':
        return render(request, 'main/index.html', {
            'form': TrainerForm(),
                      })
    elif request.method=='POST':
        form = TrainerForm(request.POST)

        if form.is_valid():
            ff=form.cleaned_data
            print(ff)
            new_trainer=Trainer(
                first_name=ff["first_name"],
                last_name=ff["last_name"],
                team=ff["team"],
                #students=ff['students']
            )
            new_trainer.save()
            for stud in ff['students']:
                new_trainer.students.add(stud)
                new_trainer.save()

        print(request.path)
        return HttpResponseRedirect(request.path)



def trainers(request,pk:int):
    return render(request, 'main/sportsmens.html', {"trainer": Trainer.objects.get(pk=pk)})

