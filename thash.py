class Token:
    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column

def tokenize_code(code):
    tokens = []
    lines = code.split('\n')
    for row, line in enumerate(lines):
        line = line.strip()
        if line:
            chars = list(line)
            column = 0
            while column < len(chars):
                if chars[column] == ';':
                    tokens.append(Token(';', row, column))
                    column += 1
                elif chars[column].isspace():
                    column += 1
                else:
                    token_value = ''
                    while column < len(chars) and not chars[column].isspace() and chars[column] != ';':
                        token_value += chars[column]
                        column += 1
                    tokens.append(Token(token_value, row, column - len(token_value)))
    return tokens


def store_tokens(tokens, custom_keys):
    hash_table = {}
    for i, token in enumerate(tokens):
        key = custom_keys[i]
        hash_table[key] = token.value
    return hash_table

def buscar_token_por_clave(hash_table):
    clave = input("Ingresa la clave del token: ")
    if clave in hash_table:
        return hash_table[clave]
    else:
        return None

#Código en C++
code = '''
int suma = 0;
suma = 54 + 20;
'''

custom_keys = ['00', '04', '09', '011', '012', '10', '15', '17', '110', '112', '114']

tokens = tokenize_code(code)
hash_table = store_tokens(tokens, custom_keys)

print("Tabla Hash:")
for key, value in hash_table.items():
    print(f'Clave: {key}, Token: {value}')

# Buscar un token por su clave ingresada desde consola
token_encontrado = buscar_token_por_clave(hash_table)

if token_encontrado:
    print(f"Token encontrado: {token_encontrado}")
else:
    print("No se encontró ningún token con la clave especificada.")
