from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CsvDataForm
from csvsite import csvdoc
import csv
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from .models import CsvData
# Create your views here.
@login_required
def editcsv(request):
    #datacsv is a dict and defines fields of csv automatically that icludes csv datas
    datacsv=csvdoc.CSVFILE().display('static/spots.csv')
    count=len(datacsv['adres'])
    #formset have forms as value of counto
    CsvDataFormSet=formset_factory(CsvDataForm,extra=count)
    if request.POST:
        dlist=[['adres','durum','hedef adres','zaman'],]
        for i in range(0,count):
            dlist.append([])
        formset=CsvDataFormSet(request.POST)
        for i in range(1,count+1):
            #dlist's first element has a list which has field names of csv document.
            dlist[i].append(request.POST.get("form-" + str(i-1)+"-adres"))
            dlist[i].append(request.POST.get("form-" + str(i-1)+"-durum"))
            dlist[i].append(request.POST.get("form-" + str(i-1)+"-hedef_adres"))
            dlist[i].append(request.POST.get("form-" + str(i-1)+"-zaman"))
        with open('/static/spots.csv',"w") as fw:
            writer=csv.writer(fw, delimiter=",",quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(dlist)
    else:
        formset=CsvDataFormSet()
        #create formset datas
        for i in range(0,count):
            formset[i].fields['adres'].initial=str(datacsv['adres'][i])
            formset[i].fields['durum'].initial=str(datacsv['durum'][i])
            formset[i].fields['hedef_adres'].initial=str(datacsv['hedef adres'][i])
            formset[i].fields['zaman'].initial=str(datacsv['zaman'][i])
            #show a page have url which is csvsite/editcsv page.
    return render(request,"editcsvhome.html",{"formset":formset})
