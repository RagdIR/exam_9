from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View
from pip._vendor.requests import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from webapp.models import Photo, Favorite


# class AddFavView(LoginRequiredMixin, View):
#     def post(self, request, *args, **kwargs):
#         photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
#         favorite, created = Favorite.objects.get_or_create(photo=photo, user=request.user)
#         if created:
#             photo.favorite
#             photo.save()
#             return HttpResponse(photo.favorite)
#         else:
#             return HttpResponseForbidden()
#
#
# class DelFavView(LoginRequiredMixin, View):
#     def delete(self, request, *args, **kwargs):
#         photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
#         favorite = get_object_or_404(photo.favorites, user=request.user)
#         favorite.delete()
#         photo.save()
#         return HttpResponse(photo.favorite)

@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')

class PhotoViewSet(ViewSet):
    queryset = Photo.objects.all()

    @action(methods=['post'], detail=True)
    def favor(self, request, pk=None):
        photo = get_object_or_404(Photo, pk=pk)
        add, created = Favorite.objects.get_or_create(photo=photo, user=request.user)
        if created:
            photo.add_favorite
            photo.save()
            return Response({'pk': pk, 'favorites': photo.add_favorite})
        else:
            return Response(status=403)

    @action(methods=['delete'], detail=True)
    def unfavor(self, request, pk=None):
        photo = get_object_or_404(Photo, pk=pk)
        add = get_object_or_404(photo.favorite, user=request.user)
        add.delete()
        photo.add_favorite
        photo.save()
        return Response({'pk': pk, 'favorites': photo.add_favorite})