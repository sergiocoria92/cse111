

def main (): #def es la palabra clave para definir una función en Python. 
    #main() es el nombre de la función principal. No recibe parámetros en este caso. 
    # Los dos puntos : indican que el bloque de código que sigue pertenece a esta función.
    end = float (input ("give me your final odometer in milles: "))
    start = float (input ("give me your inicial odometer in milles: "))
    gallons = float (input ("give me the gallons: "))
    
    mpg = miles_per_gallon (end, start, gallons) #Aquí llamamos a la función miles_per_gallon() y le pasamos los tres valores obtenidos (end, start, gallons).
    #El resultado de esa función se almacena en la variable mpg
    lp100k = lp100k_from_mpg (mpg) #Se llama a lp100k_from_mpg(mpg), pasando mpg como argumento.
    #Se almacena el resultado en la variable lp100k.
    
    print (f"your car's fuel consumption is {mpg:.2f} miles per gallon")
    print (f"your car's fuel consumption is {lp100k:.2f} liters per 100 kilometers")



def miles_per_gallon (end, start, gallons):  #def indica que estamos definiendo una función.
    #miles_per_gallon es el nombre de la función.
    #(end, start, gallons) son los parámetros, es decir, los valores que recibe la
    # función cuando es llamada.
    
    return (end - start) / gallons #return devuelve el resultado para que pueda ser usado en el código.


    
def lp100k_from_mpg (mpg):
    
    return 235.215 / mpg if mpg != 0 else float('inf')

main () #Esto inicia el programa. Sin esta línea, el código no haría nada porque 
#las funciones solo se definen pero nunca se ejecutan.

    