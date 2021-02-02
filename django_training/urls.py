from django.contrib import admin
from django.urls import path

from core.views import index, topic_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('topic/?P<pk>\\d+/', topic_details, name='topic_details'),
]
