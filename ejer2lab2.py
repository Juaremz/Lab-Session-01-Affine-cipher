import random

# --- SECCIÓN 1: FUNCIONES BASE ---

def generar_permutacion(n):
    """Punto 1.2: Genera una permutación aleatoria de tamaño n """
    pi = list(range(1, n + 1))
    random.shuffle(pi)
    return pi

def inversa_permutacion(pi):
    """Punto 1.4: Calcula la permutación inversa """
    n = len(pi)
    inv = [0] * n
    for i in range(n):
        # El valor en pi[i] nos dice a qué posición va el elemento i+1
        # En la inversa, el elemento 'valor' regresa a la posición i+1
        valor = pi[i]
        inv[valor - 1] = i + 1
    return inv

# --- SECCIÓN 2: CIFRADO Y DESCIFRADO ---

def cifrar_permutacion(mensaje, pi):
    """Punto 2.1: Cifra un mensaje m usando la permutación pi """
    n = len(pi)
    # Limpieza: quitar espacios y pasar a mayúsculas
    m = mensaje.replace(" ", "").upper()
    
    # Relleno (Padding) si la longitud no es múltiplo de n 
    while len(m) % n != 0:
        m += 'X'
    
    ciphertext = ""
    # Procesar por bloques de tamaño n
    for i in range(0, len(m), n):
        bloque = m[i:i+n]
        bloque_cifrado = [''] * n
        for j in range(n):
            # Aplicar la regla de permutación 
            bloque_cifrado[pi[j]-1] = bloque[j]
        ciphertext += "".join(bloque_cifrado)
    
    return ciphertext

def descifrar_permutacion(c, pi):
    """Punto 2.2: Descifra un criptograma c usando la permutación original """
    pi_inv = inversa_permutacion(pi)
    
    n = len(pi_inv)
    plaintext = ""
    # El proceso es idéntico al cifrado, pero usando la permutación inversa
    for i in range(0, len(c), n):
        bloque = c[i:i+n]
        bloque_descifrado = [''] * n
        for j in range(n):
            bloque_descifrado[pi_inv[j]-1] = bloque[j]
        plaintext += "".join(bloque_descifrado)
    
    return plaintext

# --- BLOQUE DE EJECUCIÓN 

if __name__ == "__main__":
    print("--- Laboratorio 03: Permutation Cipher (ESCOM) ---")
    
    # 1. Configuración inicial 
    n = int(input("Introduce el tamaño de la permutación n (>=3): "))
    
    if n >= 3:
        # 2. Alice genera la permutación 
        pi = generar_permutacion(n)
        print(f"\n Permutación generada (pi): {pi}")
        
        # 3. Alice cifra un mensaje 
        msj_original = input(" Introduce el mensaje a cifrar: ")
        criptograma = cifrar_permutacion(msj_original, pi)
        print(f" Mensaje cifrado enviado : {criptograma}")
        
        print("\n comparte pi y el criptograma con Pau o Yun")
        
        # 4. Bob descifra el mensaje 
        pi_inversa = inversa_permutacion(pi)
        print(f" Calculando inversa (pi^-1): {pi_inversa}")
        
        msj_recuperado = descifrar_permutacion(criptograma, pi)
        print(f" Mensaje recuperado: {msj_recuperado}")
    else:
        print("El tamaño n debe ser mayor o igual a 3.")
