import math
import random
import numpy as np


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
def elevarMatriz(d:int, p:int) -> list[list[int]]:
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

def productoDeMatrices(m, n):   #AUX
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



