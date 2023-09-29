
-- NUMEROS

-- dado un número natural, extrae su dı́gito de las unidades
digitoUnidades :: Integer -> Integer
digitoUnidades x | x < 10 = x
                 | x > 10 = x `mod` 10

-- dado un número natural, extrae su dı́gito de las decenas
digitoDecenas :: Integer -> Integer
digitoDecenas x | x < 100 = (x - digitoUnidades(x)) `div` 10
                | x > 100 = digitoUnidades((x - digitoUnidades(x)) `div` 10)
                | otherwise = 0

esMultiploDe :: Integer -> Integer -> Integer
esMultiploDe z n | n == 0 = 0
                 | n == 1 = z
                 | z `mod` n == 0 = z
                 | otherwise = 0

esPar :: Integer -> Bool
esPar z | z `mod` 2 == 0 = True
        | otherwise = False


maxRegionesEnElPlano :: Integer -> Integer
maxRegionesEnElPlano 0 = 1
maxRegionesEnElPlano lineas_trazadas = (maxRegionesEnElPlano (lineas_trazadas - 1)) + lineas_trazadas


--PRIMOS
divisoresDeN :: Integer -> Integer -> [Integer] --AUX
divisoresDeN _ 1 = [1]
divisoresDeN dividendo divisor | dividendo `mod` divisor == 0 = divisor:[] ++ (divisoresDeN dividendo (divisor - 1))
                               | otherwise = [] ++ (divisoresDeN dividendo (divisor - 1))

divisoresPrimosDeN :: Integer -> Integer -> [Integer] --AUX
divisoresPrimosDeN _ 1 = []
divisoresPrimosDeN dividendo divisor | not (esPrimo divisor) = [] ++ (divisoresPrimosDeN dividendo (divisor - 1))
                                     | dividendo `mod` divisor == 0 = divisor:[] ++ (divisoresPrimosDeN dividendo (divisor - 1))
                                     | otherwise = [] ++ (divisoresPrimosDeN dividendo (divisor - 1))

esFactor :: Integer -> Integer -> Bool --AUX
esFactor n p = mod n p == 0

primosDeN :: Integer -> Integer -> [Integer] -> [Integer] --AUX
primosDeN n _ _ | n <= 1 = []
primosDeN n p lista_primos | esPrimo n = [n]
                           | not (esFactor n p) = primosDeN n (siguientePrimo p) lista_primos 
                           | (esFactor n p) && (esPrimo (div n p)) = lista_primos ++ [p, (div n p)]
                           | (esFactor n p) && not (esPrimo (div n p)) = primosDeN (div n p) (p) ((p:) lista_primos)
                           | otherwise = lista_primos  

factoresPrimosDeN :: Integer -> [Integer] --PRIN
factoresPrimosDeN n = divisoresPrimosDeN n n

esPrimo :: Integer -> Bool --PRIN
esPrimo n = (divisoresDeN n n) == [n, 1]

siguientePrimo :: Integer -> Integer --PRIN
siguientePrimo n | esPrimo (n + 1) = (n + 1)
                 | otherwise = siguientePrimo (n + 1)

anteriorPrimo :: Integer -> Integer --PRIN
anteriorPrimo n | esPrimo (n - 1) = (n - 1)
                | otherwise = anteriorPrimo (n - 1)

listaDePrimosAnteriores :: Integer -> [Integer] --PRIN
listaDePrimosAnteriores 1 = []
listaDePrimosAnteriores n | esPrimo (n - 1) = (n - 1):[] ++ listaDePrimosAnteriores (n - 1)
                          | otherwise = [] ++ listaDePrimosAnteriores (n - 1)

descomponerEnPrimos :: [Integer] -> [[Integer]] --PRIN
descomponerEnPrimos [] = []
descomponerEnPrimos [x] = (primosDeN x 2 []) : []
descomponerEnPrimos (x:xs) = (primosDeN x 2 []) : [] ++ descomponerEnPrimos xs


--CONGRUENCIA
sonCongruentes :: Integer -> Integer -> Integer -> Bool
sonCongruentes a b n = mod (a - b) n == 0


--COMBINACIONES
factorial :: Integer -> Integer --AUX
factorial n | n == 0 = 1
            | otherwise = n * factorial (n-1)  

