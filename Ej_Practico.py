import multiprocessing
import time

# Función que verifica si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función principal
if __name__ == "__main__":
    numeros = [15485863, 15485867, 15485869, 15485871]  # Números grandes

    inicio = time.time()

    # Crear un Pool de procesos para ejecutar en paralelo
    with multiprocessing.Pool(processes=4) as pool:
        resultados = pool.map(es_primo, numeros)

    fin = time.time()

    # Mostrar resultados
    for num, resultado in zip(numeros, resultados):
        print(f"{num} {'es primo' if resultado else 'no es primo'}")

    print(f"Tiempo total: {fin - inicio:.2f} segundos")
