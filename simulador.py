"""Notas del codigo a tomar en cuenta para las modificaciones:
        1-Cada función encargada de realizar una instrucción recibe la memoria y el acumulador en binario, dentro de
        cada metodo esos valores se pasan a decimal pero a la hora de guardar dichos datos se vuelven a convertir en bianrio.

        2-En el acumulador no debe de aparecer ningún salto de linea al final del numero, solo pueden haber un string de un numero binario

"""



print("\033c",end="") #Borra la consola

ruta_variables = 'variables.txt'
ruta_acumulador = 'ac.txt'
ruta_es = 'es.txt'

#------------------------Lectura de el archivo .txt de las variables------------------------------------------------------------------
try:
    with open(ruta_variables, "r+") as archivo:
        variables = archivo.readlines()

except:
    print("Error al abrir el archivo con las variables")


#------------------------Lectura de el archivo .txt de los dispositivos de entrada y salida--------------------------------------------
try:
    with open(ruta_es, "r+") as archivo_es:
        entr_sal = archivo_es.readlines()

except:
    print("Error al abrir el archivo con las variables")






def reasignarMemoria(memoria ,resultado):
    """reescribe todo el archivo que contiene las variables  modificando el archivo con los cambios realizados

    Args:
        memoria (_type_): Memoria donde se va a guardar el nuevo dato
        resultado (_type_): Nuevo valor del espacio de memoria seleccionado
    """
    resultado = str(bin(resultado))[2:]
    for idx, linea in enumerate(variables):
        linea = linea.split(":")

        if linea[0] == str(memoria):
            variables[idx] = f"{linea[0]}:{resultado}\n"
            print(f"El puntero de memoria {linea[0]} a sido actualizado con el valor: {resultado} ({int(resultado, 2)})")
            break

    try:
        with open(ruta_variables, "w") as archivo:
            archivo.writelines(variables)

    except:
        print("Error al guardar los cambios en el archivo")



def reasignar_es(memoria ,resultado):
    """reescribe todo el archivo que contiene los dispositivos de E/S modificando el archivo con los cambios realizados

    Args:
        memoria (_type_): Memoria donde se va a guardar el nuevo dato
        resultado (_type_): Nuevo valor del espacio de memoria seleccionado
    """
    resultado = str(bin(resultado))[2:]
    for idx, linea in enumerate(entr_sal):
        linea = linea.split(":")

        if linea[0] == str(memoria):
            entr_sal[idx] = f"{linea[0]}:{resultado}\n"
            print(f"El dispositivo de E/S {linea[0]} a sido actualizado con el valor: {resultado} ({int(resultado, 2)})")
            break

    try:
        with open(ruta_es, "w") as archivo:
            archivo.writelines(entr_sal)

    except:
        print("Error al guardar los cambios en el archivo")



def asiganr_acumulador (ac):
    """Funcion encargada de reasignar el valor del acumulador

    Args:
        ac (int): acumulador
    """
    try:
        with open(ruta_acumulador, "w") as archivo:
            archivo.writelines(ac)

    except:
        print("Error al guardar los cambios en el archivo")

    return

def obtener_acumulador ():
    """Funcion encargada de obtener el valor del acumulador

    Returns:
        int: ultimo valor del acumulador
    """
    with open(ruta_acumulador, "r") as archivo: #Se abre el archivo para realizar la lectura
            acumulador = archivo.read()
    return acumulador



def separador():
    """Metodo para visualmente separar en la terminal cada instrucción
    """
    print("----------------------------------------------------------------------------------------------------")




# Set de instrucciones
def inst1(m1):
    """Carga de memoria 1 hacia AC

    Args:
        m1 (string): memoria 1
    """
    
    m1 = int(m1, 2) # Se convierte a decimal

    for linea in variables:
        linea = linea.split(":")

        if linea[0] == str(m1):
            asiganr_acumulador(linea[1].strip())
            print(f"El acumulador ha cambiado al valor: {obtener_acumulador()} ({int(obtener_acumulador(), 2)})")
            break
       
    separador()

