first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
#4) Na linha 6 concatenar as listas first e second usando o operado + e armazene em uma nova lista chamada full. Print a lista full na linha 7.

full = first + second
print(full)

#5) Na linha 9 use a função sorted() para  ordenar os elementos da lista full e armazene a reposta da função em uma nova lista, full_sorted. A função sorted recebe 2 argumentos: full e outro padrão da função: reverse,  que indica o tipo ordenamento. Neste caso, faça reverse = True.
full_sorted = sorted(full, reverse = True)

#6)print a lista full_sorted    
print(full_sorted)