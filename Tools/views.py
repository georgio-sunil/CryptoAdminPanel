from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib import messages
from Tools.forms import AddBannersForm, FAQForms, UpdateBannerForms
from services import api
from services.models.Banners import AddBanners, UpdateBanner
from services.models.StaticContent import FAQ, UpdateTermsandCondition
from utilities.uploadFile import saveFile, saveUniqueFile

class BannerTable(LoginRequiredMixin, TemplateView):
    template_name = "tools/banner/banner.html"
    success_url = "tools/banner/banner.html"
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

class UpdateBannerDetails(LoginRequiredMixin, TemplateView):
    template_name = "tools/banner/update-banner.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        form = UpdateBannerForms(request.POST or None)
        bannerID = str(self.kwargs['pk'])

        if 'image_upload' in request.FILES:
            image_url = saveFile(request.FILES['image_upload'], 'banner_images')
        else:
            image_url = request.POST['image_upload']
        print(form)
        if form.is_valid():
            banner = UpdateBanner(
                image_url,
                form.cleaned_data['banner_title'],
                form.cleaned_data['banner_text'],
                form.cleaned_data['button_text'],
                form.cleaned_data['button_link'],
                form.cleaned_data['banner_color'],
            )
            print(banner)  
            if api.updateBanner(bannerID, banner):
                print("Banner Updated")
        return HttpResponseRedirect(reverse('banner-table'))

    def get_context_data(self, **kwargs):
        bannerID = str(self.kwargs['pk'])
        banner_details = api.fetchBanner(bannerID)
        context = {
            "banner" : banner_details
            }
        return context


class FAQTable(LoginRequiredMixin, TemplateView):
    template_name = "tools/static_content/faq.html"
    success_url = "tools/static-content/faq.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        
        print(request.POST)
        print(request.FILES)

        if 'tandc_file' in request.FILES:
            terms_and_conditions_url= saveUniqueFile(request.FILES['tandc_file'], 'terms_and_condition_files')
            tandc_object = UpdateTermsandCondition(terms_and_conditions_url)
            if api.updateTermsandConditions(tandc_object):
                print("Terms and Conditions Updated")
                messages.success(self.request, "Terms and Conditions Updated")
            else:
                print("Terms and Conditions Failed")
                messages.error(self.request, "Terms and Conditions Failed")
        elif 'add-faq' in request.POST:
            form = FAQForms(request.POST)
            if form.is_valid():
                faq = FAQ(form.cleaned_data['faq_question'],
                form.cleaned_data['faq_answer']
                )
                if api.addFAQ(faq):
                    messages.success(self.request, "Question Added")
                else:
                    print("Question API Failed")
                    messages.error(self.request, "Question Addition Failed")
            else:
                print("Question Addition Failed")
                messages.error(self.request, "Question Addition Failed")
        return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, **kwargs):
        FAQ = []
        static_content = api.fetchStaticContent()
        for content in static_content:
            if content['content_type'] == "Terms & Conditions":
                terms_and_conditions = content
            elif content['content_type'] == "Questions":
                FAQ.append(content)
        context = {
            "terms_and_conditions": terms_and_conditions,
            "faq" : FAQ
        }
        return context

class UpdateFAQDetails(LoginRequiredMixin, TemplateView):
    template_name = "tools/static_content/update-faq.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        form = FAQForms(request.POST or None)
        faqID = str(self.kwargs['pk'])

        if form.is_valid():
            faq = FAQ(form.cleaned_data['faq_question'],
            form.cleaned_data['faq_answer']
            )
            if api.updateFAQ(faqID, faq):
                print("Question Updated")
                messages.success(self.request, "Question Updated")
            else:
                messages.error(self.request, "Question Not Updated")

        return HttpResponseRedirect(reverse('faq'))

    def get_context_data(self, **kwargs):
        faqID = str(self.kwargs['pk'])
        faq_details = api.fetchFAQ(faqID)
        context = {
            "faq" : faq_details
            }
        return context