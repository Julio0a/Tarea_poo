def calcular_salario(tarifa_horaria, horas_trabajadas):
    if horas_trabajadas <= 40:
        salario = tarifa_horaria * horas_trabajadas
    else:
        horas_normales = 40
        horas_extra = horas_trabajadas - 40
        salario = tarifa_horaria * horas_normales + 1.5 * tarifa_horaria * horas_extra
    
    return salario

try:
    tarifa_horaria = float(input("Ingrese la tarifa horaria: "))
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    
    salario_total = calcular_salario(tarifa_horaria, horas_trabajadas)
    print("El salario total es:", salario_total)
except ValueError:
    print("Error, por favor introduzca un número")
except Exception as e:
    print("Ocurrió un error:", e)
