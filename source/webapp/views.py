from django.shortcuts import render
from django.views.generic import ListView, DetailView
from webapp.models import Photo

class IndexView(ListView):
    template_name = 'photo/index.html'
    context_object_name = 'photos'
    paginate_by = 10
    paginate_orphans = 2
    model = Photo

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Photo.objects.all()
        return data


class PhotoView(DetailView):
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

