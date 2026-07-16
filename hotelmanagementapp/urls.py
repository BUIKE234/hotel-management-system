from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home.html',views.home, name='home'),
    path('rooms.html',views.rooms,name='rooms'),
    path('About.html',views.about, name='about'),
    path('bookings.html',views.bookings, name='bookings'),
    path('contacts.html',views.contacts, name='contacts'),
    path('book.html',views.book_room, name='book_room'),
    path('success/', views.success, name='success'),
    path('success/<int:booking_id>/', views.booking_success, name='booking_success'),
]
