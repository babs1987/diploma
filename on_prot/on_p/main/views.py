from pprint import pprint

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView

from .models import Armwrestler,Trainer
from .forms import TrainerForm

# Create your views here.




def index(request):
    if request.method == 'GET':
        return render(request, 'main/index.html', {"trs": Trainer.objects.all(), 'form': TrainerForm()})
    elif request.method=='POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            pprint(form.cleaned_data)
            ff=form.cleaned_data


            # new_trainer=Trainer(
            #     first_name=ff["first_name"],
            #     last_name=ff["last_name"],
            #     team=ff["team"],
            #     #students=ff['students']
            #)


            new_trainer=Trainer.objects.create(first_name=ff["first_name"],last_name=ff["last_name"],team=ff["team"])
            print("*******")
            print(type(ff['students']))
            new_trainer.students.set(ff['students'][0])

            # new_trainer.add(ff['students'])

            new_trainer.save()
            return HttpResponseRedirect(request.path)



def trainers(request,pk:int):
    return render(request, 'main/sportsmens.html', {"trainer": Trainer.objects.get(pk=pk)})

