from django.urls import path
from provinces import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.ProvincesList.as_view()),
    path("<int:pk>", views.ProvincesDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
