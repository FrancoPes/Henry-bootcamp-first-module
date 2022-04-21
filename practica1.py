
#? 1. Transformar de decimal a binario
def NumeroBinario(numero): 
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        numero: Será el número que se convertirá a binario.
 
        NumeroBinario(12) debe retornar 1100
        NumeroBinario(2) debe retornar 10
        NumeroBinario(14) debe retornar 1110
    '''
    
    if numero > 0 :
            binario = ''
            while numero // 2 != 0:
                binario = str(numero % 2) + binario
                numero = numero // 2
            return int(str(1) + binario)
    elif numero == 0:
        return 0
    
    else:
            return None
        
print(NumeroBinario(20))




#? 2. Transformar de fraccion a binario
def Numerofraccionario(decimal): 
    '''
    Esta función recibe como parámetro un número entero decimal y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        decimal: Será el decimal que se convertirá a binario.
 
        NumeroBinario(0,5) debe retornar 1
        NumeroBinario(0.3125) debe retornar 0101
        NumeroBinario(14) debe retornar 1110
    '''
    
    if decimal < 1 :
            i = 0
            
            listabinario = []
            while decimal * 2 != 0:
                listabinario.append(int(decimal * 2))
                decimal = decimal * 2 - int(decimal * 2)
                i += 1
            decimal = '0,'
            for e in listabinario:
                decimal = decimal + str(e) 
                  
            return (decimal)
        
    elif decimal < 0:
            return None
print(Numerofraccionario(0.11111111111111111111111111111))       
