import math
import random


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


def find_line(fields, unit, win_line_length):
    empty = '.'
    win_line_tail_length = win_line_length // 2
    length_of_side = len(fields[0])
    for row in range(0, len(fields)):
        for column in range(0, len(fields[row])):
            if fields[row][column] == unit:

                # Vertical line
                line = 0
                coords = []
                possible_cells = []
                if row >= win_line_tail_length and row <= length_of_side - win_line_tail_length - 1:
                    for i in range(row - win_line_tail_length, row + win_line_tail_length + 1):
                        # print(f"field[{i}][{column}] {row}")
                        if fields[i][column] != unit:
                            continue
                        line += 1
                        coords.append((i, column))
                        if i > 0:
                            y1 = i - 1
                            if fields[y1][column] == empty:
                                possible_cells.append((y1, column))

                        # print(f"{i = } {row + win_line_tail_length = } {i = }")
                        if i < length_of_side - 1:
                            y1 = i + 1
                            if fields[y1][column] == empty:
                                possible_cells.append((y1, column))

                if line == win_line_length:
                    # print(f"{unit} won, field[{row}][{column}]")
                    result = unit, coords, possible_cells
                    return result

                # Horizontal line
                if column >= win_line_tail_length and column <= length_of_side - win_line_tail_length - 1:
                    if line < win_line_length:
                        line = 0
                        coords = []
                        possible_cells = []
                        for i in range(column - win_line_tail_length, column + win_line_tail_length + 1):
                            if fields[row][i] != unit:
                                continue
                            line += 1
                            coords.append((row, i))

                            if i > 0:
                                x1 = i - 1
                                if fields[row][x1] == empty:
                                    possible_cells.append((row, x1))
                            # print(f"{i = } {row + win_line_tail_length = } {i = }")
                            if i < length_of_side - 1:
                                x1 = i + 1
                                if fields[row][x1] == empty:
                                    possible_cells.append((row, x1))

                if line == win_line_length:
                    # print(f"{unit} won, field[{row}][{column}]")
                    result = unit, coords, possible_cells
                    return result

                if row >= win_line_tail_length and row <= length_of_side - win_line_tail_length - 1 and \
                        column >= win_line_tail_length and column <= length_of_side - win_line_tail_length - 1:
                    # print(f"{row = } {column = }")
                    line = 0
                    coords = []
                    possible_cells = []
                    # print(f"field[{row}][{column}]")
                    for i in range(-win_line_tail_length, win_line_tail_length + 1):
                        # print(f"field[{i}][{column}] {row}")
                        if fields[row + i][column + i] != unit:
                            # print(f"{row + i = } {column + i = }")
                            # print('break')
                            continue
                        # hh5555555555555
                        line += 1
                        coords.append((row + i, column + i))

                        if row + i > 0 and column + i > 0:
                            x1 = i - 1
                            if fields[row + x1][column + x1] == empty:
                                possible_cells.append((row + x1, column + x1))
                        # print(f"{i = } {row + win_line_tail_length = } {i = }")
                        if row + i < length_of_side - 1 and column + i < length_of_side - 1:
                            x1 = i + 1
                            if fields[row + x1][column + x1] == empty:
                                possible_cells.append((row + x1, column + x1))

                    if line == win_line_length:
                        # print(f"{unit} won, field[{row}][{column}]")
                        result = unit, coords, possible_cells
                        return result

                    if line < win_line_length:
                        line = 0
                        coords = []
                        possible_cells = []
                        for i in range(-win_line_tail_length, win_line_tail_length + 1):
                            # print(f"field[{i}][{column}] {row}")
                            if fields[row + i][column - i] != unit:
                                continue
                            line += 1
                            coords.append((row + i, column - i))

                            if row + i > 0 and row + i < length_of_side - 1 and column - i > 0 and column - i < length_of_side - 1:
                                x1 = i - 1
                                if fields[row + x1][column - x1] == empty:
                                    possible_cells.append((row + x1, column - x1))
                            # print(f"{i = } {row + win_line_tail_length = } {i = }")
                            if row + i > 0 and row + i < length_of_side - 1 and column - i > 0 and column - i < length_of_side - 1:
                                x1 = i + 1
                                if fields[row + x1][column - x1] == empty:
                                    possible_cells.append((row + x1, column - x1))

                        if line == win_line_length:
                            # print(f"{unit} won, field[{row}][{column}]")
                            result = unit, coords, possible_cells
                            return result


