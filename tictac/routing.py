from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"ws/multi/(?P<room_name>\w+)/$", consumers.GameConsumer.as_asgi()),
]
# websocket_urlpatterns = [
#     re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
# ]

# from django.urls import re_path
# from . import consumers
#
# websocket_urlpatterns = [
#     re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
# ]