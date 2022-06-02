from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib import messages
from Language.forms import AddLanguageForm, UpdateLanguageForm
from services import api
from services.models.Language import AddLanguage, updateLanguage
from utilities.uploadFile import saveFile, saveUniqueFile

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
                    messages.success(self.request, "Language Disabled")
                    print("Language Disabled")

        elif 'enable-language' in self.request.POST:
            toEnable = request.POST.getlist('language-check')
            for id in toEnable:
                if api.languageStatus(id, True):
                    messages.success(self.request, "Language Enabled")
                    print("Language Enabled")
        
        elif 'add-language' in self.request.POST:
            form = AddLanguageForm(request.POST or None)
            image_url = saveFile(request.FILES['image_upload'], 'language_images')
            language_file_url = saveUniqueFile(request.FILES['language_file'], 'language_file')
            if form.is_valid():
                language = AddLanguage(
                    form.cleaned_data['locale_name'],
                    form.cleaned_data['language_name'],
                    image_url,
                    language_file_url
                )
                if api.addLanguage(language):
                    messages.success(self.request, "Language added")
                    print("Language Added")
        return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, **kwargs):
        language_list = api.fetchLanguages()
        context = {
            "language_list": language_list
        }
        return context

class UpdateLanguage(LoginRequiredMixin, TemplateView):
    template_name = "language/update-language.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('language-table')

    def get_context_data(self, **kwargs):
        languageID = str(self.kwargs['pk'])
        language_list = api.fetchSingleLanguage(languageID)
        context = {
            "language": language_list
        }
        return context

    def post(self, request, *args, **kwargs):
        languageID = str(self.kwargs['pk'])
        form = UpdateLanguageForm(request.POST or None)

        if 'image_upload' in request.FILES:
            image_url = saveFile(request.FILES['image_upload'], 'language_images')
        else:
            image_url = request.POST['image_upload']

        if 'language_file' in request.FILES:
            language_file_url = saveUniqueFile(request.FILES['language_file'], 'language_file')
        else:
            language_file_url = request.POST['language_file']
        
        if form.is_valid():
            language = updateLanguage(
                form.cleaned_data['locale_name'],
                form.cleaned_data['language_name'],
                image_url,
                language_file_url
                )
            if api.updateLanguage(languageID, language):
                return HttpResponseRedirect(reverse('language-table'))

        return HttpResponseRedirect(self.request.path_info)