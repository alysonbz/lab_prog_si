#Questão 1 e 1.1
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.5
areas = ["Hallway",hall,"Kitchen", kit, "Livingroom", liv, "Bedroom", bed,"Bathroom",   bath]
print(areas)

#Questão 2
listaA = [1,3,4,2]
print(listaA)
listaB = [1,2,3],[4,5,7]
print(listaB)
listaC = [1+2, "a" * 5, 3]
print(listaC)
#Todas as listas estão corretas; Listas comuns, e listas dentro de listas

#Questão 3
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
house = [["hallway", hall],
         ["kitchen", kit],
         ["Living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]
print(house)
print(type(house))

#Questão 4
areas = ["hallway", 11.25, "kitchen", 18.0, "Living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print(areas[1])
print(areas[-1])
print(areas[5])

#Questão 5
areas = ["hallway", 11.25, "kitchen", 18.0, "Living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
eat_sleep_area = areas[3] + areas[5]
print(eat_sleep_area)

#Questão 6
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
downstairs = areas[:6]
upstairs = areas[-4:]
print("Downstairs:", downstairs)
print("Upstairs:", upstairs)

#Questão abcd
#c) A float: the bathroom area

#Questão 7
areas = ["hallway", 11.25,
         "kitchen", 18.0, "Chill Zone",
         20.0, "bedroom", 10.75,
         "bathroom", 10.50]
print(areas)

#Questão 8
areas = ["hallway", 11.25, "kitchen", 18.0,
         "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]
areas_1 = areas + ["poolhouse", 24.5]
areas_2 = areas_1 + ["garage", 15.5]
print(areas_2)

#Questão 9
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = areas.copy()  # Alternativamente, areas[:] também funciona
areas_copy[0] = 5.0
print("Lista original:", areas)
print("Lista modificada:", areas_copy)



