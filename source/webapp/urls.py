from django.urls import path, include

from webapp.views import IndexView, PhotoView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', PhotoView.as_view(), name='photo_view'),
]