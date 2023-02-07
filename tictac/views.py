from django.shortcuts import render

length_of_side = 5
number_of_cells = length_of_side ** 2
list_fields = [{'index': x, 'value': ''} for x in range(number_of_cells)]
list_fields[4]['value'] = 'o'
list_fields[5]['value'] = 'x'
list_fields[23]['value'] = 'x'
list_fields[24]['value'] = 'x'
fields = [[x['value'] for x in list_fields[y:y+length_of_side]] for y in range(0, number_of_cells) if y % 5 == 0]

for i in fields:
    print(i)


def index(request, *args, **kwargs):

    print()

    print(f"{request.session = }")
    if request.session.session_key:
        print(f"{request.session.session_key = }")

    data = request.session.get('data', default=None)
    if data:
        print(f"{data = }")



    if request.method == 'POST':
        print(f"{request.POST = }")
        fields_index = request.POST.get('field_index', None)
        # print(f"{fields_index = }")
        if fields_index:
            list_fields[int(fields_index)]['value'] = 'x'
            print(f"{int(fields_index) = }")
            print(f"{list_fields[int(fields_index[0])]['value'] = }")
            fields = [[x['value'] for x in list_fields[y:y + length_of_side]] for y in range(0, number_of_cells) if
                      y % 5 == 0]
            for i in fields:
                print(i)
            data = fields
            request.session['data'] = data


    # fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # fields_x = [5, 6]
    # fields_o = [1, 2]
    context = {
        # 'menu': menu,
        # 'title': menu[2]['title'],
        # 'choose_collection_form': choose_collection_form,
        # 'choose_collection': choose_collection,
        # 'words_records': words_records,
        'list_fields': list_fields,
        # 'fields_x': fields_x,
        # 'fields_o': fields_o,
    }
    return render(request, 'tictac/index.html', context=context)
