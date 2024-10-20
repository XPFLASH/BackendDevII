# pylint:disable=all
import xmlrpc.client
import re

proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

def calculate_expression(expression):
    numbers = list(map(float, re.findall(r'\d+\.\d+|\d+', expression)))
    operators = re.findall(r'[+\-*/]', expression)

    if len(numbers) - 1 != len(operators):
        return "Error: Expresión inválida."

    i = 0
    while i < len(operators):
        if operators[i] in "*/":
            if operators[i] == "*":
                result = proxy.for_([numbers[i], numbers[i+1]])
            elif operators[i] == "/":
                result = proxy.div([numbers[i], numbers[i+1]])

            numbers[i] = result
            del numbers[i+1]
            del operators[i]
        else:
            i += 1

    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == "+":
            result = proxy.add([result, numbers[i+1]])
        elif operator == "-":
            result = proxy.less([result, numbers[i+1]])

    return result

while True:
    expression_input = input("Ingrese la operación (ej: 1+1*2) o 'salir' para terminar: ").strip()
    
    if expression_input.lower() == "salir":
        print("Terminando la calculadora remota...")
        break

    try:
        result = calculate_expression(expression_input)
        print(f"Resultado de la operación es: {result}")
    
    except ValueError:
        print("Por favor ingrese una expresión válida.")
    except Exception as e:
        print(f"Error: {e}")