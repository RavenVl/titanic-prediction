from django.shortcuts import render
from .utils import prediction_model


# Create your views here.
def index_titanic(request):
    return render(request, 'titanic/index.html')


def result(request):
    #  pclass, sex, age, sibsp, parch, fare, embarked, title
    pclass = int(request.POST['pclass'])
    sex = int(request.POST['sex'])
    age = int(request.POST['age'])
    sibsp = int(request.POST['sibsp'])
    parch = int(request.POST['parch'])
    fare = int(request.POST['fare'])
    embarked = int(request.POST['embarked'])
    title = int(request.POST['title'])

    context = {
        'prediction': prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
    }
    return render(request, 'titanic/result.html', context)
