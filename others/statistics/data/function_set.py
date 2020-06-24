def max_value(data):
    return max(data)

def min_value(data):
    return min(data)

def range_value(data):
    return max_value(data) - min_value(data)

def number_repeats(lista):
    times = {}
    for i in lista:
        if i not in times:
            times[i] = 0
        times[i] += 1 
    return times


def percent(lista, data):
    number_repeats = number_repeats(lista, data)
    return number_repeats / len(lista)


def arithmetic_median(lista):
    return sum(lista) / len(lista)


def median(lista):
    lista.sort() 
    eve = len(lista) / 2
    if even % 1 != 0:
        return lista[int(even)]
    return (lista[int(even)] + lista[int(even - 1)]) / 2


def mode(dic):
    dic = number_repeats(dic)
    i2 = max(dic.values())
    for i in dic:
        if dic[i] == i2:
            return i


 
a = [1,1,1,2,3,4,5,5]
a2 = number_repeats(a)
print(mode(a2))
    