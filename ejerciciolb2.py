import numpy as np
import random

ASCII_START = 32
ASCII_END = 126
N = (ASCII_END - ASCII_START) + 1  # n = 95

# Inverso Multiplicativo Modular
def multiplicative_inverse(n, a):
    a0, b0 = n, a
    t0, t = 0, 1
    q = a0 // b0
    r = a0 - q * b0
    
    while r > 0:
        temp = (t0 - q * t) % n
        t0 = t
        t = temp
        a0 = b0
        b0 = r
        if b0 == 0: break
        q = a0 // b0
        r = a0 - q * b0
    # si es que no tiene inverso    
    if b0 != 1:
        return None  
    return t % n

#  matriz inversa K^-1 mod n
def get_matrix_inverse(K, n):
    det = int(round(np.linalg.det(K)))
    det_inv = multiplicative_inverse(n, det % n)
    
    if det_inv is None:
        return None
    
    # Matriz adjunta para 2x2: [[d, -b], [-c, a]]
    adj = np.array([[K[1,1], -K[0,1]], [-K[1,0], K[0,0]]])
    return (det_inv * adj) % n

# Hill Cipher
def encipher_hill(filename, K, output_file):
    with open(filename, 'r', encoding='ascii', errors='ignore') as f:
        plaintext = f.read()
    ciphertext = ""
    buffer = []
    
    for char in plaintext:
        if char == '\n':
            if buffer: # Rellenar si el buffer tiene 1 caracter
                buffer.append(' ')
                ciphertext += process_block(buffer, K)
                buffer = []
            ciphertext += '\n'
            continue
            
        buffer.append(char)
        if len(buffer) == 2:
            ciphertext += process_block(buffer, K)
            buffer = []
            
    if buffer: # Relleno final (padding)
        buffer.append(' ')
        ciphertext += process_block(buffer, K)

    with open(output_file, 'w', encoding='ascii') as f:
        f.write(ciphertext)

def process_block(block, K):
    # Convertir caracteres a valores 0-(n-1)
    vec = np.array([ord(c) - ASCII_START for c in block])
    res = np.dot(K, vec) % N
    return "".join([chr(int(v) + ASCII_START) for v in res])

# 3. Función para Descifrar
def decipher_hill(ciphertext_file, K, output_file):
    K_inv = get_matrix_inverse(K, N)
    if K_inv is None:
        print("Error: La clave no es invertible.")
        return
        
    print(f"K^-1 mód {N}:\n{K_inv}") 
    encipher_hill(ciphertext_file, K_inv, output_file)

def main():
    print("--- Laboratorio 2: Cifrado Hill ---")
    mode = input("Seleccione (1) Cifrar o (2) Descifrar: ")
    file_in = input("Archivo de entrada: ")
    file_out = input("Archivo de salida: ")
    
    print("Ingrese los elementos de la matriz K 2x2:")
    k11 = int(input("K[0,0]: "))
    k12 = int(input("K[0,1]: "))
    k21 = int(input("K[1,0]: "))
    k22 = int(input("K[1,1]: "))
    K = np.array([[k11, k12], [k21, k22]])

    if mode == '1':
        encipher_hill(file_in, K, file_out)
        print(f"Archivo cifrado guardado en {file_out}")
    else:
        decipher_hill(file_in, K, file_out)
        print(f"Archivo descifrado guardado en {file_out}")

if __name__ == "__main__":
    main()