def inst2(m1):
    """Almacenar en memoria 1 desde AC

    Args:
        m1 (int): memoria 1
    """
    
    m1 = int(m1, 2) # Se convierte a decimal
    ac = int(obtener_acumulador(), 2) # Se convierte a decimal

    reasignarMemoria(m1,ac)
    separador()
            
    
    

def inst3(m1):
    """Suma: memoria 1 + AC

    Args:
        m1 (int): memoria 1
    """
    
    
    m1 = int(m1, 2)  # Se convierte a decimal
    ac = int(obtener_acumulador(), 2) #Se comvierte el acumulador a decimal
    for linea in variables:
        linea = linea.split(":")
        if linea[0] == str(m1):
            valor_memoria = int(linea[1],2)
            resultado_suma =  valor_memoria + ac
            asiganr_acumulador(str(bin(resultado_suma)[2:]))
           
            print("El resultado de la suma es: ", resultado_suma)  # Actualizar el acumulador con el resultado de la suma
            print(f"El acumulador ha cambiado al valor: {obtener_acumulador()} ({int(obtener_acumulador(), 2)})")
            break
        
    separador()

def inst4 (m1, m2):
    """Suma: memoria 1 + memoria 2 + AC

    Args:
        m1 (int): memoria 1
        m2 (int): memoria 2
        ac (int): acumulador
    """
    

    m1 = int(m1, 2)  # Se convierte a decimal
    m2 = int(m2, 2)  # Se convierte a decimal
    ac = int(obtener_acumulador(), 2) #Se comvierte el acumulador a decimal
    
    
    for linea in variables:
        linea = linea.split(":")
        if linea[0] == str(m1):
            valor_memoria1 = int(linea[1],2)
            break
       
            
    for linea2 in variables:
        linea2 = linea2.split(":")
        if linea2[0] == str(m2):
            valor_memoria2 = int(linea2[1],2)
            resultado_suma =  valor_memoria1 + valor_memoria2 + ac
            asiganr_acumulador(str(bin(resultado_suma)[2:]))
            print("El resultado de la suma es: ", resultado_suma)  # Actualizar el acumulador con el resultado de la suma
            print(f"El acumulador ha cambiado al valor: {obtener_acumulador()} ({int(obtener_acumulador(), 2)})")
            break
        
    separador()
    

def inst5 (m1):
    """Resta: AC – memoria 1, almacena en AC

    Args:
        m1 (int): memoria 1
        ac (int): acumulador
    """
    
    m1 = int(m1, 2)  # Se convierte a decimal
    ac = int(obtener_acumulador(), 2) #Se comvierte el acumulador a decimal
    for linea in variables:
        linea = linea.split(":")
        if linea[0] == str(m1):
            valor_memoria = int(linea[1],2)
            resultado_resta =  ac - valor_memoria
            asiganr_acumulador(str(bin(resultado_resta)[2:]))  
            print(f"El resultado de la resta es: {resultado_resta}")  # Actualizar el acumulador con el resultado de la suma
            print(f"El acumulador ha cambiado al valor: {obtener_acumulador()} ({int(obtener_acumulador(), 2)})")
            break
        
    separador()

def inst6 (m1, m2):
    """Resta: AC – memoria 1, almacena en memoria 2

    Args:
        m1 (int): memoria 1
        m2 (int): memoria 2
        ac (int): acumulador
    """
    m1 = int(m1, 2)  # Se convierte a decimal
    m2 = int(m2, 2)  # Se convierte a decimal
    ac = int(obtener_acumulador(), 2) #Se convierte el acumulador a decimal
    for linea in variables:
        linea = linea.split(":")
        if linea[0] == str(m1):
            valor_memoria = int(linea[1],2)
            resultado_resta =  ac - valor_memoria
            print("El resultado de la resta es: ", resultado_resta)  # Actualizar el acumulador con el resultado de la suma
            break
       

    reasignarMemoria(m2, resultado_resta)
    separador()



