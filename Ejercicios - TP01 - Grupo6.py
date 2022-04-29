
#1)
#A)
def maximo_basico(a, b):
    if a > b:
        return a
    return b
print(maximo_basico(10, 8))

#B)
def maximo_libreria(a,b):
    return max(a,b)
print(maximo_libreria(20,4))


#C)
def maximo_ternario(a, b):
    return a if a>b else b
print(maximo_ternario(3,7))


########################################

#2)
#A)
def maximo_encadenado(a,b,c):
    if a>b and a>c:
        return a
    elif b>c: return b
    else: return c
print(maximo_encadenado(1,2,3))

#B)
def maximo_cuadruple(a,b,c,d):
    return max(a,b,c,d)
print(maximo_cuadruple(1,24,37,4))

#C)
def maximo_arbitrario(*a):
    return max(*a)
print(maximo_arbitrario(1,2,3,44444,5,885))

#D)
def maximo_recursivo(*a):
    x = a[0]
    for k in a:
        if x < k:
            x = k
    return x
print(maximo_recursivo(1, 2, 3, 4, 5, 8))


#############################################

#3)
#A)
def operacion_basica(a, b,multiplicar):
    if multiplicar:
        n = a*b
    else:
        if b != 0:
            n = a / b
        else:
            n = "Operación no válida"
    return n

assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"



#B)
def operacion_multiple(a: float, b: float, multiplicar: bool):
    if multiplicar:
        return a*b
    else:
        if b != 0:
            return a / b
        else:
            return "Operación no válida"

assert operacion_multiple(1, 1, True) == 1
assert operacion_multiple(1, 1, False) == 1
assert operacion_multiple(25, 5, True) == 125
assert operacion_multiple(25, 5, False) == 5
assert operacion_multiple(0, 5, True) == 0
assert operacion_multiple(0, 5, False) == 0
assert operacion_multiple(1, 0, True) == 0
assert operacion_multiple(1, 0, False) == "Operación no válida"


#############################################

#4)
#A)
def es_vocal_if(letra: str):
    if letra.lower() == "a": return True
    elif letra.lower() == "e": return True
    elif letra.lower() == "i": return True
    elif letra.lower() == "o": return True
    elif letra.lower() == "u": return True
    else: return False


assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")



#B)
def es_vocal_if_in(letra: str):
    if letra.lower() in ("a", "e", "i", "o", "u"): return True
    else: return False

assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")


#C)
def es_vocal_in(letra):
    rta = False
    while letra.lower() in ("a", "e", "i", "o", "u"):
        rta = True
        break
    return rta

assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")


#################################

#5)
#A)
def multiplicar_basico(numeros):
    if len(numeros) == 0: return 0
    else:
        rta = 1
        for x in numeros:
            rta = rta * x
        return rta

assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
assert multiplicar_basico(range(1, 20)) == 121_645_100_408_832_000


#B)
from functools import reduce

def multiplicar_reduce(numeros):
    if len(numeros) == 0: return 0
    n = 1
    return reduce(lambda x,y : x*y, numeros)

assert multiplicar_reduce([1, 2, 3, 4]) == 24
assert multiplicar_reduce([2, 5]) == 10
assert multiplicar_reduce([]) == 0
assert multiplicar_reduce([1, 2, 3, 0, 4, 5]) == 0
assert multiplicar_reduce(range(1, 20)) == 121_645_100_408_832_000


########################################################

#6)
#A)
def numeros_al_final_basico(lista):
    nros = []
    letras = []
    for x in lista:
        if type(x) in (int, float):
            nros.append(x)
        else:
            letras.append(x)
    return letras + nros

assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]


#B)
def numeros_al_final_comprension(lista):
    nros = []
    letras = []
    nros = [x for x in lista if type(x) in (int, float)]
    letras = [x for x in lista if type(x) == str]
    return letras + nros

assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]


#C)
def numeros_al_final_sorted(lista):
    lista = sorted(lista, key=lambda x: type(x) in (int,float))
    return lista

assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]



#D)
def numeros_al_final_filter(lista):
    str(lista)
    nros = list(filter(lambda x : type(x) in (int, float), lista))
    letras = list(filter(lambda x : type(x) == str, lista))
    return letras + nros

assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]


#E)
def numeros_al_final_recursivo(lista):
    str(lista)
    nros = []
    letras = []
    for x in lista:
        if type(x) in (int, float):
            nros.append(x)
        elif type(x) == str:
            letras.append(x)
    return letras + nros

assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]



########################

#7)
#A)
def es_palindromo(palabra):
    alReves = palabra[::-1] #invierte la cadena
    if palabra == alReves:
        return True
    else: return False

assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")



#B)
def mitad(palabra):
    k = len(palabra)
    m = int(k / 2)
    if k % 2 == 0:
        return palabra[0:m]
    else:
        return palabra[0:(m+1)]
# el slice me va a devolver de la posicion 0 a la otra - 1
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""

###########################################################

#8)
#A)
from typing import Iterable, Any

def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
   rta = False
   for x in lista_1:
       for y in lista_2:
            if x == y:
                rta = True
                break
   return rta

test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))


#B)
def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
   rta = False
   for x in lista_1:
       if x in lista_2:
            rta = True
            break
   return rta

test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))


#C)
from typing import Any, Iterable
def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    return any(item in lista_1 for item in lista_2)

test_list = [1, "hello", 35.20]
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 80.2))


#D)
from typing import Any, Iterable

def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    return not set(lista_1).isdisjoint(lista_2)

test_list = [1, "hello", 35.20]
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))



##################################

#9)
#A)
def sumatoria_basico(n: int) -> int:
    rta = 0
    x = 0
    while x <= n:
        rta = rta + x
        x += 1
    return rta

assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050


#B)
def sumatoria_sum(n: int) -> int:
    lista = range(n+1)
    return sum(lista)

assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050


#C)
from functools import reduce
def sumatoria_reduce(n: int) -> int:
    lista = range(n + 1)
    return reduce(lambda x,y : x+y, lista)

if __name__ == "__main__":
    assert sumatoria_reduce(1) == 1
    assert sumatoria_reduce(100) == 5050


#D)
def sumatoria_gauss(n: int) -> int:
    return n*(n+1)/2

if __name__ == "__main__":
    assert sumatoria_gauss(1) == 1
    assert sumatoria_gauss(100) == 5050


####################################

#10)
#A)
from typing import Iterable
def tiene_pares_basico(numeros: Iterable[int]) -> bool:
    for x in numeros:
        if x%2 == 0:
            return True
    return False

assert tiene_pares_basico([1, 3, 5]) is False
assert tiene_pares_basico([1, 3, 5, 6]) is True
assert tiene_pares_basico([1, 3, 5, 600]) is True


#B)
from typing import Iterable
def tiene_pares_for_else(numeros: Iterable[int]) -> bool:
    for x in numeros:
        if x % 2 == 0:
            return True
            break
    else: return False

assert tiene_pares_for_else([1, 3, 5]) is False
assert tiene_pares_for_else([1, 3, 5, 6]) is True
assert tiene_pares_for_else([1, 3, 5, 600]) is True



#C)
from typing import Iterable
def tiene_pares_any(numeros: Iterable[int]) -> bool:
    return any(lambda x : x for x in numeros if x%2 == 0)

assert tiene_pares_any([1, 3, 5]) is False
assert tiene_pares_any([1, 3, 5, 6]) is True
assert tiene_pares_any([1, 3, 5, 600]) is True


#####################################

#11)
#A)
from typing import Iterable
def suma_cubo_pares_for(numeros: Iterable[int]) -> int:
    suma = 0
    l1 = []
    for x in numeros:
        l1.append(pow(x,3))
    for x in l1:
        if x%2 == 0:
            suma = suma + x
    return suma

assert suma_cubo_pares_for([1, 2, 3, 4, 5, 6]) == 288


#B)
from typing import Iterable
def suma_cubo_pares_sum_list(numeros: Iterable[int]) -> int:
    return sum([pow(x,3) for x in numeros if pow(x,3)%2==0])

assert suma_cubo_pares_sum_list([1, 2, 3, 4, 5, 6]) == 288


#C)
from typing import Iterable
def suma_cubo_pares_sum_gen(numeros: Iterable[int]) -> int:
    return sum((pow(x,3) for x in numeros if pow(x,3)%2==0))

assert suma_cubo_pares_sum_gen([1, 2, 3, 4, 5, 6]) == 288


#D)
# PARTE 2
# A continuación se introduce el concepto de Lambdas (Funciones anónimas),
# Escribir las funciones lambdas que corresponda en cada línea
# Referencia: https://docs.python.org/3/reference/expressions.html#lambda