def find_move(fields):
    empty = '.'
    for i in range(4, 0, -1):
        res = find_line(fields, 'x', i)
        if res and len(res[2]) > 0:
            print(f"found {res[2]}")
            res = res[2][0]
        else:
            res = None
        if res:
            print(f"Found move for line with: {i} X-es")
            break
        print(f"nothing found for: {i} X-es ")
    if not res:
        print(f"Did not find a move, using random")
        while True:
            x = random.randint(0, len(fields) - 1)
            y = random.randint(0, len(fields) - 1)
            if fields[y][x] == empty:
                res = (y, x)
                break

    return res


def print_field(fields):
    for row in range(0, len(fields)):
        for column in range(0, len(fields[row])):
            if fields[row][column] == 100:
                print('...', end=' ')
            else:
                print(fields[row][column], end=' ')
        print()


def computer_move(fields):
    pass
    ...


def find_weight(fields, my_unit, win_line_length, weights):
    def calc_weight(variants, weights, number_of_my_units, unit_1):
        if len(variants) > 0:
            # print(f"is {j}st")
            print(f"{variants = }")
            print(f"{number_of_my_units = }")
            for i in variants:
                weights[i[0]][i[1]] += number_of_my_units ** 3
                if unit_1 == my_unit:
                    weights[i[0]][i[1]] += 1

    def compute(weights, unit_1, unit_2):
        for row in range(0, len(fields)):
            for column in range(0, len(fields[row])):
                if fields[row][column] == unit_1:
                    print(f"[{row}][{column}]")

                    # line
                    for j in range(win_line_length):
                        number_of_my_units = 0
                        variants = []
                        for i in range(-j, -j + win_line_length):
                            if column + i >= length_of_side:
                                variants = []
                                break
                            if column + i < 0:
                                variants = []
                                break
                            if fields[row][column + i] == unit_1:
                                number_of_my_units += 1
                            if fields[row][column + i] == unit_2:
                                variants = []
                                break
                            if fields[row][column + i] == empty:
                                variants.append((row, column + i))
                        calc_weight(variants, weights, number_of_my_units, unit_1)

                    # column
                    for j in range(win_line_length):
                        number_of_my_units = 0
                        variants = []
                        for i in range(-j, -j + win_line_length):
                            if row + i >= length_of_side:
                                variants = []
                                break
                            if row + i < 0:
                                variants = []
                                break
                            if fields[row + i][column] == unit_1:
                                number_of_my_units += 1
                            if fields[row + i][column] == unit_2:
                                variants = []
                                break
                            if fields[row + i][column] == empty:
                                variants.append((row + i, column))
                        calc_weight(variants, weights, number_of_my_units, unit_1)

                    # diagonal right bottom
                    for j in range(win_line_length):
                        number_of_my_units = 0
                        variants = []
                        for i in range(-j, -j + win_line_length):
                            if row + i >= length_of_side:
                                variants = []
                                break
                            if row + i < 0:
                                variants = []
                                break
                            if column + i >= length_of_side:
                                variants = []
                                break
                            if column + i < 0:
                                variants = []
                                break
                            if fields[row + i][column + i] == unit_1:
                                number_of_my_units += 1
                            if fields[row + i][column + i] == unit_2:
                                variants = []
                                break
                            if fields[row + i][column + i] == empty:
                                variants.append((row + i, column + i))
                        calc_weight(variants, weights, number_of_my_units, unit_1)

                    # diagonal right top
                    for j in range(win_line_length):
                        number_of_my_units = 0
                        variants = []
                        for i in range(-j, -j + win_line_length):
                            if row + i >= length_of_side:
                                variants = []
                                break
                            if row + i < 0:
                                variants = []
                                break
                            if column - i >= length_of_side:
                                variants = []
                                break
                            if column - i < 0:
                                variants = []
                                break
                            if fields[row + i][column - i] == unit_1:
                                number_of_my_units += 1
                            if fields[row + i][column - i] == unit_2:
                                variants = []
                                break
                            if fields[row + i][column - i] == empty:
                                variants.append((row + i, column - i))
                        calc_weight(variants, weights, number_of_my_units, unit_1)

    empty = '.'
    if my_unit == 'x':
        enemy_unit = 'o'
    else:
        enemy_unit = 'x'
    length_of_side = len(fields[0])

    # unit_1 = my_unit
    # unit_2 = enemy_unit
    compute(weights, my_unit, enemy_unit)
    compute(weights, enemy_unit, my_unit)

    for row in range(0, len(weights)):
        for column in range(0, len(weights[row])):
            if type(weights[row][column]) == float:
                weights[row][column] = math.ceil(weights[row][column])

    max_weight = max([max(x) for x in weights])


    if max_weight == 100:
        print(f"Did not find a move, using random")
        while True:
            x = random.randint(len(fields) // 3, (len(fields) - 1) // 3 * 2)
            y = random.randint(len(fields) // 3, (len(fields) - 1) // 3 * 2)
            if fields[y][x] == empty:
                return (y, x)

    print_field(weights)
    for row in range(0, len(weights)):
        for column in range(0, len(weights[row])):
            if weights[row][column] == max_weight:
                return (row, column)


if __name__ == "__main__":
    # length_of_side = 7
    # number_of_cells = length_of_side ** 2
    # list_fields = [{'index': x, 'value': '.'} for x in range(number_of_cells)]
    # fields = [[x['value'] for x in list_fields[y:y+length_of_side]]
    #           for y in range(0, number_of_cells) if y % length_of_side == 0]
    f = [
        '. . . . . . . . . .',
        '. . . . . . . . . .',
        '. . . o . . . . . .',
        '. . . x x x x . . .',
        '. . . . . . . . . .',
        '. . . . . . x . x .',
        '. . . . . . . x . x',
        '. . . . . . . . o .',
        '. . . . . . . . . .',
        '. . . . . . . . . .',
    ]
    f = [
        '. . . . . . . . . o',
        '. . . . . . . . . o',
        '. . . . . . . . . .',
        '. . . o . . . . . .',
        '. . . . . . . . . .',
        '. . . . . . . . . .',
        '. . . . . . . . . .',
        '. . . x . . . . . .',
        '. . . . . . . . . x',
        '. . . . . . . . . x',
    ]
    f1 = [x.split(' ') for x in f]
    # print(f"{f1 = }")
    fields = f1
    w = [
        '100 100 100 100 100 100 100 100 100 100',
        '100 100 100 100 100 100 100 100 100 100',
        '100 100 100 100 100 100 100 100 100 100',
        '100 100 100 100 100 100 100 100 100 100',
        '100 100 100 100 100 100 100 100 100 100',
        '100 100 100 100 100 100 100 100 100 100',
        '100 100 100 100 100 100 100 100 100 100',
        '100 100 100 100 100 100 100 100 100 100',
        '100 100 100 100 100 100 100 100 100 100',
        '100 100 100 100 100 100 100 100 100 100',
    ]
    w1 = [list(map(int, x.split(' '))) for x in w]
    # print(f"{f1 = }")
    weights = w1

    print_field(fields)

    # print_field(weights)
    res = find_weight(fields, 'x', 5, weights)

    print_field(weights)
    print(f"{res = }")

    # units = ('x', 'o')
    # unit = 'x'
    # win_line_length = 5
    # win_line_tail_length = win_line_length // 2
    # print(f"{win_line_tail_length = }")

    # res = check_win(fields, units, 2)

    # fields = computer_move(fields)

    # print(res)
    # print()

    # res = find_line(fields, 'x', 3)
    # print(f"{res = }")
    # if res and len(res[2]) > 0:
    #     res = res[2][0]
    # else:
    #     res = None

    # res = find_move(fields)
    # fields[res[0]][res[1]] = 'o'
    #
    # print()
    # print(res)
    # print_field(fields)

    # Алгоритм.
    # Проверка на победу любого из игроков
    # Проверка на заполненность всех полей
    #
    #
    # 1) Найти подряд 4 О и поставить О со свободной стороны
    # 2) Найти подряд 4 Х и поставить О со свободной стороны. Если свободных сторон 2 то сдаемся
    #
    # 3) Найти подряд 3 О и если их можно дополнить до 5 то поставить 4-ый О, сохранив все варианты
    # 4) Найти подряд 3 Х и если их может стать 5 то поставить с одной стороны О
    #
    # 5) Найти подряд 2 О и если их можно дополнить до 5 то поставить 3-ый О
    # 6) Найти подряд 2 Х и если их может стать 5 то поставить с одной стороны О
    #
    # 7) Найти О и если из него можно сделать в одну из сторон 5 О то поставить 2-ой О
    # 8) Найти Х и если из него можно сделать в одну из сторон 5 Х то поставить О
    #
    # 9) Поставить случайно О

    # старый
    # 1) если есть 4 подряд O то ставим О со свободной стороны
    # 1) если есть 4 подряд креста то ставим О со свободной стороны
    # 2) если есть 3 подряд креста то ставим О со свободной стороны
    # 3) если есть 2 подряд креста то ставим О со свободной стороны
    # 3) если есть 1 подряд крест то ставим О со свободной стороны
