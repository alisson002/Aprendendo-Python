frutas = ['maçã', 'banana', 'pera', 'uva']
print(frutas)#imprime a lista toda

print(frutas[0])#primeiro elemento
print(frutas[1])#segundo elemento
print(frutas[-1])#ultimo elemento
print(frutas[-2])#penultimo elemento

frutas[2] = 'melancia'#troca o elemento
print(frutas)

del frutas[2]#remove o elemento e reorganiza a lista
print(frutas)

frutas.sort()#organiza por ordem alfabetica no caso de strings
print(frutas)

frutas = ['maçã', 'banana', 'pera', 'uva', 'amora', 'melão']
frutas.sort()#organiza em ordem alfabetica
frutas.reverse()#inverte a ordem da lista
print(frutas)

frutas = ['maçã', 'banana', 'pera', 'uva', 'amora', 'melão']
frutas.reverse()#inverte a ordem da lista
print(frutas)

print(len(frutas))#retorna quantos elementos tem na lista

frutas = ['maçã', 'banana', 'pera', 'uva', 'amora', 'melão']
for i in frutas:
    print(i)#lista todos os elementos da lista
    
for i in frutas:
    if i == 'uva':
        print('elemento encontrado')
    
    print(i)
    
print(frutas[1:4])#imprime os elementos de 1 a 3
