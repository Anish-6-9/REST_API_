from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('shakes/', views.shakes, name='shakes'),
    path('shakes/<pk>', views.details, name='details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
