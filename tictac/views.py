import json
import random
import uuid

from django.shortcuts import render, redirect

from .forms import *
from .models import *
from .algos import *

length_of_side = 15
number_of_cells = length_of_side ** 2
list_fields = [{'index': x, 'value': '.'} for x in range(number_of_cells)]
# list_fields[4]['value'] = 'A'
# list_fields[5]['value'] = 'x'
# list_fields[23]['value'] = 'x'
# list_fields[24]['value'] = 'x'
fields = [[x['value'] for x in list_fields[y:y+length_of_side]] for y in range(0, number_of_cells) if y % length_of_side == 0]



player = {'name': None, 'unit': None}
default_names = ('Rocky', 'Anna_Botik', 'April_Showers', 'Dizzy', 'Leya', 'Bob_Link', 'Lucky_Fisher', 'Sam_Sung',
                 'Saad_Maan', 'Chris_P_Bacon', 'Batman_Bin', 'Lord_Brain', 'Keihanaiku', 'MacDonald_Berger', 'Beaver',
                 'Ann_Butts', 'Mia_Khalifa', 'Mr_Gopnik', 'oilala')

# for i in fields:
#     print(i)

menu = [{'title': 'Singleplayer', 'url_name': 'single'},
        {'title': 'Multiplayer', 'url_name': 'multi'},
        {'title': 'About', 'url_name': 'about'},
        # {'title': 'Learn', 'url_name': 'learn'},
        # {'title': 'Test', 'url_name': 'test'},
        # {'title': 'About', 'url_name': 'about'},
        ]

def index(request, *args, **kwargs):

    return redirect('single')

    # print()
    #
    # player = {'name': None, 'unit': None}
    # # a = str(random.randrange(10, 99, 1))
    # # u = random.choice(unit)
    # #
    # # print(f"{a = }")
    # # print(f"{u = }")
    # player['name'] = str(random.randrange(10, 99, 1))
    # player['unit'] = 'o'
    #
    # print(f"{request.session = }")
    # if request.session.session_key:
    #     print(f"{request.session.session_key = }")
    #
    # data = request.session.get('data', default=None)
    # if data:
    #     print(f"{data = }")
    #
    #
    #
    # # if request.method == 'POST':
    # #     print(f"{request.POST = }")
    # #     fields_index = request.POST.get('field_index', None)
    # #     # print(f"{fields_index = }")
    # #     if fields_index:
    # #         list_fields[int(fields_index)]['value'] = 'x'
    # #         print(f"{int(fields_index) = }")
    # #         print(f"{list_fields[int(fields_index[0])]['value'] = }")
    # #         fields = [[x['value'] for x in list_fields[y:y + length_of_side]] for y in range(0, number_of_cells) if
    # #                   y % 5 == 0]
    # #         for i in fields:
    # #             print(i)
    # #         data = fields
    # #         request.session['data'] = data
    #
    #
    # # fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # # fields_x = [5, 6]
    # # fields_o = [1, 2]
    # context = {
    #     'menu': menu,
    #     # 'title': menu[2]['title'],
    #     # 'choose_collection_form': choose_collection_form,
    #     # 'choose_collection': choose_collection,
    #     # 'words_records': words_records,
    #     'list_fields': list_fields,
    #     # 'fields_x': fields_x,
    #     # 'fields_o': fields_o,
    #     'player': player,
    #     'j_list_fields': json.dumps([x for x in range(number_of_cells)]),
    #     'str_list_fields': json.dumps([str(x) for x in range(number_of_cells)]),
    # }
    # return render(request, 'tictac/index.html', context=context)

# def index(request):
#     return render(request, "tictac/index.html")

def singleplayer(request, *args, **kwargs):
    global list_fields


    list_weights = [100 for x in range(number_of_cells)]
    weights = [[x for x in list_weights[y:y + length_of_side]] for y in range(0, number_of_cells) if
               y % length_of_side == 0]
    print()

    Testing.objects.create(
        name=str(uuid.uuid4()),
    )
    res = Testing.objects.all()
    print(res)
    print(f"Number of raws in BD: {len(res)}")


    status = 'game_on'
    winning_cells = []

    if request.method == 'GET' or request.POST.get('pos') == None:
        list_fields = [{'index': x, 'value': '.'} for x in range(number_of_cells)]
        print(f"{request.GET = }")
        fields = [[x['value'] for x in list_fields[y:y + length_of_side]] for y in range(0, number_of_cells) if
                  y % length_of_side == 0]
        status = 'game_on'
        # res = find_move(fields)
        res = find_weight(fields, 'o', 5, weights)

        fields[res['move'][0]][res['move'][1]] = 'o'

        list_fields = []
        jj = 0
        for row in fields:
            for x in row:
                list_fields.append({'index': jj, 'value': x})
                jj += 1

        for row in range(0, len(fields)):
            for column in range(0, len(fields[row])):
                print(fields[row][column] if fields[row][column] != ' ' else '.', end=' ')
            print()


    if request.method == 'POST':
        if request.POST.get('pos'):
            print(f"{request.POST = }")
            pos = int(request.POST.get('pos'))
            if list_fields[pos]['value'] == '.':
                list_fields[pos]['value'] = 'x'

                fields = [[x['value'] for x in list_fields[y:y + length_of_side]] for y in range(0, number_of_cells) if
                          y % length_of_side == 0]


                # res = find_move(fields)
                res = find_weight(fields, 'o', 5, weights)
                # return {'status': 'game_on', 'move': (row, column)}
                print(f"{res = }")
                if res['status'] == 'game_on':
                    fields[res['move'][0]][res['move'][1]] = 'o'
                else:
                    status = 'won'
                    winning_cells = res['cells']

                list_fields = []
                jj = 0
                for row in fields:
                    for x in row:
                        list_fields.append({'index': jj, 'value': x})
                        jj += 1


                for row in range(0, len(fields)):
                    for column in range(0, len(fields[row])):
                        print(fields[row][column] if fields[row][column] != ' ' else '.', end=' ')
                    print()


    # status = 'won'
    context = {
        'menu': menu,
        'list_fields': list_fields,
        'title': menu[0]['title'],
        'status': status,
        'winning_cells': winning_cells,
    }
    return render(request, 'tictac/single.html', context=context)

def multiplayer(request, *args, **kwargs):
    print()

    print(f"{request.session = }")
    # request.session['123'] = 123
    if not request.session.session_key:
        request.session.create()

    # In case of deleting session
    if not Session.objects.filter(session_key=request.session.session_key).exists():
        request.session.create()

    # session_key = request.session.session_key
    #
    # print(f"{session_key = }")


    form = PlayerNameForm(initial={'player_name': random.choice(default_names)})

    unit = ('x', 'y', 'o', 'w', 'e', 'h')
    player['unit'] = random.choice(unit)
    context = {
        'menu': menu,
        'title': menu[1]['title'],
        'list_fields': list_fields,
        'form': form,
        'player': player,
        'session_key': request.session.session_key,
    }
    return render(request, 'tictac/multi.html', context=context)

def about(request, *args, **kwargs):
    print()
    context = {
        'menu': menu,
        'title': menu[2]['title'],
    }
    return render(request, 'tictac/about.html', context=context)

def room(request, room_name):
    if request.method == 'GET':
        print(f"{request.GET = }")
    if request.method == 'POST':
        print(f"{request.POST = }")
    return render(request, "tictac/room.html", {"room_name": room_name})


def tic(request):
    if request.method == 'GET':
        print(f"{request.GET = }")
    if request.method == 'POST':
        print(f"{request.POST = }")
    return render(request, "tictac/tic.html")

