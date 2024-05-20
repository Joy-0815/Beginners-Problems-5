stringsList = ["abc","123","2332","aBBA","heelloo","1212","DcEfD"]

def first_last(strings):
    lista = []
    for num in strings:
        if num[0] == num[-1]:
            lista.append(num)
    return lista

print(first_last(stringsList))
