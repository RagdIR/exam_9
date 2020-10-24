from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class IndexView(ListView):
    template_name = 'photo/index.html'
    context_object_name = 'photos'
    model = Photo

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Photo.objects.all()
        return data


class PhotoView(DetailView):
    template_name = 'photo/photo_view.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'photo/photo_create.html'
    form_class = PhotoForm

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return redirect('webapp:photo_view', pk=photo.pk)

    # def get_success_url(self):
    #     return reverse('photo_view', kwargs={'pk': self.object.pk})


class PhotoUpdateView(UpdateView, UserPassesTestMixin):
    template_name = 'photo/photo_update.html'
    form_class = PhotoForm
    model = Photo

    def test_func(self):
        return self.request.user.has_perm or self.request.has_perm('webapp.update_photo')

    def get_success_url(self):
        return reverse('photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView, UserPassesTestMixin):
    template_name = 'photo/photo_delete.html'
    model = Photo
    # success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.has_perm or self.request.has_perm('webapp.update_photo')

    def get_success_url(self):
        return reverse('webapp:index')