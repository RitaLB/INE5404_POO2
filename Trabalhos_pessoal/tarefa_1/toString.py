"""Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
        """
def main():
 return
    


def ordena():
    array = input("digite o array")
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


    return array_ordenado

def toString(array):
    """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
        """
    nstring = str(array)
    return nstring

main()