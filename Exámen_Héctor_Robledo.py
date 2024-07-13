import numpy as np
import json
import random
import statistics

def Asignar_Sueldos_Aleatorios():
    for x in range(10):
        sueldos.append(random.randint(300000,2500000))

def clasificar_sueldos():
    Menor = []
    Entre = []
    Mayor = []
    total_sueldos = 0
    for x in range(len(sueldos)):
        if sueldos[x] < 800000:
            Menor.append(x)
        elif 800000 <= sueldos[x] <= 2000000:
            Entre.append(x)
        elif 2000000 < sueldos[x]:
            Mayor.append(x)
    print(f"""
Sueldos menores a $800.000 TOTAL: {len(Menor)}
Nombre empleado         Sueldo""")
    for i in Menor:
        print(f'{trabajadores[i]}           ${sueldos[i]}')
    print(f"""
Sueldos entre $800.000 y $2.000.000 TOTAL: {len(Entre)}
Nombre empleado         Sueldo""")
    for i in Entre:
        print(f'{trabajadores[i]}           ${sueldos[i]}')
    print(f"""
Sueldos superiores a $2.000.000 TOTAL: {len(Mayor)}
Nombre empleado         Sueldo""")
    for i in Mayor:
        print(f'{trabajadores[i]}           ${sueldos[i]}')
    for i in sueldos:
        total_sueldos = total_sueldos + i
    print(F"\nTOTAL SUELDOS: {total_sueldos}")

def Ver_estadisticas():
    Sueldo_mas_alto = max(sueldos)
    Sueldo_mas_bajo = min(sueldos)
    total_sueldos = 0
    Media_geografica = statistics.geometric_mean(sueldos)
    print(f'\nEl sueldo más alto es ${Sueldo_mas_alto}')
    print(f'El sueldo más bajo es ${Sueldo_mas_bajo}')
    for x in sueldos:
        total_sueldos = total_sueldos + x
    print(f'El promedio de los sueldos es: ${total_sueldos/10}')
    print(f'La media geométrica es: ${Media_geografica}')

def Reporte_de_sueldos():
    print(f"Nombre del empleado         Sueldo Base             Descuento Salud          Descuento AFP           Sueldo Líquido")
    for x in range(len(trabajadores)):
        print(f"""{trabajadores[x]}                  ${sueldos[x]}                 ${round(sueldos[x]*0.07)}                  ${round(sueldos[x]*0.12)}                  ${sueldos[x]-round(sueldos[x]*0.07)-round(sueldos[x]*0.12)}""")

def guardarDatos():
    datos = []
    for i in range(10):
        paciente = {
            'Nombre': trabajadores[i],
            'Sueldo Base': sueldos[i],
            'Descuento Salud': round(sueldos[i]*0.07),
            'Descuento AFP': round(sueldos[i]*0.12),
            'Sueldo Líquido': sueldos[i]-round(sueldos[i]*0.07)-round(sueldos[i]*0.12)
        }
        datos.append(paciente)
    
    with open('pacientes.json', 'w') as file:
        json.dump(datos, file, indent=4)

trabajadores = ['Juan Pérez',
                'María García',
                'Carlos López',
                'Ana Martínez',
                'Pedro Rodríguez',
                'Laura Hernández',
                'Miguel Sánchez',
                'Isabel Gómez',
                'Francisco Días',
                'Elena Fernández']
sueldos = []


while True:
    while True:
        print('''
Menú:
1.- Asignar sueldos aleatorios
2.- Clasificar sueldos
3.- Ver estadísticas
4.- Reporte de sueldos
5.- Salir
Selecciones una opción:''',end=" ")
        op = int(input())
        if 1 <= op <=5:
            break
        else:
            print('opción inválida.')
    
    match op:
        case 1:
            Asignar_Sueldos_Aleatorios()
            print("\nSueldos Rellenados exitosamente")
        case 2:
            clasificar_sueldos()
        case 3:
            try:
                Ver_estadisticas()
            except:
                print("\nRellene los sueldos primero")
        case 4:
            try:
                Reporte_de_sueldos()
            except:
                print("\nRellene los sueldos primero")
        case 5:
            guardarDatos()
            print("\nExportando datos\nFinalizando programa...\nDesarrollado por Héctor Robledo\nRut 21.150.403-k\n")
            break
