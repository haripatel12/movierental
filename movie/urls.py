from movie import views
from django.urls import path

urlpatterns = [
    path('',views.home, name="home"),
    path('addmovie/', views.addmovie, name='addmovie'),
    path('addcustomer/',views.addcustomer, name='addcustomer'),
    path('availablemovie/',views.availablemovie, name='availablemovie'),
    path('rentedmovie/',views.rentedmovie, name='rented'),
    path('update/<int:movieid>/',views.update, name='update'),
    path('listofcustomer/', views.listofcustomer, name= "listofcustomer" ),
    path('assignmovie/',views.assignmovie),
    path('listofmovie/', views.listofmovie, name='listofmovie'),
    path('deletemovie/<int:delete_movieid>/',views.deletemovie, name='updatemovie'),
    path('deletecust/<int:delete_custid>/',views.deletecust, name='updatecust'),

]