numeroCombinatorio :: Integer -> Integer -> Integer --PRIN
numeroCombinatorio n k | k > n = 0
                       | otherwise = div (factorial n) ((factorial k)*(factorial (n - k)))


--CONVERTIR NUMEROS A DISTINTAS BASES
baseDecimalAOtraBase :: Integer -> Integer -> [Integer] -> [Integer] --AUX
baseDecimalAOtraBase n base res | n < base = (mod n base):res
                            | n >= base = baseDecimalAOtraBase (div n base) base ((mod n base):res)

otraBaseABaseDecimal :: [Integer] -> Integer -> Integer -> Integer --AUX
otraBaseABaseDecimal [res] base n = n + res
otraBaseABaseDecimal (res:restos) base n = otraBaseABaseDecimal restos base ((n + res) * base)


baseDecimalABaseN :: Integer -> Integer -> [Integer] --PRIN
baseDecimalABaseN n base = baseDecimalAOtraBase n base []

baseNABaseDecimal :: [Integer] -> Integer -> Integer --PRIN
baseNABaseDecimal n_ario base_n = otraBaseABaseDecimal n_ario base_n 0



--TUPLAS
productoEscalarR2 :: (Float, Float) -> (Float, Float) -> Float
productoEscalarR2 (a, b) (c, d) = (a*c) + (b*d)

distanciaPuntosR2:: (Float, Float) -> (Float, Float) -> Float
distanciaPuntosR2 (a, b) (c, d) = sqrt(((a - c)**2) + ((b - d)**2))

crearTupla:: a -> b -> (a, b)
crearTupla a b = (a, b)

primeraComponente :: (a, b) -> a
primeraComponente (a, _) = a

segundaComponente :: (a, b) -> b
segundaComponente (_,b) = b

cambiarPosicion :: (a, b) -> (b, a)
cambiarPosicion (a, b) = (b, a)

sonIgualesSinOrden :: Eq(t) => (t, t) -> (t, t) -> Bool
sonIgualesSinOrden (a, b) (c, d) | (a == c) && (b == d) = True
                                 | (a == d) && (b == c) = True
                                 | otherwise = False  

componentesIguales :: Eq(t) => (t, t) -> Bool
componentesIguales tupla = primeraComponente tupla == segundaComponente tupla

estaEnLaTupla :: Eq(c) => c -> (c, c) -> Bool
estaEnLaTupla c (a,b) = (c == a) || (c == b)

laOtraComponente :: Eq(t) => t -> (t,t) -> t
laOtraComponente componente (a, b) | componente == a = b
                                   | componente == b = a


-- LISTAS
primero :: [t] -> t
primero (x:_) = x

ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

enesimo :: [t] -> Int -> t
enesimo (x:_) 0 = x
enesimo (_:xs) n = enesimo xs (n-1)

longitud :: [t] -> Integer
longitud [] = 0
longitud [x] = 1
longitud (x:xs) = 1 + longitud xs

principio :: [t] -> [t]
principio [] = []
principio [_] = []
principio (x:xs) = x:[] ++ principio xs

alReves :: [t] -> [t]
alReves [] = []
alReves (x:xs) = alReves xs ++ [x]

pertenece :: Eq(t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e [x] = e == x
pertenece e (x:xs) | e /= x = pertenece e xs
                   | otherwise = True 

sonIguales :: Eq(t) => t -> t -> Bool
sonIguales x y = x == y

ocurrencias :: Eq(t) => t -> [t] -> Integer -> Integer 
ocurrencias _ [] indice = indice
ocurrencias e (x:xs) indice | e == x = ocurrencias e xs (indice + 1)
                            | otherwise = ocurrencias e xs indice

ultimo2 :: [t] -> t 
ultimo2 l = l!! ((longitud l) - 1)

reverso :: [t] -> [t]
reverso l | longitud l == 1 = l
          | longitud l > 1 = [ultimo l] ++ reverso (principio l)

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:xs) = (x == y) && todosIguales (y:xs)

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:xs) = ((pertenece x xs) == False) && todosDistintos xs

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos l | todosIguales l == True = True
               | todosDistintos l == False = True
               | otherwise = False

estaEnLaLista :: Eq(t) => t -> [t] -> Bool --AUX
estaEnLaLista _ [] = False
estaEnLaLista item (x:xs) | item == x = True
                          | otherwise = estaEnLaLista item xs

