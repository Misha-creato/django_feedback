from django.urls import path

from apps.index.views import Index


urlpatterns = [
    path(
        '',
        Index.as_view(),
        name='index',
    )
]
