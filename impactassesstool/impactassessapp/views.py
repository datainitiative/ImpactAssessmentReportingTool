# django imports
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import Group

# Import from general utilities
from util import *

# Import from app
from impactassesstool.settings import ADMIN_ROOT_URL, ROOT_APP_URL, STORAGE_ROOTPATH, STATIC_URL
from impactassessapp.models import *
from impactassessapp.forms import *

'''-----------------------
User functions
-----------------------'''   
# Register
@render_to("impactassessapp/register.html")
def register(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            new_user = signup_form.save()
            user = authenticate(username=signup_form.cleaned_data["username"], password=signup_form.cleaned_data["password2"])
            login(request, user)
            if "next" in request.GET:
                app_name = request.GET["next"].replace(APP_SERVER_URL,"").partition("/")[2].partition("/")[0]
                return HttpResponseRedirect(request.GET["next"])
            else:
                url = request.META["HTTP_REFERER"]
                if url.partition("/?next=/")[1] == "":
                    if APP_SERVER_URL == "":
                        # a trick for localhost
                        app_name = url.partition("http://")[2].replace(SERVER_URL,"").partition("/")[2].partition("/")[0]
                    else:
                        app_name = url.partition("http://")[2].replace(SERVER_URL,"").replace(APP_SERVER_URL,"").partition("/")[2].partition("/")[0]
                else:
                    app_name = url.partition("/?next=/")[2].partition("/")[0]
                return HttpResponseRedirect('%s/admin/%s/investment/' % (ROOT_APP_URL,app_name))            
        else:
            error_msg = "Please check your register information."
            return {'title':"Sign up",'error_msg':error_msg,'signup_form':signup_form}
    else:
        signup_form = UserCreationForm()
    return {'title':"Sign up",'signup_form':signup_form}


# User Profile
@login_required
@render_to("impactassessapp/user_profile.html")
def user_profile(request):
    user = request.user
    if request.method == 'GET':
        user_profile_form = UserProfileForm(instance=user)
    elif request.method == 'POST':
        user_profile_form = UserProfileForm(data=request.POST, instance=user)
        if user_profile_form.is_valid():
            user_profile_form.save()
            messages.info(request, "User profile was changed successfully.")
            if 'save' in request.POST:
                if "next" in request.GET:
                    #app_name = request.GET["next"].replace(APP_SERVER_URL,"").partition("/")[2].partition("/")[0]
                    return HttpResponseRedirect(request.GET["next"])
                else:
                    return HttpResponseRedirect('%s/admin/impactassessapp/investment/' % ADMIN_ROOT_URL)
        else:
            messages.error(request, "Please correct the errors below.")
    return {'user_name':user.username,'user_profile_form':user_profile_form}

# User Change Password
@login_required
@render_to("impactassessapp/user_password.html")
def user_change_password(request):
    user = request.user
    if request.method == 'GET':
        user_password_form = PasswordChangeForm(user)
    elif request.method == 'POST':
        user_password_form = PasswordChangeForm(user,request.POST)
        if user_password_form.is_valid():
            user_password_form.save()
            messages.info(request, "User password was changed successfully.")
            return HttpResponseRedirect('%s/user/profile/' % ROOT_APP_URL)
        else:
            messages.error(request, "Please correct the errors below.")
    return {'user_name':user.username,'user_password_form':user_password_form}

'''-----------------------
Main Functions
-----------------------'''
# Home page
@login_required
@render_to("impactassessapp/home.html")
def home(request):
    print "Home Page"
        
    return {}


# Import data functions
## Import Organization Stage
@login_required
def import_organization_stage(request):
    try:
        with open(STORAGE_ROOTPATH+"ref_organization_stage.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    org_stage = OrganizationStage(
                        name = row[0].strip().title()
                    )
                    org_stage.save()
        return HttpResponse("Organization Stage - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("Organization Stage - Import Failed! Error: %s" % e)

## Import Organization
@login_required
def import_organization(request):
    try:
        with open(STORAGE_ROOTPATH+"table_organization.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    if row[3].strip():
                        print row[3].strip().title()
                        organization_stage = OrganizationStage.objects.get(name = row[3].strip().title())
                    else:
                        organization_stage = None
                    org = Organization(
                        name = row[0].strip().title(),
                        description = row[1].strip(),
                        est_date = int(row[2].strip()) if row[2] else None,                            
                        org_stage = organization_stage,
                        org_stage_note = row[4].strip()
                    )
                    org.save()
        return HttpResponse("Organization - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("Organization - Import Failed! Error: %s" % e)
    
## Import Report Due Type
@login_required
def import_report_due_type(request):
    try:
        with open(STORAGE_ROOTPATH+"ref_report_due_type.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    report_due_type = ReportDueType(
                        name = row[0].strip().title()
                    )
                    report_due_type.save()
        return HttpResponse("Report Due Type - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("Report Due Type - Import Failed! Error: %s" % e)
   
## Import Report Status
@login_required
def import_report_status(request):
    try:
        with open(STORAGE_ROOTPATH+"ref_report_status.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    report_status = ReportStatus(
                        name = row[0].strip().capitalize()
                    )
                    report_status.save()
        return HttpResponse("Report Status - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("Report Status - Import Failed! Error: %s" % e)
    
## Import Investment Cateogry
@login_required
def import_investment_category(request):
    try:
        with open(STORAGE_ROOTPATH+"ref_investment_category.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    investment_category = InvestmentCategory(
                        name = row[0].strip().title()
                    )
                    investment_category.save()
        return HttpResponse("Investment Cateogry - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("Investment Cateogry - Import Failed! Error: %s" % e)

## Import Investment Type
@login_required
def import_investment_type(request):
    try:
        with open(STORAGE_ROOTPATH+"ref_investment_type.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    category = InvestmentCategory.objects.get(name = row[0].strip().title())
                    report_status = InvestmentType(
                        name = row[1].strip().capitalize(),
                        category = category
                    )
                    report_status.save()
        return HttpResponse("Investment Type - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("Investment Type - Import Failed! Error: %s" % e)
    
## Import Geography
@login_required
def import_geography(request):
    try:
        with open(STORAGE_ROOTPATH+"ref_geography.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    geography = Geography(
                        name = row[0].strip().title()
                    )
                    geography.save()
        return HttpResponse("Geography - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("Geography - Import Failed! Error: %s" % e)

## Thematic Area
@login_required
def import_thematic_area(request):
    try:
        with open(STORAGE_ROOTPATH+"ref_thematic_area.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    thematic_area = ThematicArea(
                        name = row[0].strip().title()
                    )
                    thematic_area.save()
        return HttpResponse("Thematic Area - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("Thematic Area - Import Failed! Error: %s" % e)

## M&E Capacity
@login_required
def import_me_capacity(request):
    try:
        with open(STORAGE_ROOTPATH+"ref_me_capacity.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    me_capacity = MECapacity(
                        name = row[0].strip().title()
                    )
                    me_capacity.save()
        return HttpResponse("M&E Capacity - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("TM&E Capacity - Import Failed! Error: %s" % e)


## Is Indicator Met
@login_required
def import_is_indicator_met(request):
    try:
        with open(STORAGE_ROOTPATH+"ref_is_indicator_met.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    is_indicator_met = IsIndicatorMet(
                        name = row[0].strip().capitalize()
                    )
                    is_indicator_met.save()
        return HttpResponse("Is Indicator Met - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("Is Indicator Met - Import Failed! Error: %s" % e)
    
## Investment
@login_required
def import_investment(request):
    try:
        with open(STORAGE_ROOTPATH+"table_investment.csv",'rb') as f:
            reader = csv.reader(f)
            for index,row in enumerate(reader):
                if index > 0:
                    organization = Organization.objects.get(name=row[0].strip().title())
                    date_of_award = datetime.datetime.strptime(row[1].strip(),'%m/%d/%Y') if row[1].strip() else None
                    report_due_dates = row[2].strip().split("; ") if row[2].strip() else None
                    report_status = ReportStatus.objects.get(name=row[3].strip().capitalize()) if row[3].strip() else None
                    amount = int(row[4].strip())
                    amount_note = row[5].strip()
                    investment_types = row[6].strip().split("; ") if row[6].strip() else None
                    geography = Geography.objects.get(name=row[7].strip().title()) if row[7].strip() else None
                    geography_note = row[8].strip()
                    thematic_area = ThematicArea.objects.get(name=row[9].strip().title()) if row[9].strip() else None
                    cost_effectiveness = row[10].strip()
                    beneficiary_level_indicator = row[11].strip()
                    organization_level_indicator = row[12].strip()
                    me_capacity = MECapacity.objects.get(name=row[13].strip().title()) if row[13].strip() else None
                    me_capacity_note = row[14].strip()
                    is_indicator_met = IsIndicatorMet.objects.get(name=row[15].strip().capitalize()) if row[15].strip() else None
                    recommended_indicator = row[16].strip()
                    notes = row[17].strip()                
                    
                    investment = Investment(
                        organization = organization,
                        date_of_award = date_of_award,
                        report_status = report_status,
                        amount = amount,
                        amount_note = amount_note,
                        geography = geography,
                        geography_note = geography_note,
                        thematic_area = thematic_area,
                        cost_effectiveness = cost_effectiveness,
                        beneficiary_level_indicator = beneficiary_level_indicator,
                        organization_level_indicator = organization_level_indicator,
                        me_capacity = me_capacity,
                        me_capacity_note = me_capacity_note,
                        is_indicator_met = is_indicator_met,
                        recommended_indicator = recommended_indicator,
                        notes = notes
                    )
                    
                    investment.save() 
                    
                    # add many to many relationships
                    ## Report due date
                    if report_due_dates:
                        for str_rdd in report_due_dates:
                            rdd_date = str_rdd.split(' (')[0]
                            rdd_type = str_rdd.split(' (')[1][:-1].strip().title()
                            report_due_date = ReportDueDate(
                                date = datetime.datetime.strptime(rdd_date,'%m/%d/%Y'),
                                report_due_type = ReportDueType.objects.get(name=rdd_type)
                            )
                            report_due_date.save()
                            investment.report_due_date.add(report_due_date)
                            investment.save()
                    ## Investment type
                    if investment_types:
                        for str_it in investment_types:
                            it_category = str_it.split(': ')[0].strip().title()
                            it_name = str_it.split(': ')[1].replace(".","")
                            investment_type = InvestmentType(
                                name = it_name,
                                category = InvestmentCategory.objects.get(name=it_category)
                            )
                            investment_type.save()
                            investment.investment_type.add(investment_type)
                            investment.save()

        return HttpResponse("Investments - Import complete!")
    except Exception as e:
        print e
        return HttpResponse("Investments - Import Failed! Error: %s" % e)