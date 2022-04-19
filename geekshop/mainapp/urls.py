from xml.etree.ElementInclude import include

from django.urls import path
import mainapp.views as mainapp
app_name = 'mainapp'
urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),

]
