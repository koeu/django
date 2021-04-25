from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import sklearn

# ML 부르기
import joblib
import pandas as pd
modelReload=joblib.load('./models/my_model11.pkl')
modelReload22=joblib.load('./models/my_model22.pkl')
##########################################################################################################


#######################################################################################

def index(request):
    temp = {}
    temp['passengerID'] = 1233243
    temp['Pclass'] =3
    temp['Name'] = 'Jack'
    temp['Sex'] = 'male'
    temp['Age'] = 34.5
    temp['SibSp'] = 0
    temp['Parch'] = 0
    temp['ticket'] = 'PC 142352'
    temp['Fare'] = 7.8292
    temp['Cabin'] = 'NaN'
    temp['Embarked']= 'Q'
    context={'temp':temp}
    return render(request, 'index.html', context)
#######################################################################################


def predictsurvived(request):
    print(request)
    if request.method == "POST":
        temp = {}
        temp['passengerID'] = request.POST.get('passengeridval')
        temp['Pclass'] = request.POST.get('pclassval')
        temp['Name'] = request.POST.get('nameval')
        temp['Sex'] = request.POST.get('sexval')
        temp['Age'] = request.POST.get('ageval')
        temp['SibSp'] = request.POST.get('sibspval')
        temp['Parch'] = request.POST.get('parchval')
        temp['ticket'] = request.POST.get('ticketval')
        temp['Fare'] = request.POST.get('farval')
        temp['Cabin'] = request.POST.get('cabinval')
        temp['Embarked']= request.POST.get('embarkedval')

        testDtaa = pd.DataFrame({'x':temp}).transpose()
        #X_test = modelReload22.transform(testDtaa)
        scoreval = modelReload22.transform(testDtaa)


    #scoreval = modelReload.predict(X_test)[0]
    #coreval = scoreval.reshape(-1, 1)

    context = {'scoreval': scoreval}
    return render(request, 'index.html', context)
