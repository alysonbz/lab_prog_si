#EXPERIMENTANDO METODOS NO PYTHON
fam = ['liz', 1.67, 'jeff', 1.9, 'mom', 1.70, 'dad', 1.8]

#EXIBINDO A POSIÇÃO DO ELEMENTO MAE NA LISTA COM .INDEX
print(fam.index('mom'))

#CONTANDO OS ELEMENTOS DA LISTA COM .COUNT
print(fam.count(1.67))

#INSERINDO ELEMENTOS NA LISTA COM O .APPEND
fam.append('uncle')
fam.append(1.80)
print(fam)
print(fam.index('uncle'))

#METODOS EM STRINGS
sister = str('liz')

#COLOCANDO A PRIMEIRA LETRA DO NOME EM CAIXA ALTA COM .CAPITALIZE
print(sister.capitalize())

#SUBSTITUINDO PARTES NO NOME COM .REPLACE
print(sister.replace('z','sa'))

#QUESTÕES (AULA 5)

#QUESTÕES 1, 2 e 3)
#string to experiment with: place
place = "poolhouse" 

# Use upper() on place: place up
place_up = place.upper()

#Print out place and place_up
print(place)
print(place_up)

#Print out the number of o's in place
print(place.count('o'))

#QUESTOES 4 E 5
#Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

#Print out the index of the element 20.0
print(areas.index(20.0))

#Print how often 9.50 appears in areas
print(areas.count(9.50))

#QUESTÕES 6, 7, 8 E 9
#Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

#Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.25)

#Print out areas
print(areas)

#Reverse the orders of the elements in the areas
areas.reverse()

#Print out areas
print(areas)