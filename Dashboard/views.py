from django.shortcuts import render
from django.views.generic.base import TemplateView
from Dashboard.forms import LoginModelForm
from django.contrib.auth import login, authenticate


# Create your views here.


def dashboard(request):
    return render(request, 'index.html')

class Boxed(TemplateView):
    template_name = "layout/vertical/layouts-boxed.html"


class CompactSidebar(TemplateView):
    template_name = "layout/vertical/layouts-compact-sidebar.html"


class IconSidebar(TemplateView):
    template_name = "layout/vertical/layouts-icon-sidebar.html"


class Lightsidebar(TemplateView):
    template_name = "layout/vertical/layouts-light-sidebar.html"

def loginPage(request):
    form = LoginModelForm(request.POST or None)
    if form.is_valid():
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['userpassword'],
        )
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        # #print(form['username'].value())
        # response = authAPI.loginAPI(form)
        # if response.status_code == 200:
    else:
        print(form.errors)
    context = {'form': form, }
    return render(request, 'login.html', context)