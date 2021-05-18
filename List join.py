list1 = [c * 3 for c in 'asdfghjk']
list2 = [c * 3 for c in 'zxcvb']


def join(list_keys, list_values):
    result = {}

    for index, item in enumerate(list_keys):
        if index < len(list_values):
            result[item] = list_values[index]
        else:
            result[item] = None

    return result


result_dictionary = join(list1, list2)


for key, value in result_dictionary.items():
    print(f'keys: {key} values: {value}')
