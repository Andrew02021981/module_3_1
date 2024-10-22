calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    info_  = (len(string),string.upper(),string.lower())
    return info_

def is_contains(string, list_to_search):
    count_calls()
    if string.upper() in str(list_to_search).upper():
        return True
    else:
        return False

print(string_info('Москва'))
print(string_info('Ростов-на-Дону'))
print(is_contains('мИр',['Владимир', 'Ростов', 'Мирный']))
print(is_contains('Ток',['Казань','Владивосток','Берлин']))
print(is_contains('Рим',['Сочи','Калининград','Санкт-Петербург']))
print(calls)