import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .views import list_fields
# from .algos import check_win

list_fields = list_fields

from channels.layers import get_channel_layer

# def get_group_names():
#     channel_layer = get_channel_layer()
#     group_names = channel_layer.group_names()
#     return group_names

list_of_groups = {'group_1': {'number_of_players': 0, 'players_ids': [], 'players_names': [], 'players_session_ids': []}}
free_group = 'group_1'
players = []


class LobbyConsumer(WebsocketConsumer):
    def connect(self):
        print()
        print('Consumer. Connecting to lobby')

        self.room_name = 'multi'
        self.room_group_name = 'multi'
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        print("Consumer. Disconnecting from lobby")
        # session_lazy_obj = self.scope.get('session')

        data = self.scope
        print(f"{data = }")

        session_id = self.scope.get('cookies').get('sessionid')

        player_index = [x for x in range(0, len(players)) if players[x]['session_key'] == session_id][0]

        if session_id in [x['session_key'] for x in players]:
            players.pop(player_index)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "lobby_message", 'players': players}
        )
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)
        print(f"{players = }")

    # Receive message from WebSocket
    def receive(self, text_data):

        # session_lazy_obj = self.scope.get('session')
        # print(f"{session_lazy_obj = }")
        print("Consumer. Receiving data from WebSocket1")
        text_data_json = json.loads(text_data)
        print(f"{text_data_json = }")
        if text_data_json['session_key'] not in [x['session_key'] for x in players]:
            players.append({'name': text_data_json['player_name'],
                            'id': text_data_json['id'],
                            'session_key': text_data_json['session_key'],
                            })
        else:
            print("Player with same id has already joined lobby")

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "lobby_message", 'players': players}
        )

    # Receive message from room group
    def lobby_message(self, event):
        print("Consumer. Sending data to all ws")
        # message = event["message"]
        print(f"{event = }")
        # message = event["message"]
        # if event.get("status") == "game started":
        #     print(f"{event.get('status') = }")
        #     print(f"{event.get('players_names') = }")
        #     self.send(text_data=json.dumps({'status': "game started", 'qqq': '222', 'players_names': event.get("players_names")}))
        # else:
        #     list_fields = event["list_fields"]
        #     move = event["move"]
        #     # print(f"{event = }")
        #     # print(f"{event['message'] = }")
        #
        #     # Send message to WebSocket
        self.send(text_data=json.dumps(event))
        # self.send(text_data=json.dumps({'status': "game started"}))