def inst7 (m1):
    """Multiplicación: memoria 1 x AC, almacena en AC

    Args:
        m1 (int): memoria 1
        ac (int): acumulador
    """

    
    m1 = int(m1, 2)  # Se convierte a decimal
    ac = int(obtener_acumulador(), 2) #Se comvierte el acumulador a decimal
    for linea in variables:
        linea = linea.split(":")
        if linea[0] == str(m1):
            valor_memoria = int(linea[1],2)
            resultado_multi =  ac * valor_memoria
            asiganr_acumulador(str(bin(resultado_multi)[2:]))
            print("El resultado de la multiplicacion es: ", resultado_multi)  # Actualizar el acumulador con el resultado de la suma
            print(f"El acumulador ha cambiado al valor: {obtener_acumulador()} ({int(obtener_acumulador(), 2)})")
            break
        
    separador()

#Adicionales---------------------------------------------
def inst8 (m1, m2):
    """Suma: memoria 1 + memoria 2, almacena en memoria 1


    Args:
        m1 (_type_): Memoria1
        m2 (_type_): Memoria2
    """

    m1 = int(m1, 2)  # Se convierte a decimal
    m2 = int(m2, 2)  # Se convierte a decimal
    
    
    for linea in variables:
        linea = linea.split(":")
        if linea[0] == str(m1):
            valor_memoria1 = int(linea[1],2)
            break
        
            
    for linea2 in variables:
        linea2 = linea2.split(":")
        if linea2[0] == str(m2):
            valor_memoria2 = int(linea2[1],2)
            resultado_suma =  valor_memoria1 + valor_memoria2
            resultado_suma = str(bin(resultado_suma)[2:])
            print("El resultado de la suma es: ", resultado_suma)  # Actualizar el acumulador con el resultado de la suma
            break
       

    reasignarMemoria(m1, resultado_suma)
    separador()


def inst9 (m1, m2):
    """Multiplicación: memoria 1 x AC, almacena en memoria 2


    Args:
        m1 (_type_): Memoria1
        m2 (_type_): Memoria2
    """

    m1 = int(m1, 2)  # Se convierte a decimal
    m2 = int(m2, 2)  # Se convierte a decimal
    ac = int(obtener_acumulador(), 2) #Se comvierte el acumulador a decimal
    
    for linea in variables:
        linea = linea.split(":")
        if linea[0] == str(m1):
            valor_memoria1 = int(linea[1],2)
            break
        
            
    for linea2 in variables:
        linea2 = linea2.split(":")
        if linea2[0] == str(m2):
            valor_memoria2 = int(linea2[1],2)
            resultado_multi =  valor_memoria1 * ac
            print(f"El resultado de la multiplicación es: {bin(resultado_multi)[2:]} ({resultado_multi})")  # Actualizar el acumulador con el resultado de la suma
            break
        

    reasignarMemoria(m2, resultado_multi)
    separador()



def inst10 (m1):
    """División: AC / memoria 1, almacena en AC

    Args:
        m1 (string): memoria 1
        ac (string): acumulador
    """

    
    m1 = int(m1, 2)  # Se convierte a decimal
    ac = int(obtener_acumulador() ,2) #Se comvierte el acumulador a decimal
    for linea in variables:
        linea = linea.split(":")
        if linea[0] == str(m1):
            valor_memoria = int(linea[1],2)
            resultado_div =  ac / valor_memoria
            asiganr_acumulador(str(bin(int(resultado_div))[2:]) )
            print("El resultado de la división es: ", resultado_div)  # Actualizar el acumulador con el resultado de la suma
            print(f"Nuevo valor del acumulador: {obtener_acumulador()} ({int(obtener_acumulador(), 2)})")
            break
        
    separador()



