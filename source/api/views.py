from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from webapp.models import Photo, Favorite


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