from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoryApi.as_view()),
    path('services', views.WorkApi.as_view()),
    path('specialists', views.SpecialistsApi.as_view()),
    path('last_change', views.ChangeLogApi.as_view()),
    path('create_pdf', views.PDFApi.as_view()),
    path('parce_excel', views.parce_excel),
]