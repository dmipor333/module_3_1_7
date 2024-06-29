calls = 0
def count_calls():
    global calls
    calls = calls + 1
count_calls()
def string_info(string):
    string = (len(string), string.upper(), string.lower())
    return string
print(string_info('Copibara'))
print(string_info('Armageddon'))
count_calls()
def is_contains(string, list_to_search):
     string = string.lower()
     list_to_search = " ".join(list_to_search)
     list_to_search = list_to_search.lower()
     print(string in list_to_search)
     count_calls()
is_contains('Urban', ['urBAN', 'BaNaN', 'ban'])  #Urban ~ urBAN
is_contains('cicle', ['recycling', 'cyclic']) #No matches
print(calls)