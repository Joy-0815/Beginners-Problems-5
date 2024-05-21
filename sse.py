stringsList = ["abc","123","2332","aBBA","heelloo","1212","DcEfD"]

def first_last(strings):
    lista = []
    for word in strings:
        if len(word) >= 1 and word[0] == word[-1]:
            lista.append(word)
    return lista

print(first_last(stringsList))
