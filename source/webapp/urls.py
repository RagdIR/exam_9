from django.urls import path, include

from webapp.views import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/', include([
        path('<int:pk>/', include([
            path('', PhotoView.as_view(), name='photo_view'),

            path('update/', PhotoUpdateView.as_view(), name='photo_update'),
            path('delete/', PhotoDeleteView.as_view(), name='photo_delete'),
            ]))
        ])),
    path('add/', PhotoCreateView.as_view(), name='photo_create'),
    ]