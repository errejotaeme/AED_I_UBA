{-
------------------
LISTA DE FUNCIONES
------------------

esPar :: Integer -> Bool
esMultiploDeN :: Integer -> Integer -> Bool
esPrimo :: Int -> Bool
siguientePrimo :: Int -> Int

crearTupla:: a -> b -> (a, b)
primeraComponente :: (a, b) -> a
segundaComponente :: (a, b) -> b
cambiarPosicion :: (a, b) -> (b, a)
sonIgualesSinOrden :: Eq(t) => (t, t) -> (t, t) -> Bool
componentesIguales :: Eq(t) => (t, t) -> Bool

sonIguales :: Eq(t) => t -> t -> Bool
estaEnLaTupla :: Eq(c) => c -> (c, c) -> Bool
laOtraComponente :: Eq(t) => t -> (t,t) -> t
primero :: tx -> ty -> tx
segundo :: tx -> ty -> ty
sumatoria :: [Int] -> Int
longitud :: [t] -> Int
ultimo :: [t] -> t
principio :: [t] -> [t]
reverso :: [t] -> [t]
pertenece :: Eq(t) => t -> [t] -> Bool
hayRepetidos :: (Eq t) => [t] -> Bool
todosDistintos :: (Eq t) => [t] -> Bool
todosIguales :: (Eq t) => [t] -> Bool
agregarAlFinal :: t -> [t] -> [t]
quitar :: (Eq t) => t -> [t] -> [t]
quitarTodos :: (Eq t) => t -> [t] -> [t]
eliminarRepetidos :: (Eq t) => [t] -> [t]
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
capicua :: (Eq t) => [t] -> Bool
valorMaximoEnListaZ :: [Integer] -> Integer
valorMinimoEnListaZ :: [Integer] -> Integer
sumarN :: Integer -> [Integer] -> [Integer]
sumarElPrimero :: [Integer] -> [Integer] 
sumarElUltimo :: [Integer] -> [Integer] 
soloParesEnLista :: [Integer] -> [Integer]
multiplosDeN :: Integer -> [Integer] -> [Integer]
ocurrencias :: Eq(t) => t -> [t] -> Integer -> Integer
sacarBlancosRepetidos :: [Char] -> [Char]
contarPalabras :: [Char] -> Integer
extraerPrimerPalabra :: [Char] -> [Char]
borrarPrimerPalabra :: [Char] -> [Char]
palabras :: [Char] -> [[Char]]
palabraMasLarga :: [Char] -> [Char]
aplanar :: [[Char]] -> [Char]
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
sumaAcumulada :: (Num t) => [t] -> [t]
descomponerEnPrimos :: [Integer] -> [[Integer]]

-}

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

obtDivAux :: Integer -> Integer -> Integer --AUX
obtDivAux 1 _ = 1
obtDivAux p q | q == p = p
              | (p `mod` q) == 0 = q
              | (p `mod` q) /= 0 = obtDivAux p (q + 1)

minDivAux :: Integer -> Integer --AUX
minDivAux n = obtDivAux n (2)

esPrimo :: Integer -> Bool
esPrimo 1 = False
esPrimo n = n == minDivAux n

siguientePrimo :: Integer -> Integer
siguientePrimo primo | esPrimo(primo + 1) == True = (primo + 1)
                     | esPrimo(primo + 1) == False = siguientePrimo(primo + 1)


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




-- LISTAS

pertenece :: Eq(t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) | e == x = True
                   | e /= x = pertenece e xs
                   | otherwise = False


sonIguales :: Eq(t) => t -> t -> Bool
sonIguales x y = x == y

estaEnLaTupla :: Eq(c) => c -> (c, c) -> Bool
estaEnLaTupla c (a,b) = (c == a) || (c == b)

laOtraComponente :: Eq(t) => t -> (t,t) -> t
laOtraComponente componente (a, b) | componente == a = b
                                   | componente == b = a

ocurrencias :: Eq(t) => t -> [t] -> Integer -> Integer 
ocurrencias _ [] indice = indice
ocurrencias e (x:xs) indice | e == x = ocurrencias e xs (indice + 1)
                            | otherwise = ocurrencias e xs indice

primero :: tx -> ty -> tx
primero x y = x

segundo :: tx -> ty -> ty
segundo x y = y


longitud :: [t] -> Int 
longitud (_:xs) = 1 + longitud xs


ultimo :: [t] -> t 
ultimo l = l!! ((longitud l) - 1)


principio :: [t] -> [t]
principio [_] = []
principio (x:xs) = (x:(principio xs))


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


descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos [x] = (primosDeN x 2 []) : []
descomponerEnPrimos (x:xs) = (primosDeN x 2 []) : [] ++ descomponerEnPrimos xs

primosDeN :: Integer -> Integer -> [Integer] -> [Integer] --AUX
primosDeN n p lista_primos | esPrimo n = [n]
                           | not (esFactor n p) = primosDeN n (siguientePrimo p) lista_primos 
                           | (esFactor n p) && (esPrimo (div n p)) = lista_primos ++ [p, (div n p)]
                           | (esFactor n p) && not (esPrimo (div n p)) = primosDeN (div n p) (p) ((p:) lista_primos)
                           | otherwise = lista_primos
                               
esFactor :: Integer -> Integer -> Bool --AUX
esFactor n p = mod n p == 0

