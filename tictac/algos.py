def check_win(fields, units, win_line_length):
    win_line_tail_length = win_line_length // 2
    length_of_side = len(fields[0])
    for row in range(0, len(fields)):
        for column in range(0, len(fields[row])):
            for unit in units:
                if fields[row][column] == unit:

                    line = 0
                    if row >= win_line_tail_length and row <= length_of_side - win_line_tail_length - 1:
                        for i in range(row - win_line_tail_length, row + win_line_tail_length + 1):
                            # print(f"field[{i}][{column}] {row}")
                            if fields[i][column] != unit:
                                break
                            line += 1

                    if line == win_line_length:
                        # print(f"{unit} won, field[{row}][{column}]")
                        return unit

                    if column >= win_line_tail_length and column <= length_of_side - win_line_tail_length - 1:
                        if line < win_line_length:
                            line = 0
                            for i in range(column - win_line_tail_length, column + win_line_tail_length + 1):
                                if fields[row][i] != unit:
                                    break
                                line += 1

                    if line == win_line_length:
                        # print(f"{unit} won, field[{row}][{column}]")
                        return unit

                    if row >= win_line_tail_length and row <= length_of_side - win_line_tail_length - 1 and \
                            column >= win_line_tail_length and column <= length_of_side - win_line_tail_length - 1:
                        line = 0
                        # print(f"field[{row}][{column}]")
                        for i in range(-win_line_tail_length, win_line_tail_length + 1):
                            # print(f"field[{i}][{column}] {row}")
                            if fields[row + i][column + i] != unit:
                                break
                            line += 1

                        if line < win_line_length:
                            line = 0
                            for i in range(-win_line_tail_length, win_line_tail_length + 1):
                                # print(f"field[{i}][{column}] {row}")
                                if fields[row + i][column - i] != unit:
                                    break
                                line += 1

                    if line == win_line_length:
                        # print(f"{unit} won, field[{row}][{column}]")
                        return unit

if __name__ == "__main__":

    length_of_side = 7
    number_of_cells = length_of_side ** 2
    list_fields = [{'index': x, 'value': '='} for x in range(number_of_cells)]




    # fields = [[x['value'] for x in list_fields[y:y+length_of_side]]
    #           for y in range(0, number_of_cells) if y % length_of_side == 0]
    f = [
        '= = = = = = =',
        '= = = = = = =',
        '= = = = = = =',
        '= = = = = = =',
        '= = = = = = =',
        '= = = = = = =',
        '= = = = = = =',
    ]

    f = [
        '= = = = = x =',
        '= x x = x = =',
        '= = x x x x =',
        '= = = = x x =',
        '= = o = = = =',
        '= = = = x x =',
        '= = x x x x x',
    ]

    f = [
        'x x = = = = =',
        '= x x = = = =',
        '= = = x = = =',
        '= = = x x = =',
        '= = = = x x =',
        '= = = = = x =',
        '= = = = = = =',
    ]

    f = [
        'x x x x x = =',
        '= = = = = x =',
        '= o = = x = x',
        '= = o = = x x',
        '= = x o = x =',
        '= x = x o = =',
        '= = x x = o =',
    ]
    f1 = [x.split(' ') for x in f]
    # print(f"{f1 = }")
    fields = f1

    # fields[2][1] = 'x'
    # fields[2][2] = 'x'
    # fields[2][3] = 'x'
    # fields[2][4] = 'x'
    # fields[2][5] = 'x'
    #
    # fields[2][1] = 'x'
    # fields[2][2] = 'x'
    # fields[2][3] = 'x'
    # fields[2][4] = 'x'
    # fields[2][5] = 'x'

    # for i, v in enumerate(list_fields):
    #     print(v['value'], end=' ')
    #     if (i+1) % length_of_side == 0:
    #         print()
    #
    # print()
    #
    # for i in fields:
    #     print(*i)
    #
    # print()
    #
    # print(fields[2][1])



    # print()

    for row in range(0, len(fields)):
        for column in range(0, len(fields[row])):
            print(fields[row][column], end=' ')
        print()

    print()






    units = ('x', 'o')
    # unit = 'x'
    win_line_length = 5
    # win_line_tail_length = win_line_length // 2
    # print(f"{win_line_tail_length = }")

    res = check_win(fields, units, win_line_length)

    print(res)
    print()




