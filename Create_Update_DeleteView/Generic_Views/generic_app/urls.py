from django.urls import path
from .views import PublishList,DetailList,CreateNews,DeleteNews,UpdateNews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',PublishList.as_view(),name = 'home'),
    path('create/',CreateNews.as_view(),name = 'create'),
    path('post/<int:pk>/',DetailList.as_view(),name = 'post'),
    path('delete/<int:pk>/',DeleteNews.as_view(),name = 'delete'),
    path('update/<int:pk>/',UpdateNews.as_view(),name = 'update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
