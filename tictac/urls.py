from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('single/', singleplayer, name='single'),
    path('multi/', multiplayer, name='multi'),
    path('multi/<str:room_name>/', multiplayer, name='multi'),
    # path('collections/', collections, name='collections'),
    # path('test/', test, name='test'),
    path('about/', about, name='about'),
    # path('register/', RegisterUser.as_view(), name='register'),
    # path('login/', LoginUser.as_view(), name='login'),
    # path('logout/', logout_user, name='logout'),
    # path("<str:room_name>/", room, name="room"),
    path('tic/', tic, name='tic'),
]

