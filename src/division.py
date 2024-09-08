def evaluar(dividendo, divisor):

    if divisor == 0:
        return "error"
    
    cociente = dividendo// divisor
    residuo = dividendo % divisor
    
    if residuo==0:
        respuesta = f"La división es exacta. \nCociente: {cociente}\nResiduo: {residuo}"
    else: 
        respuesta= f"La división no es exacta. \nCociente: {cociente}\nResiduo: {residuo}"

    return respuesta


if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