def inst11 (m1, m2):
    """División: AC / memoria 1, almacena en memoria 2

    Args:
        m1 (_type_): Memoria1
        m2 (_type_): Memoria2
    """

    m1 = int(m1, 2)  # Se convierte a decimal
    m2 = int(m2, 2)  # Se convierte a decimal
    ac = int(obtener_acumulador(), 2) #Se comvierte el acumulador a decimal

    for linea in variables:
        linea = linea.split(":")
        if linea[0] == str(m1):
            valor_memoria = int(linea[1],2)
            resultado_div =  int(ac / valor_memoria)
            print(f"El resultado de la división es: {bin(resultado_div)[2:]} ({resultado_div})")  # Actualizar el acumulador con el resultado de la suma
            break
        

    reasignarMemoria(m2, resultado_div)
    separador()


def inst12 (m1):
    """Carga en el acumulador el valor del dispositivo de E/S (m1(Memoria 1))

    Args:
        m1 (string): memoria 1
        ac (string): acumulador
    """

    
    m1 = int(m1, 2) # Se convierte a decimal

    for linea in entr_sal:
        linea = linea.split(":")
        if linea[0] == str(m1):
            asiganr_acumulador(str(linea[1].strip()))
            print(f"Nuevo valor del acumulador: {obtener_acumulador()} ({int(obtener_acumulador(), 2)})")
            break
       
    separador()


def inst13(m1):
    """Guardar en E/S desde AC, almacena el contenido de AC en un dispositivo de E/S

    Args:
        m1 (int): memoria 1 (dispositivo de entrada y salida)
    """
    
    m1 = int(m1, 2) # Se convierte a decimal
    ac = int(obtener_acumulador(), 2) # Se convierte a decimal

    reasignar_es(m1, ac)
    separador()



def simulador():
    """Metodo principal encargado de la simulacion.
       Inicialmente se abre el archivo de las instrucciones y se procede a realizar la lectura de las mismas.
       Luego se abren casos en donde si la instrucción coincide mediante los primeros 4 bits(en binario) con alguna de las 
       instrucciones ya predeterminadas se llama a la funcion encargada de dicha instrucción.
    """
    
    ruta_instrucciones = 'instrucciones.txt'


    try:
        with open(ruta_instrucciones, "r") as archivo: #Se abre el archivo para realizar la lectura
            instrucciones = archivo.readlines()

            for linea in instrucciones:
                #Segmentacion de la instruccion
                linea = linea.split("=")
                
                instruccion = linea[1][:4]  #4 Bits
                memoria1 = linea[1] [4:15] #11 Bits
                memoria2 = linea[1] [15:26] #11 Bits
                
                if instruccion == "0001":
                    print(linea[0])
                    inst1(memoria1)
                    
                elif instruccion == "0010":
                    print(linea[0])
                    inst2(memoria1)
                    
                elif instruccion == "0011":
                    print(linea[0])
                    inst3(memoria1)
                    
                elif instruccion == "0100":
                    print(linea[0])
                    inst4(memoria1, memoria2)
                    
                elif instruccion == "0101":
                    print(linea[0])
                    inst5(memoria1)
                    
                elif instruccion == "0110":
                    print(linea[0])
                    inst6(memoria1, memoria2)
                    
                elif instruccion == "0111":
                    print(linea[0])
                    inst7(memoria1)

                elif instruccion == "1000":
                    print(linea[0])
                    inst8(memoria1, memoria2)
                elif instruccion == "1001":
                    print(linea[0])
                    inst9(memoria1, memoria2)

                elif instruccion == "1010":
                    print(linea[0])
                    inst10(memoria1)

                elif instruccion == "1011":
                    print(linea[0])
                    inst11(memoria1, memoria2)

                elif instruccion == "1100":
                    print(linea[0])
                    inst12(memoria1)

                elif instruccion == "1101":
                    print(linea[0])
                    inst13(memoria1)

                else:
                    print("Error: Instrucciones fuera de rango, revise los primeros 4 bits de la instrucción: ", linea[0])

            print(f"El valor final del acumulador corresponde a: {obtener_acumulador()} ({int(obtener_acumulador(),2)})")


    except:
        print("Error con el archivo")
        return



simulador() #Ejecución del simulador