from unicodedata import category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from Academy.forms import AddCategoryForm, AddCourseForm, TopicFileUploadForm, TopicForm, UpdateCourseForm
from services import api
from services.models.Category import AddCategory
from services.models.Courses import AddCourse, UpdateCourse
from services.models.Topics import Topic
from utilities.uploadFile import saveFile


class CourseTable(LoginRequiredMixin, TemplateView):
    template_name = "academy/course-table.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        form = AddCourseForm(request.POST or None)
        image_url = saveFile(request.FILES['course_image'], 'course_images')
        print(form)
        if form.is_valid():
            course = AddCourse(
                form.cleaned_data['course_name'],
                form.cleaned_data['course_tags'],
                image_url,
                form.cleaned_data['course_url'],
                form.cleaned_data['course_desc']
            )
            if api.addCourse(course):
                print("Course Added")
        return HttpResponseRedirect(reverse('courses'))

    def get_context_data(self, **kwargs):
        course_list = api.fetchCourses()
        context = {
            "course_list": course_list,
        }
        return context

class CategoriesTable(LoginRequiredMixin, TemplateView):
    template_name = "academy/categories/categories_list.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        form = AddCategoryForm(request.POST or None)
        course_tags = request.POST.getlist('category_tags')
        image_url = saveFile(request.FILES['image_upload'], 'category_images')
        if form.is_valid():
            category = AddCategory(
                form.cleaned_data['category_name'],
                form.cleaned_data['category_type'],
                image_url,
                course_tags,
            )
            print(category)
            if api.addCategory(category):
                print("Category Added")
        return HttpResponseRedirect(reverse('categories-list'))


    def get_context_data(self, **kwargs):
        categories_list = api.fetchCategories()
        context = {
            "categories_list": categories_list,
        }
        return context

class UpdateCategory(LoginRequiredMixin, TemplateView):
    template_name = "academy/categories/update_categories.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        form = AddCategoryForm(request.POST or None)
        categoryID = str(self.kwargs['pk'])
        course_tags = request.POST.getlist('category_tags')

        if 'image_upload' in request.FILES:
            image_url = saveFile(request.FILES['image_upload'], 'category_images')
        else:
            image_url = request.POST['image_upload']

        if form.is_valid():
            category = AddCategory(
                form.cleaned_data['category_name'],
                form.cleaned_data['category_type'],
                image_url,
                course_tags
            )
            print(category)  
            if api.updateCategory(categoryID, category):
                print("Category Updated")
        return HttpResponseRedirect(reverse('categories-list'))

    def get_context_data(self, **kwargs):
        categoryID = str(self.kwargs['pk'])
        category_details = api.fetchCategory(categoryID)
        context = {
            "category" : category_details
            }
        return context

class ViewCourse(LoginRequiredMixin, TemplateView):
    template_name = "academy/course-detail.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        courseID = str(self.kwargs['pk'])
        form = UpdateCourseForm(request.POST or None)
        print('Status ' ,request.FILES.get('image_upload', True))
        
        if 'image_upload' in request.FILES:
            image_url = saveFile(request.FILES['image_upload'], 'news_images')
        else:
            image_url = request.POST['image_upload']

        print(image_url)
        if form.is_valid():
            course = UpdateCourse(
                course_name = form.cleaned_data['course_name'],
                course_tags = form.cleaned_data['course_tags'],
                course_image=image_url,
                course_url= form.cleaned_data['course_url'],
                course_desc = form.cleaned_data['course_desc'] 
            )
            print(course)
            if api.updateCourse(courseID, course):
                print("Course Updated")
        return HttpResponseRedirect(reverse('courses'))

    def get_context_data(self, **kwargs):
        courseID = str(self.kwargs['pk'])
        course_details = api.fetchCourse(courseID)
        topic_details = course_details["topics"]
        context = {
            "course" : course_details,
            "topics" : topic_details
            }
        return context

class AddTopic(LoginRequiredMixin, TemplateView):
    template_name = "academy/topics/add-topic.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        form = TopicForm(request.POST or None)
        courseID = str(self.kwargs['pk'])
        course_details = api.fetchCourse(courseID)
        print(request.FILES['topic_image'])
        image_url = saveFile(request.FILES['topic_image'], 'topic_images')
        print(form)
        if form.is_valid():
            print("valid")
            topic = Topic(
                form.cleaned_data['topic_name'],
                form.cleaned_data['topic_desc'],
                form.cleaned_data['topic_type'],
                image_url,
                form.cleaned_data['topic_url']
            )
            course_details["topics"] = [topic]
            if api.updateCourse(courseID, course_details):
                print("Topic Added")
        return HttpResponseRedirect(reverse('courses'))

class UpdateTopic(LoginRequiredMixin, TemplateView):
    template_name = "academy/topics/update-topic.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        form = TopicForm(request.POST or None)
        courseID = str(self.kwargs['pk'])
        course_details = api.fetchCourse(courseID)
        if form.is_valid():
            topic = Topic(
                form.cleaned_data['topic_name'],
                form.cleaned_data['topic_desc'],
                form.cleaned_data['topic_type'],
                form.cleaned_data['topic_url'],
                form.cleaned_data['topic_content']
            )
            course_details["topics"] = [topic]
            if api.updateCourse(courseID, course_details):
                print("Topic Added")
        return HttpResponseRedirect(reverse('courses'))

    def get_context_data(self, **kwargs):
        courseID = str(self.kwargs['pk'])
        course_details = api.fetchCourse(courseID)
        topic_details = course_details["topics"]
        context = {
            "topic" : topic_details[0]
            }
        return context