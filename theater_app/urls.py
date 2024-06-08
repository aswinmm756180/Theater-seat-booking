from django.urls import path
from. import views

urlpatterns = [
    path('',views.index,name="index"),



    # ----------------------user--------------------------------------------------
    path('user_reg',views.user_reg,name="user_reg"),
    path('user_login',views.user_login,name="user_login"),
    path('home',views.home,name="home"),
    path('logout_view',views.logout_view,name="logout_view"),
    path('view_all_movies',views.view_all_movies,name="view_all_movies"),
    path('movie/<int:movie_id>/theaters/', views.theaters_by_movie, name='theaters_by_movie'),
    path('movie/<int:movie_id>/theater/<int:theater_id>/booking/<str:time_slot>/', views.theater_seat_booking, name='theater_seat_booking'),
    # path('book_seats/', views.book_seats, name='book_seats'),
    # path('<int:movie_id>/theater/<int:theater_id>/booking/<str:time_slot>/confirm/', views.confirm_booking, name='confirm_booking'),
    path('all_theaters/', views.all_theaters, name='all_theaters'),
    path('book-seat/', views.book_seat, name='book_seat'),
    path('booking-confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('user/bookings/', views.user_bookings, name='user_bookings'),
    path('bookings/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('view_booking_details/', views.view_booking_details, name='view_booking_details'),
    path('payment',views.payment,name="payment"),
    path('user_chat',views.user_chat,name='user_chat'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('delete-all/', views.delete_all_messages, name='delete_all_messages'),

  





    #-----------------------manager------------------------------------------------
    path('manager_reg',views.manager_reg, name='manager_reg'),
    path('manager_login',views.manager_login, name='manager_login'),
    path('manager_home',views.manager_home, name='manager_home'),
    path('manager/logout/', views.manager_logout, name='manager_logout'),
    path('add_movie', views.add_movie, name='add_movie'),
    path('view_movie', views.view_movie, name='view_movie'),
    path('delete_movie/<int:id>/', views.delete_movie, name='delete_movie'), 
    path('add_theater', views.add_theater, name='add_theater'),
    path('view_theater', views.view_theater, name='view_theater'),
    path('edit_theater/<int:theater_id>/',views.edit_theater, name='edit_theater'),
    path('delete_theater/<int:id>/', views.delete_theater, name='delete_theater'),
    path('manager/booking/', views.manager_booking_page, name='manager_booking_page'),
    path('manager/booking/theater/<int:theater_id>/', views.theater_booking_page, name='theater_booking_page'),
    path('booking/<int:booking_id>/',views.view_booking, name='view_booking'),
    path('manager_chat',views.manager_chat,name='manager_chat'),
    path('delete_chat/<int:chat_id>/', views.delete_chat, name='delete_chat'),
 





    #-----------------------admin---------------------------------------------------
    path('admin_reg',views.admin_reg,name='admin_reg'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_panel',views.admin_panel,name='admin_panel'),
    path('logout_admin',views.logout_admin,name='logout_admin'),
    path('view_all_users/',views.view_all_users, name='view_all_users'),
    path('view_all_managers/',views.view_all_managers, name='view_all_managers'),
    path('view_all_theaters/',views.view_all_theaters, name='view_all_theaters'),
    path('bookings/', views.view_all_bookings, name='view_all_bookings'),
]