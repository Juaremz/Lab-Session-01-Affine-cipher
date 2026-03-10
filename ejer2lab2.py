import random

def generar_permutacion(n):
    pi = list(range(1, n + 1))
    random.shuffle(pi)
    return pi

def inversa_permutacion(pi):
    """Punto 1.4: Calcula la permutación inversa pi^-1 """
    n = len(pi)
    inv = [0] * n
    for i in range(n):
        valor = pi[i]
        inv[valor - 1] = i + 1
    return inv

# ---  CIFRADO Y DESCIFRADO ---

def cifrar_permutacion(mensaje, pi):
    """Punto 2.1: Cifra un mensaje m usando la permutación pi """
    n = len(pi)
    m = mensaje.replace(" ", "").upper()
    
    # Relleno (Padding) si la longitud no es múltiplo de n 
    while len(m) % n != 0:
        m += 'X'
    
    ciphertext = ""
    for i in range(0, len(m), n):
        bloque = m[i:i+n]
        bloque_cifrado = [''] * n
        for j in range(n):
            bloque_cifrado[pi[j]-1] = bloque[j]
        ciphertext += "".join(bloque_cifrado)
    
    return ciphertext

# --- MENÚ PRINCIPAL ---

def menu():
    print("\n--- LABORATORIO 03: PERMUTATION CIPHER ---")
    
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Generar Permutación y Cifrar (Alice)")
        print("2. Descifrar un mensaje (Bob)")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            n = int(input("Introduce el tamaño n (>=3): "))
            pi = generar_permutacion(n)
            print(f"Permutación pi generada: {pi}")
            
            msj = input("Introduce el mensaje claro: ")
            cifrado = cifrar_permutacion(msj, pi)
            print(f"Criptograma para enviar a Bob: {cifrado}")
            
        elif opcion == "2":
            # Aquí Bob pide los datos que Alice le compartió 
            cripto = input("Introduce el criptograma recibido: ")
            pi_str = input("Introduce la permutación pi (separada por comas, ej: 3,1,4,2): ")
            
            # Convertir el string de la permutación a una lista de enteros
            pi_recibida = [int(x.strip()) for x in pi_str.split(",")]
            
            # Bob calcula la inversa para poder descifrar 
            pi_inv = inversa_permutacion(pi_recibida)
            print(f"Inversa calculada (pi^-1): {pi_inv}")
            
            # Descifrar usando la inversa
            descifrado = cifrar_permutacion(cripto, pi_inv)
            print(f"Mensaje original recuperado: {descifrado}")
            
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
