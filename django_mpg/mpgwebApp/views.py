from django.shortcuts import render
from django.http import HttpResponse

import joblib #ML load
reloadModel = joblib.load('./models/RFModelforMPG.pkl')

import pandas as pd # pandas 읽기

# Create your views here.
def index(request):
    context = {'a':"Hello World!"}
    return render(request, 'index.html', context)
    #return HttpResponse({'a':1})  # a 출력

def predictMPG(request):
    print(request)
    if request.method == 'POST':
        print(request.POST.dict())
        temp = {}
        temp['cylinders'] = request.POST.get('cylinderVal')
        temp['displacement'] = request.POST.get('dispVal')
        temp['horsepower'] = request.POST.get('hrsPwrVal')
        temp['weight'] = request.POST.get('weightVal')
        temp['acceleration'] = request.POST.get('accVal')
        temp['model_year'] = request.POST.get('modelVal')
        temp['origin'] = request.POST.get('originVal')

    testDtaa = pd.DataFrame({'x':temp}).transpose()
    scoreval = reloadModel.predict(testDtaa)[0]

    context = {'scoreval': scoreval}
    return render(request, 'index.html', context)