class GameConsumer(WebsocketConsumer):
    def connect(self):
        global free_group

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        session_id = self.scope.get('cookies').get('sessionid')
        # list_of_groups[free_group] = {'number_of_players': 0, 'players_ids': [], 'players_names': []}
        list_of_groups[free_group]['number_of_players'] += 1
        list_of_groups[free_group]['players_ids'].append(self.room_name)
        list_of_groups[free_group]['players_session_ids'].append(session_id)

        self.room_group_name = free_group

        if list_of_groups.get(free_group).get('number_of_players') == 2:
            new_group = f'group_{len(list_of_groups) + 1}'
            list_of_groups[new_group] = {'number_of_players': 0, 'players_ids': [],
                                         'players_names': [], 'players_session_ids': []}
            free_group = new_group

        print(f"game_{self.room_name = }")
        print(f"game_{self.room_group_name = }")

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        print("game_ Consumer. Disconnecting from group")
        # session_lazy_obj = self.scope.get('session')

        print(f"{self.scope = }")

        session_id = self.scope.get('cookies').get('sessionid')

        print(f"{session_id = }")

        print(f"{players = }")

        print(f"{list_of_groups = }")

        players_index = list_of_groups[self.room_group_name]['players_session_ids'].index(session_id)

        # player_index = [x for x in range(0, len(players)) if players[x]['session_key'] == session_id][0]

        # print(f"{list_of_groups = }")
        #
        # print(f"{session_id = }")

        print(f"eee2")

        print(f"{list_of_groups[self.room_group_name]['number_of_players'] = }")

        # print(f"{type(list_of_groups[self.room_group_name]['number_of_players']) = }")
        list_of_groups[self.room_group_name]['number_of_players'] -= 1
        print('---one')
        # for id in list_of_groups[self.room_group_name]['players_ids']:
        #     if id not in players
        list_of_groups[self.room_group_name]['players_ids'].pop(players_index)
        print('---two')
        list_of_groups[self.room_group_name]['players_names'].pop(players_index)
        list_of_groups[self.room_group_name]['players_session_ids'].pop(players_index)
        print(f"{list_of_groups = }")


        # data = self.scope
        # print(f"{data = }")

        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name, {"type": "lobby_message", 'players': players}
        # )
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)
        # print(f"{players = }")

    # Receive message from WebSocket
    def receive(self, text_data):
        print('game____')

        print(f"{list_of_groups = }")
        text_data_json = json.loads(text_data)
        print(f"game_{text_data_json = }")
        if text_data_json.get('game').get('status') == 'joining new game':
            list_of_groups[self.room_group_name]["players_names"].append(text_data_json.get('game').get('player_name'))
            if len(list_of_groups[self.room_group_name]["players_ids"]) == 2:
                print(f"game_game started, 2 players connected")

                async_to_sync(self.channel_layer.group_send)(self.room_group_name, {"type": "message_start_game",
                                                                                    'data': list_of_groups[
                                                                                        self.room_group_name],
                                                                                    })
        if text_data_json.get('game').get('status') == 'Game started':
            list_fields = text_data_json.get('game').get('list_fields')

            fields = [[x['value'] for x in list_fields[y:y+int(len(list_fields) ** 0.5)]]
                      for y in range(0, len(list_fields)) if y % int(len(list_fields) ** 0.5) == 0]
            # winner = check_win(fields=fields, units=('x', 'o'), win_line_length=2)
            winner = None
            if winner:
                print(f'winner is {winner}')

                message = {
                    'type': "data",
                    'game': {
                        'status': 'Game finished',
                        'list_fields': list_fields,
                        # 'move': event['data']['game']['move'],
                        # 'id': player_id,
                        'victory_status': None,
                        'winner': text_data_json.get('game').get('move'),
                    },
                    'players': [
                        {
                            'id': list_of_groups[self.room_group_name]["players_ids"][0],
                            'name': list_of_groups[self.room_group_name]["players_names"][0],
                            'unit': 'x',
                            'wins': 0,
                            'losses': 0,
                            'draws': 0,
                        },
                        {
                            'id': list_of_groups[self.room_group_name]["players_ids"][1],
                            'name': list_of_groups[self.room_group_name]["players_names"][1],
                            'unit': 'o',
                            'wins': 0,
                            'losses': 0,
                            'draws': 0,
                        },

                    ]
                }
                async_to_sync(self.channel_layer.group_send)(self.room_group_name, {"type": "message_game_over",
                                                                                    'data': message,
                                                                                    })



            else:
                if text_data_json.get('game').get('move') == list_of_groups[self.room_group_name]["players_ids"][0]:
                    move = list_of_groups[self.room_group_name]["players_ids"][1]
                else:
                    move = list_of_groups[self.room_group_name]["players_ids"][0]
                message = {
                    'type': "data",
                    'game': {
                        'status': 'Game started',
                        'list_fields': text_data_json.get('game').get('list_fields'),
                        'move': move,
                    }
                }
                async_to_sync(self.channel_layer.group_send)(self.room_group_name, {"type": "message_next_move",
                                                                                    'data': message,
                                                                                    })

        # # Send message to room group
        # if text_data_json.get('game').get('status') == 'joining new game':
        #     async_to_sync(self.channel_layer.group_send)(self.room_group_name, {"type": "message1", 'data': text_data_json })
        # else:
        #     async_to_sync(self.channel_layer.group_send)(self.room_group_name, {"type": "message1", 'data': text_data_json })
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name, {"type": "chat_message", 'lol':{'lal':'lyl'}, 'list_fields':list_fields, 'move': move}

    # Receive message from room group
    def message_start_game(self, event):
        print("game_message_start_game")

        print(f"game_ {event = }")

        print(f"game_{self.room_group_name = }")
        message = {
            'type': "data",
            'game': {
                'status': 'Game started',
                'list_fields': list_fields,
                'move': list_of_groups[self.room_group_name]["players_ids"][0],
                # 'id': player_id,
                'victory_status': None,
                'winner': None,
            },
            'players': [
                {
                    'id': list_of_groups[self.room_group_name]["players_ids"][0],
                    'name': list_of_groups[self.room_group_name]["players_names"][0],
                    'unit': 'x',
                    'wins': 0,
                    'losses': 0,
                    'draws': 0,
                },
                {
                    'id': list_of_groups[self.room_group_name]["players_ids"][1],
                    'name': list_of_groups[self.room_group_name]["players_names"][1],
                    'unit': 'o',
                    'wins': 0,
                    'losses': 0,
                    'draws': 0,
                },

            ]
        }

        self.send(text_data=json.dumps(message))


    def message_next_move(self, event):
        print("game_message_next_move")

        # print(f"game_ {event = }")

        # print(f"game_{self.room_group_name = }")
        message = {
            'type': "data",
            'game': {
                'status': 'Game started',
                'list_fields': event['data']['game']['list_fields'],
                'move': event['data']['game']['move'],
                # 'id': player_id,
                'victory_status': None,
                'winner': None,
            },
            'players': [
                {
                    'id': list_of_groups[self.room_group_name]["players_ids"][0],
                    'name': list_of_groups[self.room_group_name]["players_names"][0],
                    'unit': 'x',
                    'wins': 0,
                    'losses': 0,
                    'draws': 0,
                },
                {
                    'id': list_of_groups[self.room_group_name]["players_ids"][1],
                    'name': list_of_groups[self.room_group_name]["players_names"][1],
                    'unit': 'o',
                    'wins': 0,
                    'losses': 0,
                    'draws': 0,
                },

            ]
        }

        self.send(text_data=json.dumps(message))


    def message_game_over(self, event):
        print("game_message_game_over")

        self.send(text_data=json.dumps(event.get('data')))








    #     # message = event["message"]
    # if event.get("status") == "game started":
    #     print(f"{event.get('status') = }")
    #     print(f"{event.get('players_names') = }")
    #     self.send(text_data=json.dumps({'status': "game started", 'qqq': '222', 'players_names': event.get("players_names")}))
    # else:
    #     list_fields = event["list_fields"]
    #     move = event["move"]
    #     # print(f"{event = }")
    #     # print(f"{event['message'] = }")
    #
    #     # Send message to WebSocket
    #     self.send(text_data=json.dumps({'list_fields': list_fields, 'qqq': '222', 'move': move}))

