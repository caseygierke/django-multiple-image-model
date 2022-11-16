from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from .models import Image, Project
from django.views.generic import DetailView, TemplateView, ListView, CreateView, UpdateView, DeleteView
from .forms import ProjectForm

# Create your views here.

def home(request):
    images=Image.objects.all()
    context={
        'images':images
    }
    return render(request, 'index.html', context)

def file_upload(request):
    if request.method == 'POST':
        my_file=request.FILES.get('file')
        Image.objects.create(image=my_file)
        return HttpResponse('')
    return JsonResponse({'post':'false'})

class ImagePageView(TemplateView):
    
    template_name = 'images.html'

    def get_queryset(self):
        print(f'\n\nCalling ImagePageView\n\n')
        return Image.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(ImagePageView, self).get_context_data(**kwargs)
        # context['events'] = Event.objects.all()
        context['images'] = Image.objects.all()
        print(type(context['images'][0]))
        print(dir(context['images'][0]))
        # context['pastEvents'] = Event.objects.filter(event_date__lte=timezone.now())
        # context['categories'] = Categories.objects.all()
        # And so on for more models
        return context  

# class ProjectPageView(TemplateView):
class ProjectPageView(ListView):
    
    template_name = 'projects.html'

    def get_queryset(self):
        print(f'\n\nCalling ProjectPageView\n\n')
        return Project.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(ProjectPageView, self).get_context_data(**kwargs)
        # context['events'] = Event.objects.all()
        context['projects'] = Project.objects.all()
        context['images'] = Image.objects.all()
        # print(type(context['images'][0]))
        # print(dir(context['images'][0]))
        # context['pastEvents'] = Event.objects.filter(event_date__lte=timezone.now())
        # context['categories'] = Categories.objects.all()
        # And so on for more models
        return context  

class ProjectCreateView(CreateView):

    def __init__(self):
        print(f'\n\nCalling ProjectCreateView\n\n')

    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects')        

    # def get_context_data(self, **kwargs):
    #     context = super(ProjectPageView, self).get_context_data(**kwargs)
    #     print(type(context))
    #     print(dir(context))
        
class ProjectUpdateView(UpdateView):

    def __init__(self):
        print(f'\n\nCalling ProjectUpdateView\n\n')

    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects')   

class ProjectDeleteView(DeleteView):

    def __init__(self):
        print(f'\n\nCalling ProjectDeleteView\n\n')

    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects') 