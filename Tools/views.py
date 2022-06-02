from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib import messages
from Language.forms import AddLanguageForm, UpdateLanguageForm
from Tools.forms import AddBannersForm
from services import api
from services.models.Banners import AddBanners
from utilities.uploadFile import saveFile, saveUniqueFile

class BannerTable(LoginRequiredMixin, TemplateView):
    template_name = "tools/banner.html"
    success_url = "tools/banner.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if 'disable-banner' in self.request.POST:
            print(request.POST)
            toDisable = request.POST.getlist('banner-check')
            for id in toDisable:
                if api.bannerStatus(id, False):
                    print("Language Disabled")
            messages.success(self.request, "Banner Disabled")

        elif 'enable-banner' in self.request.POST:
            toEnable = request.POST.getlist('banner-check')
            for id in toEnable:
                if api.bannerStatus(id, True):
                    print("Language Enabled")
            messages.success(self.request, "Banner Enabled")

        
        elif 'add-banner' in self.request.POST:
            form = AddBannersForm(request.POST or None)
            image_url = saveFile(request.FILES['image_upload'], 'banner_images')
            if form.is_valid():
                banner = AddBanners(
                    image_url,
                    form.cleaned_data['banner_title'],
                    form.cleaned_data['banner_text'],
                    form.cleaned_data['button_text'],
                    form.cleaned_data['button_link'],
                    form.cleaned_data['banner_color'],
                    )
                if api.addBanner(banner):
                    messages.success(self.request, "Banner added")
                    print("Banner Added")
        return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, **kwargs):
        banners_list = api.fetchBanners()
        context = {
            "banners_list": banners_list
        }
        return context
