from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import cardioVascularForm

import pickle

# Create your views here.



def getDataAndPredict(request):
    if request.method=='POST':
        form=cardioVascularForm(request.POST)
        temp=[]
        dict={}
        for x in request.POST:
            print(request.POST[x])
            dict[x]=request.POST[x]
            temp.append(request.POST[x])

        temp.pop(0)
        test_data=[]
        test_data.append(temp)
        print(test_data)
       
        filename = 'core/model.pkl'
        model = pickle.load(open(filename, 'rb'))
        my_prediction = model.predict(test_data)
        context={
            'form':form ,
            'my_prediction':my_prediction[0],
        }

        return render(request,'core/index.html',context)
    else:
        form=cardioVascularForm()
         
    context={'form':form }
     
    return render(request,'core/index.html',context)

