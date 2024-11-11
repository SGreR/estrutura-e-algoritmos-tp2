#Ex 2 - MergeSort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

#Ex 3
def encontrar_duplicados_forca_bruta(arr):
    duplicados = set()
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                duplicados.add(arr[i])  # Se encontrar um duplicado, adiciona ao set

    return list(duplicados)


def encontrar_duplicados_com_set(arr):
    vistos = set()
    duplicados = set()

    # Percorrer cada elemento da lista
    for num in arr:
        if num in vistos:
            duplicados.add(num)
        else:
            vistos.add(num)

    return list(duplicados)

#Ex 4

def ordenar_pilha(pilha):
    if not pilha:
        return pilha

    topo = pilha.pop()
    ordenar_pilha(pilha)
    inserir_em_ordem(pilha, topo)

    return pilha


def inserir_em_ordem(pilha, valor):
    if not pilha or pilha[-1] <= valor:
        pilha.append(valor)
    else:
        topo = pilha.pop()
        inserir_em_ordem(pilha, valor)
        pilha.append(topo)


#Ex 5
def tarefa_no_topo(pilha_de_tarefas):
    if pilha_de_tarefas:
        return pilha_de_tarefas[-1]
    else:
        return None

#Ex 6
def contar_pedidos_impares(pilha_de_pedidos):
    contador = 0
    pilha_copia = pilha_de_pedidos[:]

    while pilha_copia:
        pedido = pilha_copia.pop()
        if pedido % 2 != 0:
            contador += 1

    return contador

#Ex 7
def contar_pedidos_pares(pilha_de_pedidos):
    contador = 0
    pilha_copia = pilha_de_pedidos[:]

    while pilha_copia:
        pedido = pilha_copia.pop()
        if pedido % 2 == 0:
            contador += 1

    return contador

#Ex 9

#Ex 10
def inverter_fila(fila):
    temp_pilha = []

    while fila:
        temp_pilha.append(fila.pop(0))

    while temp_pilha:
        fila.append(temp_pilha.pop())

#Ex 9
def contar_livros_impares(fila_de_livros):
    contador = 0
    fila_copia = fila_de_livros[:]

    while fila_copia:
        livro = fila_copia.pop(0)
        if livro % 2 != 0:
            contador += 1
    return contador