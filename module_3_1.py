calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(str1):
    result = (len(tuple(str1)), str1.upper(), str1.lower())
    count_calls()
    return result


def is_contains(str1, list_to_search):
    for i in list_to_search:
        if str(i.lower()) == str1.lower():
            bool_list = True
            break
        else:
            bool_list = False

    count_calls()
    return bool_list



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)