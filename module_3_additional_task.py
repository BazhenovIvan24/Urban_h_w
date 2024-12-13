def calculate_structure_sum(*args):
    total_sum = 0


    def sum_element(element):
        nonlocal total_sum
        if isinstance(element, (int, float)):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, list):
            for item in element:
                sum_element(item)
        elif isinstance(element, tuple):
            for item in element:
                sum_element(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                sum_element(key)
                sum_element(value)
        elif element is not None and isinstance(element, set) or isinstance(element, frozenset):  # Обработка множеств
            for item in element:
                sum_element(item)
        elif element is not None and hasattr(element, '__len__') and not isinstance(element, (str, bytes)):
            total_sum += len(element)


    sum_element(args[0])

    return total_sum



data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]


result = calculate_structure_sum(data_structure)

print(result)