quitar :: (Eq t) => t -> [t] -> [t]
quitar item lista | not (estaEnLaLista item lista) = lista
                  | (estaEnLaLista item lista) = quitarPrimerItem item lista []

agregarAlFinal :: t -> [t] -> [t] --AUX
agregarAlFinal i [] = [i]
agregarAlFinal i (x:xs) = (x:((agregarAlFinal i) xs))

quitarPrimerItem :: (Eq t) => t -> [t] -> [t] -> [t] --AUX
quitarPrimerItem i (x:xs) lista_final | i /= x = quitarPrimerItem i xs (agregarAlFinal x lista_final)
                                      | i == x = lista_final ++ xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos item lista | not (estaEnLaLista item lista) = lista
                       | (estaEnLaLista item lista) = quitarTodos item (quitar item lista)

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos lista | not (hayRepetidos lista) = lista 
                        | hayRepetidos lista = filtrarRepetidos lista 0
                                                       
filtrarRepetidos :: Eq(t) => [t] -> Int -> [t] --AUX
filtrarRepetidos lista indice | indice == longitud lista = lista
                              | not (hayRepetidos lista) = filtrarRepetidos lista (indice + 1)
                              | hayRepetidos lista = filtrarRepetidos ((lista!!indice) : (quitarTodos (lista!!indice) lista)) (indice + 1)


mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos lista_a lista_b | (compararListas lista_a lista_b) && (compararListas lista_b lista_a) = True
                                | otherwise = False

compararListas :: Eq(t) => [t] -> [t] -> Bool --AUX
compararListas [] lista = True
compararListas (x:xs) lista = (estaEnLaLista x lista) && (compararListas xs lista)

capicua :: (Eq t) => [t] -> Bool
capicua [_] = True
capicua lista = lista == reverso lista

sumatoria :: [Integer] -> Integer 
sumatoria [] = 0
sumatoria (x:xs) = sumatoria xs + x

productoria :: [Integer] -> Integer 
productoria [] = 1
productoria (x:xs) = x * productoria xs

valorMaximoEnListaZ :: [Integer] -> Integer
valorMaximoEnListaZ [x] = x
valorMaximoEnListaZ (x:xs) = obtenerMayor x xs 0

obtenerMayor :: Integer -> [Integer] -> Integer -> Integer --AUX
obtenerMayor n [] mayor = mayor
obtenerMayor n (x:xs) mayor | n == x = obtenerMayor n xs n
                            | n > x = obtenerMayor n xs n
                            | n < x = obtenerMayor x xs x

sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = [n]
sumarN n [x] = [(n + x)]
sumarN n (x:xs) = (n + x) : (sumarN n xs)

sumarElPrimero :: [Integer] -> [Integer] 
sumarElPrimero [x] = [x + x]
sumarElPrimero (x:xs) = (x + x) : (sumarN x xs)

sumarElUltimo :: [Integer] -> [Integer] 
sumarElUltimo [x] = [x + x]
sumarElUltimo (x:xs) = (x + (ultimo (x:xs))) : (sumarN (ultimo (x:xs)) xs)

soloParesEnLista :: [Integer] -> [Integer]
soloParesEnLista [] = []
soloParesEnLista [x] | esPar x = [x]
                     | otherwise = []
soloParesEnLista (x:xs) | esPar x = (x):(soloParesEnLista xs)
                        | otherwise = soloParesEnLista xs

esMultiploDeN :: Integer -> Integer -> Bool --AUX
esMultiploDeN 0 0 = True
esMultiploDeN _ 0 = False
esMultiploDeN z n | z `mod` n == 0 = True
                  | otherwise = False

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n [x] | esMultiploDeN x n = [x]
                   | otherwise = []
multiplosDeN n (x:xs) | esMultiploDeN x n = (x) : (multiplosDeN n xs)
                      | otherwise = multiplosDeN n xs


valorMinimoEnListaZ :: [Integer] -> Integer
valorMinimoEnListaZ [x] = x
valorMinimoEnListaZ (x:xs) = obtenerMenor x xs 0

obtenerMenor :: Integer -> [Integer] -> Integer -> Integer --AUX
obtenerMenor n [] menor = menor
obtenerMenor n (x:xs) menor | n == x = obtenerMenor n xs n
                            | n < x = obtenerMenor n xs n
                            | n > x = obtenerMenor x xs x

