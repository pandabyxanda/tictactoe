import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from channels.layers import get_channel_layer

# def get_group_names():
#     channel_layer = get_channel_layer()
#     group_names = channel_layer.group_names()
#     return group_names

list_of_groups = [{'name': 'group1', 'players': 0, 'players_names': []}]

class GameConsumer(WebsocketConsumer):
    def connect(self):
        print()
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        sc_all = self.scope
        print(f"{sc_all = }")
        # self.room_group_name = "chat_%s" % self.room_name
        group = list_of_groups[-1]
        if group['players'] == 2:
            list_of_groups.append({'name': f'group{len(list_of_groups)+1}', 'players': 0, 'players_names': []})

        group = list_of_groups[-1]
        self.room_group_name = group['name']
        list_of_groups[-1]["players"] += 1
        list_of_groups[-1]["players_names"].append(self.room_name)
        print("connect function called")
        print(f"{self.room_name = } ===={self.room_group_name = }")

        # print("111")

        # s = get_group_names()
        # print(f"{self.channel_layer = }")
        # print(f"{s = }")
        # print("111")
        # Join room group
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        self.accept()

        if list_of_groups[-1]["players"] == 2:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {"type": "chat_message", "status": "game started", 'players_names': list_of_groups[-1]["players_names"]}
            )

    def disconnect(self, close_code):
        print("disconnect function called")

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print('___')
        text_data_json = json.loads(text_data)
        # message = text_data_json["message"]
        list_fields = text_data_json["list_fields"]
        move = text_data_json["move"]
        print(f"{list_fields = }")

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", 'lol':{'lal':'lyl'}, 'list_fields':list_fields, 'move': move}
        )
        print("receive function called")
        print(f"{text_data_json = }")

    # Receive message from room group
    def chat_message(self, event):
        print("chat_message function called")
        # message = event["message"]
        if event.get("status") == "game started":
            print(f"{event.get('status') = }")
            print(f"{event.get('players_names') = }")
            self.send(text_data=json.dumps({'status': "game started", 'qqq': '222', 'players_names': event.get("players_names")}))
        else:
            list_fields = event["list_fields"]
            move = event["move"]
            # print(f"{event = }")
            # print(f"{event['message'] = }")

            # Send message to WebSocket
            self.send(text_data=json.dumps({'list_fields': list_fields, 'qqq': '222', 'move': move}))





class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        print()
        print("connect function called")
        print(f"{self.room_name = } {self.room_group_name = }")
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()
        print(f"{self.channel_layer = }")

    def disconnect(self, close_code):
        print("disconnect function called")

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print('___')
        text_data_json = json.loads(text_data)
        # message = text_data_json["message"]
        list_fields = text_data_json["list_fields"]
        print(f"{list_fields = }")

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", 'lol':{'lal':'lyl'}, 'list_fields':list_fields}
        )
        print("receive function called")
        print(f"{text_data_json = }")

    # Receive message from room group
    def chat_message(self, event):
        print("chat_message function called")
        # message = event["message"]
        list_fields = event["list_fields"]
        # print(f"{event = }")
        # print(f"{event['message'] = }")

        # Send message to WebSocket
        self.send(text_data=json.dumps({'list_fields': list_fields}))



























# import json
#
# from channels.generic.websocket import WebsocketConsumer
#
#
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()
#
#     def disconnect(self, close_code):
#         pass
#
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#
#         self.send(text_data=json.dumps({"message": message}))
#
#
#
#
#















# import json
# from channels.generic.websocket import WebsocketConsumer
#
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()
#
#         self.send(text_data=json.dumps({
#             'type': 'connection_established',
#             'message': 'You are connected',
#         }))