from django.shortcuts import render
from placement.models import *
import pandas as pd


# Create your views here.


def index(request):
    context = {}

    try:
        year_no = list(PresentYear.objects.all())[0]
        database = CompanyDatabase.objects.filter(year=year_no.year)
    except:
        PresentYear.objects.create(year=2020)
        year_no = 2020
        database = CompanyDatabase.objects.filter(year=year)

    

    name=[]
    ctc=[]
    cgpa=[]
    base=[]
    opendream=[]
    total_offers = []

    for d in database:
        name.append(d.name)
        ctc.append(d.ctc)
        cgpa.append(d.cgpa)
        base.append(d.base)
        opendream.append(d.open_dream)
        if int(d.total_offers) != -1:
            total_offers.append(int(d.total_offers))


    context = {
                "name":name,
                "ctc":ctc,
                "cgpa":cgpa,
                "base":base,
                "opendream":opendream,
                "company" :database,
                "max_offers": sum(total_offers),
                "year_no":year_no.year

    }
    return render(request, "placement/index.html",context)

##################################################################################################################
def refresh(request):
    context ={}

    ########################

    existing_database = CompanyDatabase.objects.all()
    all_names = []
    all_years = []
    for x in existing_database:
        all_names.append(x.name)
        all_years.append(x.year)

    #############################
    df = pd.read_excel ("placement/static/placement/placementsdata.xlsx")
    company_name = df["company_name"]
    cgpa_cutoff = df["cgpa_cutoff"]
    ctc=df["ctc"]
    base=df["base"]
    total_offers = df["total_offers"]
    open_dream = df["open_dream"]
    year=df["year"]


    total_fields = len(company_name)
    for i in range(total_fields):
        if company_name[i] not in all_names:
            CompanyDatabase.objects.create(name=company_name[i],
                                    ctc=ctc[i],
                                    cgpa=cgpa_cutoff[i],
                                    base=base[i],
                                    total_offers=total_offers[i],
                                    open_dream=open_dream[i],
                                    year=year[i])
        elif company_name[i] in all_names:
            companyobj = CompanyDatabase.objects.filter(name=company_name[i])
            years = []
            for c in companyobj:
                years.append(c.year)

            if year[i] not in years:
                CompanyDatabase.objects.create(name=company_name[i],
                                        ctc=ctc[i],
                                        cgpa=cgpa_cutoff[i],
                                        base=base[i],
                                        total_offers=total_offers[i],
                                        open_dream=open_dream[i],
                                        year=year[i])
            else:
                pass
        else:
            pass


    ##########################################
    try:
        year_no = list(PresentYear.objects.all())[0]
    except:
        PresentYear.objects.create(year=2020)

    database = CompanyDatabase.objects.filter(year=year_no.year)

    name=[]
    ctc=[]
    cgpa=[]
    base=[]
    opendream=[]
    total_offers = []

    for d in database:
        name.append(d.name)
        ctc.append(d.ctc)
        cgpa.append(d.cgpa)
        base.append(d.base)
        opendream.append(d.open_dream)
        if int(d.total_offers) != -1:
            total_offers.append(int(d.total_offers))


    context = {
                "name":name,
                "ctc":ctc,
                "cgpa":cgpa,
                "base":base,
                "opendream":opendream,
                "company" :database,
                "max_offers": sum(total_offers),
                "year_no":year_no.year

    }
    return render(request, "placement/index.html",context)


##################################################################################################################

def highestctc(request):
    context={}


    year_no = list(PresentYear.objects.all())[0]
    database = CompanyDatabase.objects.order_by("-ctc").filter(year=year_no.year)

    name=[]
    ctc=[]
    cgpa=[]
    base=[]
    opendream=[]
    total_offers = []

    for d in database:
        name.append(d.name)
        ctc.append(d.ctc)
        cgpa.append(d.cgpa)
        base.append(d.base)
        opendream.append(d.open_dream)
        if int(d.total_offers) != -1:
            total_offers.append(int(d.total_offers))


    context = {
                "name":name,
                "ctc":ctc,
                "cgpa":cgpa,
                "base":base,
                "opendream":opendream,
                "company" :database,
                "max_offers": sum(total_offers),
                "year_no":year_no.year
    }

    return render(request, "placement/ctc.html",context)
