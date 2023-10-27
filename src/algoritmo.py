def ordenar_burbuja(arreglo):
    arreglo_ordenado = arreglo.copy()  # Creamos una copia para no modificar el arreglo original
    n = len(arreglo_ordenado)
    
    for i in range(n):
        intercambio = False

        for j in range(0, n-i-1):
            if arreglo_ordenado[j] > arreglo_ordenado[j+1]:
                arreglo_ordenado[j], arreglo_ordenado[j+1] = arreglo_ordenado[j+1], arreglo_ordenado[j]
                intercambio = True
        
        if not intercambio:
            break

    return arreglo_ordenado  # Devolvemos el arreglo ordenado

if __name__ == "__main__":
    entrada_usuario = input("Introduce una lista de números separados por espacios: ")
    numeros = [int(item) for item in entrada_usuario.split()]

    numeros_ordenados = ordenar_burbuja(numeros)
    print("Arreglo ordenado:", numeros_ordenados)

     
