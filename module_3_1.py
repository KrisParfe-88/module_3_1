calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    tup = (len(string), string.upper(), string.lower())
    count_calls()
    return tup


def is_contains(string, list_to_search):
    list_to_search = [i.lower() for i in list_to_search]
    search = string.lower() in list_to_search
    count_calls()
    return search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
