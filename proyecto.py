import random

#Definimos el alfabeto ASCII  
ALPHABET = [chr(i) for i in range(32, 127)]
N = len(ALPHABET) # Tamaño del alfabeto (95)

# 1. Función para el Máximo Común Divisor (GCD) 
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 2. Generar el grupo multiplicativo Zn*
def get_zn_star(n):
    return [x for x in range(1, n) if get_gcd(x, n) == 1]

# 3. Encontrar el inverso multiplicativo modular (a^-1 mod n)
def get_inverse(a, n):
    for b in range(1, n):
        if (a * b) % n == 1:
            return b
    return None

# 4a. Generación de llaves aleatorias 
def generate_key():
    zn_star = get_zn_star(N)
    a = random.choice(zn_star)
    b = random.randint(0, N - 1)
    return (a, b)

# 4b. Función para cifrar
def encipher(filename_in, filename_out, key):
    a, b = key
    with open(filename_in, 'r', encoding='ascii') as f:
        plaintext = f.read()
    
    ciphertext = ""
    for char in plaintext:
        if char in ALPHABET:
            p_index = ALPHABET.index(char)
            c_index = (a * p_index + b) % N
            ciphertext += ALPHABET[c_index]
        else:
            # Mantener caracteres fuera del rango
            ciphertext += char
            
    with open(filename_out, 'w', encoding='ascii') as f:
        f.write(ciphertext)
    print(f"Archivo cifrado guardado en: {filename_out}")

# 4c. Función para descifrar
def decipher(filename_in, filename_out, key):
    a, b = key
    a_inv = get_inverse(a, N) 
    print(f"Valor de a^-1 mod {N}: {a_inv}") 
    
    with open(filename_in, 'r', encoding='ascii') as f:
        ciphertext = f.read()
        
    plaintext = ""
    for char in ciphertext:
        if char in ALPHABET:
            # Fórmula: P = a^-1 * (C - b) mod n 
            c_index = ALPHABET.index(char)
            p_index = (a_inv * (c_index - b)) % N
            plaintext += ALPHABET[p_index]
        else:
            plaintext += char
            
    with open(filename_out, 'w', encoding='ascii') as f:
        f.write(plaintext)
    print(f"Archivo descifrado guardado en: {filename_out}")

if __name__ == "__main__":
    print("--- Laboratorio 01: Cifrado Afín ---")
    mode = input("¿Deseas (E)ncifrar o (D)escifrar?: ").upper()
    
    file_in = input("Nombre del archivo de entrada: ")
    file_out = input("Nombre del archivo de salida: ")
    
    if mode == 'E':
        k_a, k_b = generate_key()
        print(f"Llave generada automáticamente: K = ({k_a}, {k_b})")
        encipher(file_in, file_out, (k_a, k_b))
    else:
        k_a = int(input("Ingresa el valor de 'a' de la llave: "))
        k_b = int(input("Ingresa el valor de 'b' de la llave: "))
        decipher(file_in, file_out, (k_a, k_b))
