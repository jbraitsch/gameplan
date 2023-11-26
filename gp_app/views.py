from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Business, NHLTeam
from .forms import BusinessForm, CreateUserForm
from django.contrib.auth.models import Group, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def indexCity(request, city):
    businesses_in_city = Business.objects.filter(city = city)
    context = {'businesses_in_city':businesses_in_city}
    context["city"] = city
    print("Businesses near you", businesses_in_city)
    return render( request, 'gp_app/index_city.html', context)

def index(request):
    #all_cities = City.objects.filter()
    CITIES = (' ','Colorado Springs','Denver', 'Fort Collins')
    return render(request, 'gp_app/index.html', {'cities': CITIES})

class BusinessListView(generic.ListView):
    model = Business

class BusinessDetailView(LoginRequiredMixin, generic.DetailView):
    model = Business

def deleteBusiness(request, business_id):
    business = Business.objects.get(id=business_id)
    context = {'business': business}
    if request.method == 'GET':
        return render(request, 'gp_app/business_delete.html',context)       
    elif request.method == 'POST':
        business.delete()
        return redirect('index_city', business.city)

@login_required(login_url='login')
@allowed_users(allowed_roles=['business_role'])    
def createBusiness(request):
    form = BusinessForm()
    #business = Business.objects.get(pk=business_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        business_data = request.POST.copy()
        #business_data['business_id'] = business_id
        
        form = BusinessForm(business_data)
        if form.is_valid():
            # Save the form without committing to the database
            business = form.save(commit=False)
            # Set the portfolio relationship
            business.save()

            # Redirect back to the portfolio detail page
            return redirect('business-detail', business.id)

    context = {'form': form}
    return render(request, 'gp_app/business_form.html', context)

def updateBusiness(request, business_id):
    business = Business.objects.get(id=business_id)
    #student = Customer.objects.get(portfolio_id=portfolio_id)
    form = BusinessForm(instance=business)
    
    if request.method == 'POST':
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            business.save()

            # Redirect back to the business detail page
            return redirect('business-detail', business_id)
    else:
        context = {'form': form}
        return render(request, 'gp_app/business_form.html', context) 


def listNHLTeams(request):
    teams = NHLTeam.objects.all()
    context = {'teams': teams}
    return render(request, 'gp_app/nhl_teams_list.html', context)


def NHLTeamDetails(request, team_id):
    team = NHLTeam.objects.get(id=team_id)
    abbrev = team.get_team_abbrev()
    schedule = team.get_week_schedule(abbrev)
    return render(request, 'gp_app/nhl_team_detail.html', {"schedule":schedule, "team":team})

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get_or_create(name='user')
            (gtype, btype) = group
            user.groups.add(gtype.id)
            user.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


