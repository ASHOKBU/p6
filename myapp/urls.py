from django.urls import path
from myapp import views 
app_name = 'myapp'
urlpatterns=[
    path('base/',views.base,name="base"),
    path('child/',views.child,name="child"),
    path('home/',views.home,name="home"),
]