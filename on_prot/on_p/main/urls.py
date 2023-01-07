from django.urls import path
from .views import index, trainers
from .models import Armwrestler, Trainer

urlpatterns = [
    path('', index, name='main'),
    path('trainers', trainers, name='trs'),
]

for trainer in Trainer.objects.all():
    urlpatterns += [
        path(trainer.en_view,
             trainers,
             kwargs={'pk': trainer.id})
    ]
