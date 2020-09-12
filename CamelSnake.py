def camelcase(snakecase):
    str_lst = snakecase.split("_")
    cs=''
    for i in range(1, len(str_lst)):
        str_lst[i] = str_lst[i].capitalize()
        cs = cs+str_lst[i]
    return str_lst[0]+cs


def snake_case(camelCase):
    sc = ''
    for ch in camelCase:
        if ch.upper() == ch :
            sc= sc+'_'+ch.lower()
        else: sc = sc + ch
    return sc

print(camelcase("snake_case_convert"))

print(snake_case("camelCaseConvert"))