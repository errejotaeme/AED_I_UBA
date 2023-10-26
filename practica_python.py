import copy, csv, math, pprint, random
import numpy as np
from queue import LifoQueue as Pila
from queue import Queue as Cola



# RUTAS
ruta_archivo: str = '' #txt
ruta_archivo_2: str = '' #txt
ruta_archivo_binario: str = '' # imagenes, videos, pdfs, etc
ruta_notas: str = '' #csv





#E1-1
def imprimir_hola_mundo () -> str:
    print('Ejercicio1_1:\n','hola mundo')

#E1-2
def imprimir_un_verso() -> str:
    print('Ejercicio1_2:\n','linea 1\nlinea 2\nlinea 3\nlinea 4')

#E1-3
def raiz_de(n: int) -> float:
    return round(math.sqrt(n), 4)

#E1-4
def factorial_de(n: int) -> int:
    return math.factorial(n)

#E1-5
def perimetro(radio: int) -> float:
    return 2 * math.pi * radio

#E2-1
def imprimir_saludo(nombre: str) -> str:
    print(f'Hola {nombre}')

#E2-2
#raiz

#E2-3
def fahrenheit_a_celsius(t: float) -> float:
    return ((t - 32)*5)/9

#E2-4
def imprimir_dos_veces(estribillo: str) -> str:
    print(estribillo * 2)

#E2-5
def es_multiplo_de(n: int, m: int)-> bool:
    return (n % m) == 0

#E2-6
def es_par(n: int) -> bool:
    return es_multiplo_de(n, 2)

