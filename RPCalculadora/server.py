# pylint:disable=all
from xmlrpc.server import SimpleXMLRPCServer

def add_numbers(numbers):
    return sum(numbers)

def less_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def for_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def div_numbers(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            if num == 0:
                return "Error: División por cero no permitida"
            result /= num
        return result
    except ZeroDivisionError:
        return "Error: División por cero no permitida."

server = SimpleXMLRPCServer(('localhost', 9000))
print("Escuchando en el puerto 9000...")

server.register_function(add_numbers, 'add')
server.register_function(less_numbers, 'less')
server.register_function(for_numbers, 'for_')
server.register_function(div_numbers, 'div')

server.serve_forever()
