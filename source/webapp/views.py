from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo, Favorite


class IndexView(ListView):
    template_name = 'photo/index.html'
    context_object_name = 'photos'
    model = Photo

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Photo.objects.all().order_by('-created_at')
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
        return self.request.user.has_perm or self.request.user('webapp.update_photo')

    def get_success_url(self):
        return reverse('photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView, UserPassesTestMixin):
    template_name = 'photo/photo_delete.html'
    model = Photo
    # success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user or self.request.user.has_perm('webapp.update_photo')

    def get_success_url(self):
        return reverse('webapp:index')


class AddFavView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        favorite, created = Favorite.objects.get_or_create(photo=photo, user=request.user)
        if created:
            photo.favorite
            photo.save()
            return HttpResponse(photo.favorite)
        else:
            return HttpResponseForbidden()


class DelFavView(LoginRequiredMixin, View):
    def delete(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        favorite = get_object_or_404(photo.favorites, user=request.user)
        favorite.delete()
        photo.save()
        return HttpResponse(photo.favorite)