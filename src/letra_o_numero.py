def evaluar(caracter):
    codigo_ascii = ord(caracter) 
    
        if 48 <= codigo_ascii <= 57:
            return "Es número"
        if 65 <= codigo_ascii <= 90:
            return "Es letra mayúscula"
        if 97 <= codigo_ascii <= 122:
            return "Es letra minúscula"
        return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