numeros = [1, 2, 3, 4, 5, 6]

# Escribir una función lambda que eleve los elementos al cubo
numeros_al_cubo = list(map(lambda x : pow(x,3), numeros))

# Escribir una función lambda que permita filtrar todos los elementos pares
pares = list([x for x in numeros if x%2==0])
numeros_al_cubo_pares = list(map(lambda x : pow(x,3), pares))

# Escribir una función Lambda que sume todos los elementos
from functools import reduce
suma_numeros_al_cubo_pares = reduce(lambda x,y : x + y, numeros_al_cubo_pares)

# Escribir una función Lambda que permita ordenar los elementos de la numeros
# en base a si son pares o impares
numeros_ordenada = sorted(numeros, key= lambda x : x%2 == 0, reverse= False)


assert numeros_al_cubo == [1, 8, 27, 64, 125, 216]
assert numeros_al_cubo_pares == [8, 64, 216]
assert suma_numeros_al_cubo_pares == 288
assert numeros_ordenada == [1, 3, 5, 2, 4, 6]


##########################################################

#12)
#A)
from typing import Any, List, Tuple

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]

def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:
    tupla = ()
    tuplas = ()
    tupla_mayor = ()
    for x in range(0,3):
        tupla = (nombres[x], precios[x])
        tuplas = (*tuplas, tupla)
    return tuplas

respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.2),
            )

assert combinar_basico(nombre_articulos, precio_articulos) == respuesta


#B)
from typing import Any, List, Tuple
nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]
id_articulos = [6852, 1459, 3578]

def combinar_enumerate(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    tuplas = ()
    for x, v in enumerate(nombres):
        tupla = (nombres[x], precios[x], ids[x])
        tuplas = (*tuplas, tupla)
    return tuplas

respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
            )

assert combinar_enumerate(nombre_articulos, precio_articulos, id_articulos) == respuesta


#C)
from typing import Any, List, Tuple
nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]
id_articulos = [6852, 1459, 3578]

def combinar_zip(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    for x in range(len(nombres)):
        l = tuple(zip(nombres, precios, ids))
    return l

respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
            )

assert combinar_zip(nombre_articulos, precio_articulos, id_articulos) == respuesta


#D)
from typing import Any, List, Tuple
nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]
id_articulos = [6852, 1459, 3578]
categoria_articulos = ["hogar", "libreria", "perfumeria"]
importado_articulos = [True, False, True]


def combinar_zip_args(*args) -> Tuple[Any]:
    for x in range(len(args[0])):
        l = tuple(zip(*args))
    return l

respuesta = (
    ("ventana", 100.48, 6852, "hogar", True),
    ("lámpara", 16.42, 1459, "libreria", False),
    ("shampoo", 5.2, 3578, "perfumeria", True),
            )

componentes = [
    nombre_articulos,
    precio_articulos,
    id_articulos,
    categoria_articulos,
    importado_articulos,
                ]

assert combinar_zip_args(*componentes) == respuesta


#######################################################

#13)
#A)
from typing import Iterator, Callable
def generar_pares_clousure(initial: int = 0) -> Callable[[], int]:
    initial = -2
    def devuelve():
        nonlocal initial
        initial = initial + 2
        return initial
    return devuelve

generador_pares = generar_pares_clousure(0)
assert generador_pares() == 0
assert generador_pares() == 2
assert generador_pares() == 4


#B)
def generar_pares_generator(initial: int = 0) -> Iterator[int]:
    initial = 0
    yield initial

    for x in generar_pares_generator():
        initial +=2
        yield initial

generador_pares = generar_pares_generator()
assert next(generador_pares) == 0
assert next(generador_pares) == 2
assert next(generador_pares) == 4


#D)
from typing import Iterator, Callable

def generar_pares_delegados(initial: int = 0) -> Iterator[int]:
    yield initial
    yield from generar_pares_delegados(initial + 2)
    yield initial

if __name__ == "__main__":
    generador_pares = generar_pares_delegados()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4


########################################

#14)
#A)
from functools import partial
from typing import Callable, Iterable

def apply(lista: Iterable[int], func: Callable[[int], bool]) -> Iterable[bool]:
    for x in lista:
        lista.append(func(x))
    return lista

def esta_entre_valores(x: int, min_: float, max_: float) -> bool:
    return min_ < x < max_


#B)
from functools import partial
from typing import Callable, Iterable

