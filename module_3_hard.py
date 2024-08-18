uni_sum = 0


def calculate_structure_sum(*args):
    global uni_sum
    for item in args:
        if isinstance(item, int or float):
            uni_sum += item
        elif isinstance(item, str):
            uni_sum += len(item)
        elif isinstance(item, list or tuple or set):
            calculate_structure_sum(*item)
        elif isinstance(item, dict):
            calculate_structure_sum(*item.keys())
            calculate_structure_sum(*item.values())
        else:
            calculate_structure_sum(*item)
#        print(item, uni_sum)
    return uni_sum


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
