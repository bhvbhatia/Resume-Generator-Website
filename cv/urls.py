from django.urls import path
from . import views
urlpatterns = [
    path('', views.homeView, name='home'),
    path('detail/', views.detailView, name='detail'),
    path('detail/pdf/',views.render_pdf_view, name='pdf')
    ]