def apply(lista: Iterable[int], func: Callable[[int], bool]) -> Iterable[bool]:
    for x in lista:
        lista.append(func(x))
    return lista

def esta_entre_valores(x: int, min_: float, max_: float) -> bool:
    return min_ < x < max_

lista = [3, 4, 5, 6, 7, 8]
min_ = 4
max_ = 7
nueva_funcion = partial(esta_entre_valores, min_, max_)



#####################################

#15)
#A)
from itertools import permutations
from time import perf_counter
from typing import Callable, Sequence, Tuple

def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for x in range(limite):
        for _ in permutations(lista, x):
            count += 1
    return count


n = 11
limite = 10
lista = list(range(n))

start = perf_counter()
result = calcular_posibilidades(lista, limite)
elapsed = perf_counter() - start

print(f"Tiempo: {elapsed:2.2f} segundos - Enfoque procedural")
assert result == 28671512


#B)
from functools import partial

def medir_tiempo(func: Callable[[], int]) -> Tuple[int, float]:
    start = perf_counter()
    result = func()
    elapsed = perf_counter() - start
    return result, elapsed


result, elapsed = medir_tiempo(partial(calcular_posibilidades, lista, limite))
print(f"Tiempo: {elapsed:2.2f} segundos - Usando Partial")
assert result == 28671512


#C)
def medir_tiempo(func: Callable[[Sequence[int], int], int]) -> Callable[[Sequence[int], int], Tuple[int, float]]:
    def funcionConArgs(*args):
        nonlocal func
        start = perf_counter()
        result = func(*args)
        elapsed = perf_counter() - start
        return result, elapsed
    return funcionConArgs


calcular_posibilidades_nueva = medir_tiempo(calcular_posibilidades)
result, elapsed = calcular_posibilidades_nueva(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Decorador")
assert result == 28671512


#D)
@medir_tiempo
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for x in range(limite):
        for _ in permutations(lista, x):
            count += 1
    return count


result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Decorador con sintaxis especial")
assert result == 28671512


#E)
def memoized(func):
    cacheList = []
    argsList = []
    def funcMemoized(*args):
        nonlocal func
        nonlocal cacheList
        nonlocal argsList
        if args not in argsList:
            argsList.append(args)
            cacheList.append(func(*args))
        return cacheList[argsList.index(args)]
    return funcMemoized


@medir_tiempo
@memoized
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for x in range(limite):
        for _ in permutations(lista, x):
            count += 1
    return count

print()

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Con Memoized - 1ra ejecución")
assert result == 28671512

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.8f} segundos - Con Memoized - 2da ejecución")
assert result == 28671512

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.8f} segundos - Con Memoized - 3ra ejecución")
assert result == 28671512


#F)
@medir_tiempo
@memoized
def calcular_posibilidades_recursiva(lista: Sequence[int], limite: int) -> int:
    count = 0
    if limite == 0:
        return 0
    for _ in permutations(lista, limite):
        count += 1
    return count + calcular_posibilidades_recursiva(lista, limite-1)


if __name__ == "__main__":
    print()

    result, elapsed = calcular_posibilidades_recursiva(lista, limite)
    print(f"Tiempo: {elapsed:2.2f} segundos - Recursiva Memoized - 1ra Ejecución")
    assert result == 28671512

    result, elapsed = calcular_posibilidades_recursiva(lista, limite)
    print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - 2da Ejecución")
    assert result == 28671512

    print()

    result, elapsed = calcular_posibilidades(lista, limite + 1)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro + 1")
    assert result == 68588312

    result, elapsed = calcular_posibilidades_recursiva(lista, limite + 1)
    print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro + 1")
    assert result == 68588312

    print()

    result, elapsed = calcular_posibilidades(lista, limite + 2)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro + 2")
    assert result == 108505112

    result, elapsed = calcular_posibilidades_recursiva(lista, limite + 2)
    print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro + 2")
    assert result == 108505112

    print()

    result, elapsed = calcular_posibilidades(lista, limite - 1)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro - 1")
    assert result == 8713112

    result, elapsed = calcular_posibilidades_recursiva(lista, limite - 1)
    print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro - 1")
    assert result == 8713112

    print()

    result, elapsed = calcular_posibilidades(lista, limite - 2)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro - 2")
    assert result == 2060312

    result, elapsed = calcular_posibilidades_recursiva(lista, limite - 2)
    print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro - 2")
    assert result == 2060312
