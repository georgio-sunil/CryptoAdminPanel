from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.base import TemplateView
from Language.forms import AddLanguageForm
from services import api
from services.models.Language import AddLanguage
from utilities.uploadFile import saveFile

# Create your views here.

class LanguageTable(LoginRequiredMixin, TemplateView):
    template_name = "language/language-table.html"
    success_url = "language/language-table.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if 'disable-language' in self.request.POST:
            print(request.POST)
            toDisable = request.POST.getlist('language-check')
            for id in toDisable:
                if api.languageStatus(id, False):
                    print("Language Disabled")

        elif 'enable-language' in self.request.POST:
            toEnable = request.POST.getlist('language-check')
            for id in toEnable:
                if api.languageStatus(id, True):
                    print("Language Enabled")
        
        elif 'add-language' in self.request.POST:
            form = AddLanguageForm(request.POST or None)
            image_url = saveFile(request.FILES['image_upload'], 'language_images')
            if form.is_valid():
                course = AddLanguage(
                    form.cleaned_data['locale_name'],
                    form.cleaned_data['language_name'],
                    image_url
                )
                if api.addLanguage(course):
                    print("Language Added")
            return HttpResponseRedirect(reverse('language-table'))
        return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, **kwargs):
        language_list = api.fetchLanguages()
        context = {
            "language_list": language_list
        }
        return context