#E2-7
def cantidad_de_pizzas(comensales: int, min_porciones: int) -> int:
    if (comensales * min_porciones) % 8 == 0:
        return ((comensales * min_porciones) // 8)
    else:
        return (((comensales * min_porciones) // 8) + 1)

#E3-1
def alguno_es_0(n1: float, n2: float) -> bool:
    return (n1 == 0 or n2 == 0)

#E3-2
def ambos_son_0(n1: float, n2: float) -> bool:
    return (n1 == 0 and n1 == 0) 

#E3-3
def es_nombre_largo(nombre: str) -> bool:
    return (len(nombre) >= 3 and len(nombre) <= 8) 

#E3-4
def es_bisiesto(año: int) -> bool:
    return es_multiplo_de(año, 400) or (es_multiplo_de(año, 4) and not es_multiplo_de(año, 100))

#E4-1
def peso_pino(altura:int)-> int:
    if altura <= 3:
        return (altura * 100 * 3)
    else:
        return (900 + (altura - 3) * 100 * 2)

def es_peso_util(peso:int) -> bool:
    return peso >= 400 and peso <= 1000

def sirve_pino(altura: int) -> bool:
    return es_peso_util(peso_pino(altura))

#E5-1
def devolver_el_doble_si_es_par(numero: int) -> int:
    if es_par(numero):
        return numero * 2
    else:
        return numero

#E5-2    
def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if es_par(numero):
        return numero
    else:
        return numero + 1

#E5-3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if es_multiplo_de(numero, 9):
        res = numero * 3
    elif es_multiplo_de(numero, 3):
        res = numero * 2
    else:
        res = numero
    return res

#E5-4
def lindo_nombre(nombre: str) -> str:
    if len(nombre) >= 5:
        res = 'Tu nombre tiene muchas letras!'
    else:
        res = 'Tu nombre tiene menos de 5 caracteres'
    return res

#E5-5
def el_rango(numero:int) -> str:
    if numero < 5:
        res = 'Menor a 5'
    elif numero >= 10 and numero <= 20:
        res = 'Entre 10 y 20'
    elif numero > 20:
        res = 'Mayor a 20'
    else:
        res = 'otro'
    return res

#E5-6
def laburo(sexo: str, edad: int) -> str:
    if edad < 18:
        res = 'Andá de vacaciones'
    elif (edad >= 18) and (edad < 60) and (sexo == 'F'):
        res = 'Te toca trabajar'
    elif (edad >= 18) and (edad < 65) and (sexo == 'M'):
        res = 'Te toca trabajar'
    else:
        res = 'Andá de vacaciones'
    return res

#E6-1
def uno_diez():
    cont = 0
    while cont < 10:
        print(cont + 1)
        cont += 1
#E7-1        
def uno_diez_for():
   for i in range(10):
       print(i+1)

#E6-2
def pares_10_40() -> int:
    cont = 9
    while cont < 41:
        if es_par(cont):
            print(cont)
        cont += 1

#E7-2
def pares_10_40_for():
    for i in range(10, 41, 2):
        print(i)

#E6-3
def eco():
    cont = 0
    while cont < 10:
        print('eco ')
        cont += 1

#E7-3
def eco_for():
    for i in range(10):
        print('eco')

#E6-4
def cuenta_regresiva(n: int):
    while n >= 1:
        print(n)
        n -= 1
    print('Despegue!')

#E7-4
def cuenta_regresiva_for(n: int):
    for i in range(n):
        print(n-i)
    print('Despegue!')


#E6-5
def viaje_tiempo(partida: int, llegada: int):
    while partida > llegada + 1:
        partida -= 1
        print(f'Viajó un año al pasado, estamos en el año: {partida}')      
    print(f'Llegaste al año {llegada}!')

#E7-5
def viaje_tiempo_for(partida: int, llegada: int):
    for i in range(llegada, partida):
        print(f'Viajó un año al pasado, estamos en el año: {(partida-1) - i + llegada}')      
    print(f'Llegaste al año {llegada}!')

#E6-6
def monitoreo_viaje_tiempo(partida:int):
    while partida > -384 + 20:
        partida -= 20
        print(f'Viajó veinte años al pasado, estamos en el año: {partida}')
    print(f'Llegaste al año {partida} a.C., podes concer a Aristóteles!')

#E7-6
def monitoreo_viaje_tiempo_for(partida:int):
    for i in range(0, partida + 384, 20):
        if i <= 1:
            next
        else:
            print(f'Viajó veinte años al pasado, estamos en el año: {partida - i}')
    print(f'Llegaste al año {partida} a.C., podes conocer a Aristóteles!')



#PARTE I

#P1_E-1
def pertenece(s:list[int], e) -> bool:
    return e in s

def pertenece_2(s:list[int], e:int) -> bool:
    res:bool = False
    for i in range(len(s)):
        if s[i] == e:
            res = True       
    return res

def pertenece_3(s:list[int], e:int) -> bool:
    res:bool = False
    i:int = 0
    while i < len(s):
        if res == True:
            return res
        res = (s[i] == e)
        i+=1
    return res


#P1_E-2
def divideATodos(s:list[int], e:int)->bool:
    res:bool = True
    for i in range(len(s)):
        if s[i] % e == 0:
            continue
        else:
            res = False
    return res


#P1_E-3
def sumaTotal(s:list[int]) -> int:
    res:int = 0
    for i in range(len(s)):
        res += s[i]
    return res


#P1_E-4
def ordenados(s:list[int]) -> bool:
    res:bool = True
    for i in range(len(s)):
        if i == 0:
            continue
        if s[i-1] < s[i]:
            continue
        else:
            res = False
    return res
    

#P1_E-5
def mayorASiete(listaPalabras:list[str]) -> bool:
    res:bool = False
    for palabra in listaPalabras:
        if len(palabra) > 7:
            res = True
    return res
    


#P1_E-6
def palindromo(texto:str)-> bool:
    texto_original:str = texto.lower().replace(' ','')
    i:int = len(texto_original)
    texto_al_reves:str = ''
    while i > 0:
        texto_al_reves += texto_original[i-1]
        i-=1
    return texto_original == texto_al_reves


#P1_E-7
def tieneMinusculas(palabra:str) -> bool:  #AUX
    res = False
    for letra in palabra:
        if letra.islower():
            res = True
    return res

#60 <= ord('caracter') <= 90   <---- ASCII
def tieneMayusculas(palabra:str) -> bool:  #AUX
    res = False
    for letra in palabra:
        if letra.isupper():
            res = True
    return res

def tieneNumeros(palabra:str) -> bool:  #AUX
    res = False
    for letra in palabra:
        if letra.isnumeric():
            res = True
    return res

def fortalezaClave(clave:str) -> str:
    res:str = ''
    if (tieneMinusculas(clave) and 
        tieneMayusculas(clave) and
        tieneNumeros(clave) and
        len(clave) > 8):
        res = 'VERDE'
    elif (len(clave) < 5):
        res = 'ROJA'
    else:
        res = 'AMARILLA'
    return res

#P1_E-8
def saldo(transacciones:list[tuple[str, int]]) -> int:
    res:int = 0
    for movimiento in transacciones:
        if movimiento[0] == 'I':
            res += movimiento[1]
        elif movimiento[0] == 'R':
            res -= movimiento[1]
    return res

#P1_E-9
def tieneVocales(texto:str) -> bool:
    vocales:str = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    lista_de_vocales:list[str] = []
    for letra in texto:
        if (letra in vocales and not 
            letra in lista_de_vocales):
            lista_de_vocales.append(letra)
    return (len(lista_de_vocales) >= 3)
    

#PARTE II

#P2_E-1
def borrarPares(s:list[int]) -> list[int]:
    for i in range(1, len(s), 2):
        s[i] = 0
    return s

#P2_E-2
def borrarPares_2(s:list[int]) -> list[int]:
    lista_final:list[int] = []
    for i in range(len(s)):
        if (i % 2 == 0):
            lista_final.append(s[i])
        else:
            lista_final.append(0)
    return lista_final

#P2_E-3
def sinVocales(texto:str)-> str:
    vocales:str = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    cadena_salida:str = ''
    for letra in texto:
        if letra in vocales:
            continue
        cadena_salida += letra
    return cadena_salida

#P2_E-4
def reemplazaVocales(texto:str) -> str:
    vocales:str = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    cadena_salida:str = ''
    for letra in texto:
        if letra in vocales:
            cadena_salida += '-'
            continue
        cadena_salida += letra
    return cadena_salida

#P2_E-5
def daVuelta(texto:str) -> str:
    i:int = len(texto)
    texto_al_reves:str = ''
    while i > 0:
        texto_al_reves += texto[i-1]
        i-=1
    return texto_al_reves


#P2_E-6
def eliminarRepetidos(texto: str) -> str:
    texto_nuevo:str = ''
    for caracter in texto:
        if caracter == ' ':
            texto_nuevo += caracter
        if (caracter not in texto_nuevo):
            texto_nuevo += caracter
    return texto_nuevo


#P2_E-7
def promedio(notas:list[int]) -> float: #AUX
    total:int = 0
    for nota in notas:
        total += nota
    return (total / len(notas))

def todasMasDeCuatro(notas:list[int]) -> bool: #AUX
    res:bool = True
    for nota in notas:
        if nota < 4:
            res = False
    return res


def aprobado(notas:list[int]) -> int:
    res:bool = 0
    if (todasMasDeCuatro(notas) and
        promedio(notas) >= 7):
        res = 1
    if (todasMasDeCuatro(notas) and
        promedio(notas) < 7 and
        promedio(notas) >= 4):
        res = 2
    if ((not todasMasDeCuatro(notas)) or
        promedio(notas) < 4):
        res = 3
    return res


#P2_E-8
def ingresarNombre() -> list[str]:
    print('Ingresar nombres. Para finalizar ingresar "listo":')
    lista_final:list[str] = []
    while 'listo' not in lista_final:
        lista_final.append(input())
    return lista_final[:-1]


#P2_E-9
def monedero() -> list[tuple[str, int]]:
    movimientos:list[tuple[str, int]] = []
    condicion:bool = True
    while condicion:
        print('Para operar, ingrese:\n "C" para cargar créditos\n "D" para descontar créditos\n "X" para salir')
        entrada:str = input()
        if entrada == 'C':
            print('Ingresar monto a cargar:')
            movimientos.append(('C', input()))
            print('La operación fue exitosa.')
        if entrada == 'D':
            print('Ingresar monto a descontar:')
            movimientos.append(('D', input()))
            print('La operación fue exitosa.')
        if entrada == 'X':
            condicion = False
    return movimientos

#P2_E-10
def juego() -> list[int]:
    condicion:bool = True
    cartas:list[int] = []
    total:float = 0
    print('Empezó el juego! Se preguntará si desea seguir sacando cartas. Si la suma de las cartas es mayor a 7.5 pierde:')
    while condicion:
        if total > 7.5:
            print(f'Perdiste. tus cartas suman {total}.')
            condicion = False
        print('Sacar una carta? "SI" o "NO"')
        entrada:str = input()
        if entrada == 'SI':
            carta:int = random.randint(1,12)
            if carta == 8 or carta == 9:
                carta = random.randint(1,12)
            cartas.append(carta)
            if (carta == 10 or 
                carta == 11 or
                carta == 12):
                total += 0.5
            else:
                total += carta
        if entrada == 'NO':
            condicion = False
        if total > 7.5:
            print(f'Perdiste. tus cartas suman {total}.')
            condicion = False
    return cartas



#P2_E-11
def perteneceACadaUno(s:list[list[int]], e:int) -> list[bool]:
    res:list[bool] = []
    for i in range(len(s)):
        if pertenece(s[i], e):
            res.append(True)
        else: 
            res.append(False)
    return res


#P2_E-12
def esMatriz(s:list[list[int]]) -> bool:
    res:bool = True
    if len(s) == 0:
        res == False
    try:
        if len(s[0]) == 0:
            res = False
    except:
        res = False
    try:
        longitud:int = len(s[0])
        for i in range(len(s)):
            if len(s[i]) != longitud:
                res = False
    except:
        res = False
    return res

#P2_E-13
def filasOrdenadas(m:list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for i in range(len(m)):
        res.append(ordenados(m[i]))
    return res


#P2_E.5.4
def elevarMatriz(d:int, p:int) -> :np.array:
    m:np.array = np.random.randint(1,5, (d, d))
    res:np.array = m.copy()
    print('matriz original:\n', m)
    if p==0:
        for i in range(len(m)):
            for j in range(len(m[i])):
                if j==i:
                    res[i][j] = 1
                else:
                    res[i][j] = 0
    while (p-1) > 0:
        res = productoDeMatrices(res, m)
        p-=1        
    return res

def productoDeMatrices(m:np.array, n:np.array) -> np.array:   #AUX
    res:np.array = m.copy()
    for i in range(len(m)):
        for j in range(len(m[i])):
            vector_aux:np.array = n[:,j]
            res[i][j] = productoEscalar(m[i], vector_aux)
    return res    
            
def productoEscalar(u:np.array, v:np.array) -> int: #AUX
    res:int = 0
    for i in range(len(u)):
        res += u[i]*v[i]
    return res






# ARCHIVOS
#1.1
def contar_lineas(ruta: str) -> int:
    with open(ruta, 'r', encoding="utf-8") as archivo:
        lineas: list[str] = archivo.readlines()
    return len(lineas)


def contar_lineas_2(archivo: str) -> int: # Resuelto en clase
    a: archivo = open(archivo)
    n: int = 0
    while (a.readline() != ''):
        n += 1
    return n


#1.2
def existe_palabra(palabra: str, ruta: str) -> bool:
    with open(ruta, 'r', encoding="utf-8") as archivo:
        texto: str = archivo.read()
    texto = texto.replace('\n', ' ')
    return (palabra in texto)


#1.3
def cantidad_de_apariciones(ruta: str, palabra: str) -> int:
    with open(ruta, 'r', encoding="utf-8") as archivo:
        texto: str = archivo.read()
    texto = texto.replace('\n', ' ')
    return texto.count(palabra)

def cantidad_de_apariciones_2(ruta: str, palabra: str) -> int:    # Si no se permite utilizar count
    with open(ruta, 'r', encoding="utf-8") as archivo:
        texto: str = archivo.read()
    texto = texto.replace('\n', ' ')
    lista_de_palabras: list[str] = texto.split(' ')
    res: int = 0
    for item in lista_de_palabras:
        if item == palabra:
            res += 1
    return res

#2
def clonar_sin_comentarios(ruta: str) -> None:
    with open(ruta, 'r', encoding="utf-8") as archivo:
        lineas: list[str] = archivo.readlines()
        
    lista_aux: list[str] = []
    for linea in lineas:
        linea_aux: str = linea.strip() 
        if linea_aux == '':
            continue
        if linea_aux[0] == '#':
            continue
        else:
            lista_aux.append(linea)

    lineas_finales: str = '\n'.join(linea for linea in lista_aux)
    archivo = open(f'{ruta[:-4]}_sin_comentarios.txt', 'w', encoding='utf-8')
    archivo.write(lineas_finales)
    archivo.close()


def clonar_sin_comentarios_2(nombre_de_archivo: str) -> None: # Resuelto en clase
    archivo_de_entrada = open(nombre_de_archivo, "r")
    archivo_de_salida = open("nombre_de_otro_archivo", "w")
    cantidad_de_lineas_de_entrada = contar_lineas(nombre_de_archivo)

    while cantidad_de_lineas_de_entrada > 0:
        linea: str = archivo_de_entrada.readline()
        if not es_comentario(linea):
            archivo_de_salida.write(linea)
        cantidad_de_lineas_de_entrada -= 1

    archivo_de_entrada.close()
    archivo_de_salida.close()

def es_comentario(linea: str) -> bool: #AUX Resuelto en clase
    linea2 = linea.strip()
    if len(linea2) == 0:
        return False
    return linea2[0] == '#'

            
         
#3 
def invertir_orden(ruta: str) -> None:
    with open(ruta, 'r', encoding="utf-8") as archivo:
        lineas: list[str] = archivo.readlines()  
    lista_aux: list[str] = []
    conteo: int = len(lineas)
    
    while conteo > 0:
        lista_aux.append(lineas[conteo - 1])
        conteo -= 1 
    
    lineas_finales: str = '\n'.join(linea for linea in lista_aux)
    archivo = open(f'{ruta[:-4]}_reverso', 'w', encoding='utf-8')
    archivo.write(lineas_finales)
    archivo.close()
    
            
#4
def agregar_frase_al_final(ruta: str, frase: str) -> None:
    archivo = open(ruta, 'a', encoding="utf-8")
    archivo.write(frase) 
    
    
#5
def agregar_frase_al_inicio(ruta: str, frase: str) -> None:
    with open(ruta, 'r+', encoding="utf-8") as archivo:
        contenido: str = archivo.read()
        archivo.seek(0,0)
        archivo.truncate(0)
        archivo.write(f'{frase}\n{contenido}') 
        
        
#6
def binario(ruta: str) -> list[str]:
    with open(ruta, 'r+b') as archivo:
        secuencia: bytes = archivo.read()   
    cadena_aux: str = ''
       
    for entero in secuencia:       
        if (entero >= 65 and entero <= 90
            or entero >= 97 and entero <= 122
            or entero == 32
            or entero == 95):
            cadena_aux += chr(entero)
    
    palabras_legibles: list[str] = cadena_aux.split(' ')
    
    return [p for p in palabras_legibles if len(p) >= 5]
          
        
#7
def promedio_estudiante(lu: str) -> float:
    with open(ruta_notas, 'r') as archivo:
        filas = csv.reader(archivo)
        next(filas)
        tabla: list[list] = list(filas)

    lista_aux: list[float] = []
    
    for registro in tabla:
        if registro[0] == lu:
            lista_aux.append(float(registro[3]))
            
    return promedio(lista_aux)
            

def promedio(notas: list[float]) -> float: #AUX
    total: int = 0
    
    for nota in notas:
        total += nota
        
    return round((total / len(notas)), 2)


# PILAS
#8
def generar_numeros_al_azar(n: int, desde: int, hasta: int) -> Pila:
    pila_enteros: Pila[int] = Pila()
    conteo: int = 0
    
    while conteo < n:
        pila_enteros.put(random.randint(desde, hasta))
        conteo += 1
        
    return pila_enteros


#9
def cantidad_elementos_en_pila(p: Pila) -> int:
    lista_aux: list[any] = []
    
    while (p.empty() == False):
        lista_aux.insert(0, p.get())   # Reconstruye la pila agregando los elementos al inicio de la lista
        
    for item in lista_aux:
        p.put(item)
        
    return len(lista_aux)


#10
def buscar_el_maximo_en_pila(p: Pila) -> int:
    lista_aux: list = []
    
    while (p.empty() == False):
        lista_aux.insert(0, p.get())
    for item in lista_aux:
        p.put(item)
        
    return max(lista_aux)

def buscar_el_maximo_en_pila_2(p: Pila) -> int:  # Resuelto en clase
    pila_aux: Pila = Pila()    # En lugar de una lista e insert, utiliza otra pila
    maximo: int = p.get()
    pila_aux.put(maximo)
          
    while not p.empty():
        item: int = p.get()
        pila_aux.put(item)
        if item > maximo:
            maximo = item    
    while not pila_aux.empty():
        p.put(pila_aux.get())
        
    return maximo


#11              
def bien_balanceada(cadena: str) -> bool:
    res: bool = True
    cadena_aux = cadena.replace(' ','')
    pila_aux: Pila = Pila()
    for c in cadena_aux[::-1]:
        pila_aux.put(c)
    pila_aux.get()
    i: int = 0

    while not pila_aux.empty():
        elemento: str = pila_aux.get()
        if (i == 0 and es_operador(cadena_aux[i]) 
            and ord(cadena_aux[i]) != 45):
            res = False
            i += 1
            continue            
        if (pila_aux.empty() and 
            es_operador(elemento)):
            res = False
            continue
        if ((ord(cadena_aux[i]) == 40) and
            ord(elemento) == 45):
            i += 1
            continue              
        if (es_operador(cadena_aux[i]) and
            es_operador(elemento)):
            res = False
            i += 1
            continue
        if (es_operador(cadena_aux[i]) and
            ord(elemento) == 41):
            res = False
            i =+ 1
            continue
        if ((ord(cadena_aux[i]) == 40) and
            es_operador(elemento)):
            res = False
            i =+ 1
            continue
        if ((ord(cadena_aux[i]) == 40) and
            (ord(elemento) == 41)):
            res = False
            i =+ 1
            continue        
        i += 1
        
    return (res and orden_parentesis(cadena)) 

def es_operador(caracter: str) -> bool: #AUX
    res: bool = False
    
    if (ord(caracter) == 42 or
        ord(caracter) == 43 or
        ord(caracter) == 45 or
        ord(caracter) == 47 or
        ord(caracter) == 61):
        res = True
        
    return res

def orden_parentesis(cadena: str) -> bool: #AUX
    computo: int = 0
    
    for caracter in cadena:
        if computo < 0:
            return False
        elif ord(caracter) == 40:
            computo += 1
        elif ord(caracter) == 41:
            computo -= 1
            
    return (computo == 0)


#12
def postfix(cadena) -> int:
    pila_aux: Pila[int] = Pila()
    lista_aux: list[str] = cadena.split(' ')

    for item in lista_aux:
        if item.isnumeric():
            pila_aux.put(item)
        if not item.isnumeric():
            a: int = int(pila_aux.get())
            if pila_aux.empty():
                return 'Expresión incorrecta'
            b: int = int(pila_aux.get())
            if ord(item) == 43:
                pila_aux.put(b + a)
            if ord(item) == 45:
                pila_aux.put(b - a)
            if ord(item) == 42:
                pila_aux.put(b * a)
            if ord(item) == 47:
                pila_aux.put(b / a)
    
    return pila_aux.get()         
             

# COLAS
#13
def cola_de_enteros(n: int = 5, desde: int = 1, hasta: int = 100) -> Cola[int]:
    cola_z: Cola[int] = Cola()
    pila_aux: Pila[int] = generar_numeros_al_azar(n, desde, hasta)

    while n > 0:
        cola_z.put(pila_aux.get())
        n -=1

    return cola_z


#14
def cantidad_elementos_en_cola(c: Cola) -> int:
    lista_aux: list[any] = []
    
    while (c.empty() == False):        
        lista_aux.append(c.get())    # Se reconstruye la cola agregando los elem al final de la lista
    
    for item in lista_aux:
        c.put(item)
        
    return len(lista_aux)


#15
def buscar_el_maximo_en_cola(c: Cola) -> int:
    lista_aux: list = []
    
    while (c.empty() == False):
        lista_aux.append(c.get())
        
    for item in lista_aux:
        c.put(item)
        
    return max(lista_aux)

def buscar_el_maximo_en_cola_2(c: Cola) -> int:
    cola_aux: Cola = Cola()   # En lugar de una lista y append, utiliza otra cola
    maximo: int = c.get()
    cola_aux.put(maximo)   
    
    while not c.empty():
        item: int = c.get()
        cola_aux.put(item)
        if item > maximo:
            maximo = item   
            
    while not cola_aux.empty():
        c.put(cola_aux.get())  
        
    return maximo


#16
def armar_secuencia_de_bingo() -> Cola[int]: #AUX
    return cola_de_enteros(12, 0, 99)

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    lista_aux: list[int] = copy.deepcopy(carton)
    cola_aux: Cola = Cola()
    
    while not bolillero.empty():
        bola: int = bolillero.get()
        cola_aux.put(bola)
        try:
            lista_aux.remove(bola)
        except:
            continue
        
    while not cola_aux.empty():
        bolillero.put(cola_aux.get())
        
    return len(lista_aux)


#17
def n_pacientes_urgentes(c: Cola[(int, str, str)]) -> int:
    cola_aux: Cola = Cola()
    n_urgentes: int = 0
    
    while not c.empty():
        paciente: tuple[int, str, str] = c.get()
        cola_aux.put(paciente)
        if paciente[0] in range(1, 4):
            n_urgentes += 1
            
    while not cola_aux.empty():
        c.put(cola_aux.get())
        
    return n_urgentes

def generar_cola_pacientes(n: int = 50) -> Cola[(int, str, str)]: #AUX: genera una cola sintética de pacientes
    cola_pacientes: Cola = Cola()
    lista_prioridades: list[int] = [random.randint(1, 10) for _ in range(n)]
    lista_nombres: list[int] =  [random.randint(97, 122) for _ in range(n)]
    lista_especialidades: list[int] =  [random.randint(65, 80) for _ in range(n)]
    
    while n > 0:
        cola_pacientes.put((lista_prioridades.pop(),
                      (chr(lista_nombres.pop()) * 5),
                      chr(lista_especialidades.pop())))
        n -= 1
        
    return cola_pacientes


#18
def generar_cola_clientes(n: int = 30) -> Cola[(str, int, bool, bool)]: #AUX: genera una cola sintética de clientes
    cola_clientes: Cola = Cola()
    lista_nombres: list[int] = [random.randint(97, 122) for _ in range(n)]
    lista_dni: list[int] = []
    
    for i in range(n):
        lista_aux: list[int] = [random.randint(1, 9) for _ in range(8)]
        cadena_aux: str = ''.join(str(numero) for numero in lista_aux)
        lista_dni.append(int(cadena_aux))
    lista_cuentas: list[int] =  [random.randint(0, 1) for _ in range(n)]
    lista_prioridades: list[int] = [random.randint(0, 1) for _ in range(n)]
    
    while n > 0:
        cola_clientes.put(((chr(lista_nombres.pop()) * 5),
                           lista_dni.pop(),
                           bool(lista_cuentas.pop()),
                           bool(lista_prioridades.pop())))
        n -= 1
    return cola_clientes

def a_clientes(c: Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    cola_atencion: Cola[(str, int, bool, bool)] = Cola()
    n: int = cantidad_elementos_en_cola(c)    
    lista_aux: list[(str, int, bool, bool)] = [c.get() for _ in range(n)]   # Respalda la cola original
    re_encolar(c, lista_aux)    
    
    for _ in range(cantidad_elementos_en_cola(c)): # prioridad 1
        cliente = c.get()
        if cliente[3] == True:
            cola_atencion.put(cliente)
        else:
            c.put(cliente)                       
            
    for _ in range(cantidad_elementos_en_cola(c)): # prioridad 2
        cliente = c.get()
        if cliente[2] == True:
            cola_atencion.put(cliente)
        else:
            c.put(cliente)    
            
    while not c.empty():    # resto de clientes
        cola_atencion.put(c.get())
    re_encolar(c, lista_aux)    
    
    return cola_atencion
 
def re_encolar(cola: Cola, lista: list):
    for i in range(len(lista)):
        cola.put(lista[i])
    return cola
        


# DICCIONARIOS
#19
def agrupar_por_longitud(ruta: str) -> dict:
    with open(ruta, 'r', encoding="utf-8") as archivo:
        texto: str = archivo.read()
        
    texto = texto.replace('\n', ' ')
    lista_de_palabras: list[str] = recortar(texto, ' ')
    
    conteo: list[int] = []    
    for item in lista_de_palabras:
        conteo.append(len(item))

    longitudes: dict = {}
    for c in conteo:
        longitudes[c] = contar_ocurrencias(c, conteo)
        borrar_ocurrencias(c, conteo)
    
    return longitudes        
        
def contar_ocurrencias(n: any, lista: list[any]) -> int: #AUX
    return len([z for z in lista if z == n])

def borrar_ocurrencias(e:any, lista: list[any]) -> None: #AUX
    lista = [item for item in lista if item != e]

def recortar(cadena: str, corte: str) -> list[str]: #AUX
    res: list[int] = []                             # Si no se permite utilizar split 
    aux: str = ''                                   # funciona solo para un caracter como referencia para el corte
    for caracter in cadena:
        if caracter != corte:
            aux += caracter
        else:
            cadena = cadena[cadena.find(corte):]
            if aux != '':
                res.append(aux)
            aux = ''
    if aux != '':
        res.append(aux)
    return res

     
    
#20
def promedios_todos() -> dict:
    with open(ruta_notas, 'r') as archivo:
        filas = csv.reader(archivo)
        next(filas)
        tabla: list[list] = list(filas)

    lista_alumnos: list[str] = [] 
    for registro in tabla:
        if registro[0] not in lista_alumnos:
            lista_alumnos.append(registro[0])
    
    res: dict = {}     
    for alumno in lista_alumnos:
        res[alumno] = promedio_estudiante(alumno)
        
    return res


#21
def la_palabra_mas_frecuente(ruta: str) -> str:
    with open(ruta, 'r', encoding="utf-8") as archivo:
        texto: str = archivo.read()
        
    texto = texto.replace('\n', ' ')
    lista_de_palabras: list[str] = recortar(texto, ' ')
    res: str = lista_de_palabras[0]

    dicc_aux: dict = {}    
    for palabra in lista_de_palabras:
        dicc_aux[palabra] = contar_ocurrencias(palabra, lista_de_palabras)
        borrar_ocurrencias(palabra, lista_de_palabras)

    for clave in dicc_aux.keys():
        if dicc_aux[res] < dicc_aux[clave]:
            res = clave
    
    return res
            
       
#22
historiales: dict[str, Pila[str]] = {}
historiales_2: dict[str, Pila[str]] = {}

def visitar_sitio(h: dict, usuario: str, sitio: str) -> None:
    if usuario not in h.keys():
        pila_aux: Pila[str] = Pila()
        h[usuario] = pila_aux
        h[usuario].put(sitio)
    else:
        h[usuario].put(sitio)

def navegar_atras(h: dict, usuario: str) -> None:
    if usuario not in historiales_2.keys():
        pila_aux: Pila[str] = Pila()
        historiales_2[usuario] = pila_aux
        historiales_2[usuario].put(h[usuario].get())
    else:
        h[usuario].put(h[usuario].get)
        
def navegar_adelante(h: dict, usuario: str) -> None:
    h[usuario].put(historiales_2[usuario].get())
    
    

#23
inventario: dict = {}

def agregar_producto(inv: dict, nombre: str, precio: float, cantidad: int) -> None:
    if nombre in inv.keys():
        pass
    else: 
        inv[nombre] = {'precio':precio, 'cantidad': cantidad}
        
def actualizar_stock(inv: dict, nombre: str, cantidad: int) -> None:
    if nombre not in inv.keys():
        pass
    else:
        inv[nombre]['cantidad'] = cantidad
        
def actualizar_precio(inv: dict, nombre: str, precio: float) -> None:
    if nombre not in inv.keys():
        pass
    else:
        inv[nombre]['precio'] = precio

def calcular_valor_inventario(inv: dict) -> float:
    total: float = 0
    for clave in inv.keys():
        total += inv[clave]['cantidad'] * inv[clave]['precio']
    return total


