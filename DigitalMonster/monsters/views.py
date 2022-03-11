from django.shortcuts import get_object_or_404, render


from .models import *

def index(request):
    latest_baby_list = Baby.objects.all()
    latest_training_list = Training.objects.all()
    latest_rookie_list = Rookie.objects.all()
    latest_champion_list = Champion.objects.all()
    return render(request, "monsters/index.html",{
        "latest_baby_list" : latest_baby_list,
        "latest_training_list" : latest_training_list,
        "latest_rookie_list" : latest_rookie_list,
        "latest_champion_list" : latest_champion_list
    })

def baby(request, baby_id):
    baby = get_object_or_404(Baby, pk= baby_id)
    evolution_list = First.objects.filter(baby= baby)
    
    return render(request, "monsters/baby.html",{
        "baby" : baby,
        "evolution_list" : evolution_list
    })


def training(request, training_id):
    training = get_object_or_404(Training, pk= training_id)
    devolution_list = First.objects.filter(training= training)
    evolution_list = Second.objects.filter(training= training)
    
    return render(request, "monsters/training.html",{
        "training" : training,
        "devolution_list" : devolution_list,
        "evolution_list" : evolution_list
    })


def rookie(request, rookie_id):
    rookie = get_object_or_404(Rookie, pk= rookie_id)
    devolution_list = Second.objects.filter(rookie= rookie)
    evolution_list = Third.objects.filter(rookie= rookie)
    
    return render(request, "monsters/rookie.html",{
        "rookie" : rookie,
        "devolution_list" : devolution_list,
        "evolution_list" : evolution_list
    })


def champion(request, champion_id):
    champion = get_object_or_404(Champion, pk= champion_id)
    devolution_list = Third.objects.filter(champion= champion)
    
    return render(request, "monsters/champion.html",{
        "champion" : champion,
        "devolution_list" : devolution_list
    })