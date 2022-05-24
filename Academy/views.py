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
        if form.is_valid():
            course = AddCourse(
                form.cleaned_data['course_name'],
                form.cleaned_data['course_tags'],
                form.cleaned_data['course_image'],
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
        if form.is_valid():
            category = AddCategory(
                form.cleaned_data['category_name'],
                form.cleaned_data['category_type'],
                form.cleaned_data['category_tags'].split(","),
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

class ViewCourse(LoginRequiredMixin, TemplateView):
    template_name = "academy/course-detail.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        courseID = str(self.kwargs['pk'])
        form = UpdateCourseForm(request.POST or None)
        print(form)
        if form.is_valid():
            course = UpdateCourse(
                course_name = form.cleaned_data['course_name'],
                course_tags = form.cleaned_data['course_tags'],
                course_desc = form.cleaned_data['course_desc'] 
            )
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
        fileForm = TopicFileUploadForm(request.FILES)
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