ordenar :: [Integer] -> [Integer]
ordenar [x] = [x]
ordenar s = reverso (ordenarDecreciente s)

ordenarDecreciente:: [Integer] -> [Integer] --AUX
ordenarDecreciente [x] = [x]
ordenarDecreciente s = valorMaximoEnListaZ s : ordenarDecreciente (quitar (valorMaximoEnListaZ s) s)

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:xs) | (x /= ' ') = x : sacarBlancosRepetidos xs
                             | (x == ' ') && (head xs == ' ') = sacarBlancosRepetidos xs
                             | otherwise = x : sacarBlancosRepetidos xs 

contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras [x] | x == ' ' = 0
                   | otherwise = 1
contarPalabras (x:xs) | (x /= ' ') && (head xs == ' ') = 1 + contarPalabras (sacarBlancosRepetidos xs)
                      | otherwise = contarPalabras (sacarBlancosRepetidos xs)

extraerPrimerPalabra :: [Char] -> [Char] --AUX
extraerPrimerPalabra [] = []
extraerPrimerPalabra [x] | x == ' ' = []
                   | otherwise = [x]
extraerPrimerPalabra (x:xs) | (x == ' ') && (head xs /= ' ') = [] ++ extraerPrimerPalabra xs
                      | (x /= ' ') && (head xs == ' ') = [x]
                      | (x /= ' ') = [x] ++ extraerPrimerPalabra xs
                      | otherwise = xs

borrarPrimerPalabra :: [Char] -> [Char] --AUX
borrarPrimerPalabra [] = []
borrarPrimerPalabra (x:xs) | x /= ' ' = borrarPrimerPalabra xs
                           | otherwise = xs
                           
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras [x] = [[x]]
palabras (x:xs) | x == ' ' = palabras xs
                | x /= ' ' =  ((extraerPrimerPalabra (x:xs)):) [] ++ palabras (borrarPrimerPalabra (sacarBlancosRepetidos (x:xs))) 
        
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga lista = cadenaMax (palabras lista)

cadenaMax :: [[Char]] -> [Char] --AUX
cadenaMax [x] = x
cadenaMax (x:xs) = obtenerCadenaMax x xs []

obtenerCadenaMax :: [Char] -> [[Char]] -> [Char] -> [Char] --AUX
obtenerCadenaMax c [] mayor = mayor
obtenerCadenaMax c (x:xs) mayor | longitud c == longitud x = obtenerCadenaMax c xs c
                                | longitud c > longitud x = obtenerCadenaMax c xs c
                                | longitud c < longitud x = obtenerCadenaMax x xs x

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ (aplanar xs)

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos [x] = x
aplanarConBlancos (x:xs) = x ++ [' '] ++ (aplanarConBlancos xs)

aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:xs) n = x ++ (nBlancos n) ++ (aplanarConNBlancos xs n)

nBlancos :: Integer -> [Char] --AUX
nBlancos n | n == 0 = []
           | otherwise = [' '] ++ nBlancos (n-1)

sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x:xs) = sumaAcuAux (x:xs) 0 

sumaAcuAux :: (Num t) => [t] -> t -> [t]
sumaAcuAux [x] val = [x + val]
sumaAcuAux (x:xs) val = (x + val): sumaAcuAux xs (val + x) 


--TRIANGULO DE PASCAL
pascal :: Integer -> IO()
pascal n = mapM_ print (coeficientesPascal n)

coeficientesPascal :: Integer -> [[Integer]] --AUX
coeficientesPascal 0 = [[1]]
coeficientesPascal n = [[1]] ++ (generarListaDeListas [1] n) 

generarListaDeListas :: [Integer] -> Integer-> [[Integer]] --AUX
generarListaDeListas lista 0 = []
generarListaDeListas lista i = (unirListaDeCoeficientes lista):[] ++ generarListaDeListas (unirListaDeCoeficientes lista) (i - 1)

unirListaDeCoeficientes :: [Integer] -> [Integer] --AUX
unirListaDeCoeficientes (x:xs) = [x] ++ listaDeCoeficientes (x:xs)

listaDeCoeficientes :: [Integer] -> [Integer] --AUX
listaDeCoeficientes [_] = [1]
listaDeCoeficientes (x:xs) = ((x + (head xs)):)[] ++ (listaDeCoeficientes xs)