const_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Прописные буквы
const_lower = 'abcdefghijklmnopqrstuvwxyz'  # Строчные буквы


def cesar_code(_string):
    print(_string)
    fcount = 0
    ecount = 0
    k = 0
    shifr =''
    _list = []
    for i in range(len(_string)):
        if _string[i] == ' ':
            _list.append(_string[fcount:i])
            fcount = ecount + 1
        ecount += 1
    _list.append(_string[fcount:ecount])

    while k < len(_list):
        count = len(_list[k])
        for kk in range(len(_list[k])):
            if const_upper.find(_list[k][kk]) < 0 and const_lower.find(_list[k][kk]) < 0:
                count -= 1
        for kk in range(len(_list[k])):
            if const_upper.find(_list[k][kk]) >= 0 and (const_upper.find(_list[k][kk]) + count) <= 25:
                shifr += const_upper[const_upper.find(_list[k][kk]) + count]
            elif const_upper.find(_list[k][kk]) >= 0 and (const_upper.find(_list[k][kk]) + count) > 25:
                shifr += const_upper[const_upper.find(_list[k][kk]) + count - 26]
            elif const_lower.find(_list[k][kk]) >= 0 and const_lower.find(_list[k][kk]) + count <= 25:
                shifr += const_lower[const_lower.find(_list[k][kk]) + count]
            elif const_lower.find(_list[k][kk]) >= 0 and const_lower.find(_list[k][kk]) + count > 25:
                shifr += const_lower[const_lower.find(_list[k][kk]) + count-26]
            elif const_upper.find(_list[k][kk]) < 0 and const_lower.find(_list[k][kk]) < 0:
                shifr += _list[k][kk]
        if k < len(_list[k]) or len(_list[k]) < 3:
            shifr += ' '
        k += 1
    print(shifr)
cesar_code('Day, mice. "Year" is a mistake!')
