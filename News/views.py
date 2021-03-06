from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from News.forms import AddNewsFeedForm, CreateNewsForm
from services import api
from services.models.News import AddNews
from services.models.NewsFeed import AddNewsFeed
from utilities.uploadFile import saveFile

# Create your views here.

class NewsTable(LoginRequiredMixin, TemplateView):
    template_name = "news/news-table.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = AddNewsFeedForm(request.POST or None)
        if form.is_valid():
            n = AddNewsFeed(form.cleaned_data['feed_name'],
                form.cleaned_data['feed_url']
            )
            print(n)
            if api.addNewsFeed(n):
                return HttpResponseRedirect(reverse('news-feed'))

        return HttpResponseRedirect(self.request.path_info)


    def get_context_data(self, **kwargs):
        news_list = api.fetchNews()
        context = {
            "news_list": news_list
        }
        return context

class NewsFeedTable(LoginRequiredMixin, TemplateView):
    template_name = "news/news-feed-list.html"
    success_url = "news/news-feed-list.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        # Disable the feed.
        if 'disable-feed' in self.request.POST:
            print(request.POST)
            toDisable = request.POST.getlist('feed-check')
            for id in toDisable:
                if api.feedStatus(id, False):
                    print("Feed Disabled")

        # Enable the feed.
        elif 'enable-feed' in self.request.POST:
            toEnable = request.POST.getlist('feed-check')
            for id in toEnable:
                if api.feedStatus(id, True):
                    print("Feed Enabled")
        return HttpResponseRedirect(self.request.path_info)

    
    def get_context_data(self, **kwargs):
        feed_list = api.fetchFeed()
        context = {
            "news_feed_list": feed_list
        }
        return context

class CreateNews(LoginRequiredMixin, TemplateView):
    template_name = "news/add-news.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('news')

    def post(self, request, *args, **kwargs):
        form = CreateNewsForm(request.POST or None)
        news_tags = request.POST.getlist('tags')
        print(news_tags)
        image_url = saveFile(request.FILES['image_upload'], 'news_images')
        if form.is_valid():
            n = AddNews(form.cleaned_data['news_title'],
                news_tags,
                form.cleaned_data['content'],
                image_url
            )
            print(n)
            if api.addNews(n):
                return HttpResponseRedirect(reverse('news'))

        return HttpResponseRedirect(self.request.path_info)

class UpdateNews(LoginRequiredMixin, TemplateView):
    template_name = "news/update-news.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('news')

    def get_context_data(self, **kwargs):
        newsID = str(self.kwargs['pk'])
        news_list = api.fetchSingleNews(newsID)
        context = {
            "news": news_list
        }
        return context

    def post(self, request, *args, **kwargs):
        newsID = str(self.kwargs['pk'])
        form = CreateNewsForm(request.POST or None)

        # if request.POST.get('image_upload', True):
        #     image_url = request.POST['image_upload']
        # else:
        #     image_url = saveFile(request.FILES['image_upload'], 'news_images')

        news_tags = request.POST.getlist('tags')

        if 'image_upload' in request.FILES:
            image_url = saveFile(request.FILES['image_upload'], 'news_images')
        else:
            image_url = request.POST['image_upload']

        if form.is_valid():
            print("valid")
            n = AddNews(form.cleaned_data['news_title'],
                news_tags,
                form.cleaned_data['content'],
                image_url
            )
            print(n)
            if api.updateNews(newsID, n):
                return HttpResponseRedirect(reverse('news'))

        return HttpResponseRedirect(self.request.path_info)