# class GameConsumer(WebsocketConsumer):
#     def connect(self):
#         print()
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         sc_all = self.scope
#         print(f"{sc_all = }")
#         # self.room_group_name = "chat_%s" % self.room_name
#         group = list_of_groups[-1]
#         if group['players'] == 2:
#             list_of_groups.append({'name': f'group{len(list_of_groups)+1}', 'players': 0, 'players_names': []})
#
#         group = list_of_groups[-1]
#         self.room_group_name = group['name']
#         list_of_groups[-1]["players"] += 1
#         list_of_groups[-1]["players_names"].append(self.room_name)
#         print("connect function called")
#         print(f"{self.room_name = } ===={self.room_group_name = }")
#
#         # print("111")
#
#         # s = get_group_names()
#         # print(f"{self.channel_layer = }")
#         # print(f"{s = }")
#         # print("111")
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
#
#         self.accept()
#
#         if list_of_groups[-1]["players"] == 2:
#             async_to_sync(self.channel_layer.group_send)(
#                 self.room_group_name,
#                 {"type": "chat_message", "status": "game started", 'players_names': list_of_groups[-1]["players_names"]}
#             )
#
#     def disconnect(self, close_code):
#         print("disconnect function called")
#
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         print('___')
#         text_data_json = json.loads(text_data)
#         # message = text_data_json["message"]
#         list_fields = text_data_json["list_fields"]
#         move = text_data_json["move"]
#         print(f"{list_fields = }")
#
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {"type": "chat_message", 'lol':{'lal':'lyl'}, 'list_fields':list_fields, 'move': move}
#         )
#         print("receive function called")
#         print(f"{text_data_json = }")
#
#     # Receive message from room group
#     def chat_message(self, event):
#         print("chat_message function called")
#         # message = event["message"]
#         if event.get("status") == "game started":
#             print(f"{event.get('status') = }")
#             print(f"{event.get('players_names') = }")
#             self.send(text_data=json.dumps({'status': "game started", 'qqq': '222', 'players_names': event.get("players_names")}))
#         else:
#             list_fields = event["list_fields"]
#             move = event["move"]
#             # print(f"{event = }")
#             # print(f"{event['message'] = }")
#
#             # Send message to WebSocket
#             self.send(text_data=json.dumps({'list_fields': list_fields, 'qqq': '222', 'move': move}))
#
#
#
#
#
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = "chat_%s" % self.room_name
#
#         print()
#         print("connect function called")
#         print(f"{self.room_name = } {self.room_group_name = }")
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )
#
#         self.accept()
#         print(f"{self.channel_layer = }")
#
#     def disconnect(self, close_code):
#         print("disconnect function called")
#
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         print('___')
#         text_data_json = json.loads(text_data)
#         # message = text_data_json["message"]
#         list_fields = text_data_json["list_fields"]
#         print(f"{list_fields = }")
#
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {"type": "chat_message", 'lol':{'lal':'lyl'}, 'list_fields':list_fields}
#         )
#         print("receive function called")
#         print(f"{text_data_json = }")
#
#     # Receive message from room group
#     def chat_message(self, event):
#         print("chat_message function called")
#         # message = event["message"]
#         list_fields = event["list_fields"]
#         # print(f"{event = }")
#         # print(f"{event['message'] = }")
#
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({'list_fields': list_fields}))


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