##################################################################################################################
def highestbase(request):
    context={}

    ##########################################
    year_no = list(PresentYear.objects.all())[0]
    database = CompanyDatabase.objects.order_by("-base").filter(year=year_no.year)
    name=[]
    ctc=[]
    cgpa=[]
    base=[]
    opendream=[]
    total_offers = []

    for d in database:
        name.append(d.name)
        ctc.append(d.ctc)
        cgpa.append(d.cgpa)
        base.append(d.base)
        opendream.append(d.open_dream)
        if int(d.total_offers) != -1:
            total_offers.append(int(d.total_offers))


    context = {
                "name":name,
                "ctc":ctc,
                "cgpa":cgpa,
                "base":base,
                "opendream":opendream,
                "company" :database,
                "max_offers": sum(total_offers),
                "year_no":year_no.year

    }

    return render(request, "placement/basep.html",context)
##################################################################################################################
def highestoffers(request):
    context={}

    ##########################################
    year_no = list(PresentYear.objects.all())[0]
    database = CompanyDatabase.objects.order_by("-total_offers").filter(year=year_no.year)
    name=[]
    ctc=[]
    cgpa=[]
    base=[]
    opendream=[]
    total_offers = []

    for d in database:
        name.append(d.name)
        ctc.append(d.ctc)
        cgpa.append(d.cgpa)
        base.append(d.base)
        opendream.append(d.open_dream)
        if int(d.total_offers) != -1:
            total_offers.append(int(d.total_offers))

    context = {
                "name":name,
                "ctc":ctc,
                "cgpa":cgpa,
                "base":base,
                "opendream":opendream,
                "company" :database,
                "max_offers": sum(total_offers),
                "year_no":year_no.year

    }


    return render(request, "placement/offers.html",context)
##################################################################################################################
def cgpa(request):
    context={}

    ##########################################
    year_no = list(PresentYear.objects.all())[0]
    database = CompanyDatabase.objects.order_by("-cgpa").filter(year=year_no.year)

    name=[]
    ctc=[]
    cgpa=[]
    base=[]
    opendream=[]
    total_offers = []

    for d in database:
        name.append(d.name)
        ctc.append(d.ctc)
        cgpa.append(d.cgpa)
        base.append(d.base)
        opendream.append(d.open_dream)
        if int(d.total_offers) != -1:
            total_offers.append(int(d.total_offers))


    context = {
                "name":name,
                "ctc":ctc,
                "cgpa":cgpa,
                "base":base,
                "opendream":opendream,
                "company" :database,
                "max_offers": sum(total_offers),
                "year_no":year_no.year

    }

    return render(request, "placement/cgpa.html",context)
##################################################################################################################


def change_year(request):

    context = {}

    year_no = list(PresentYear.objects.all())[0]

    if request.method == "POST":
        yearno = request.POST["yearno"]
        if yearno == 0:
            yearno = 2020
        year_no.year = yearno
        year_no.save()

    database = CompanyDatabase.objects.filter(year=year_no.year)

    name=[]
    ctc=[]
    cgpa=[]
    base=[]
    opendream=[]
    total_offers = []

    for d in database:
        name.append(d.name)
        ctc.append(d.ctc)
        cgpa.append(d.cgpa)
        base.append(d.base)
        opendream.append(d.open_dream)
        if int(d.total_offers) != -1:
            total_offers.append(int(d.total_offers))


    context = {
                "name":name,
                "ctc":ctc,
                "cgpa":cgpa,
                "base":base,
                "opendream":opendream,
                "company" :database,
                "max_offers": sum(total_offers),
                "year_no":year_no.year

    }


    return render(request, "placement/index.html",context)
