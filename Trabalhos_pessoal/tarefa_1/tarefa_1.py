array = input("digite o array")
print(type(array))
array = array.split(" ")
print(array)


for _ in range (len(array)):
    array[_] = int(array[_])
    
array_ordenado = []*len(array)



while len(array) != 0:
    fnum = array[0]
    for posição in range (len(array)-1):
        if fnum> array[posição+1]:
            fnum = array[posição+1]
            
    array.remove(fnum)
    array_ordenado.append(fnum)


print(array_ordenado)
        