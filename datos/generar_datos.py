import csv
import random
from datetime import datetime, timedelta

def generar_datos_triage(n_registros=5000, archivo_salida="datos/admisiones.csv"):
    nombres = ["Carlos", "María", "Juan", "Ana", "Luis", "Elena", "David", "Sofía", "Jorge", "Laura", "Andrés", "Camila"]
    apellidos = ["Gómez", "Rodríguez", "Martínez", "López", "Hernández", "Patiño", "Múnera", "Zapata", "Morales", "Calle"]
    
    motivos_triage = {
        "I": ["Paro cardiorrespiratorio", "Shock anafiláctico", "Trauma craneoencefálico severo", "ACV isquémico masivo"],
        "II": ["Dolor torácico agudo", "Dificultad respiratoria moderada", "Hemorragia activa", "Convulsión reciente"],
        "III": ["Fiebre alta persistente", "Dolor abdominal agudo", "Traumatismo en extremidad", "Deshidratación moderada"],
        "IV": ["Laceración superficial", "Migraña moderada", "Esguince leve", "Infección urinaria leve"],
        "V": ["Renovación de fórmula", "Valoración por resfriado", "Retiro de puntos", "Consulta por dermatitis leve"]
    }
    
    servicios = ["Admisión General", "Pediátrico", "Ginecoobstetricia", "Traumatología"]
    pesos_triage = [0.05, 0.15, 0.40, 0.25, 0.15]  # Distribución porcentual típica
    niveles = ["I", "II", "III", "IV", "V"]
    
    fecha_inicio = datetime(2026, 8, 1, 0, 0, 0)
    
    with open(archivo_salida, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Encabezado exacto presentado en el Hito 0
        writer.writerow(["id_admision", "documento", "nombre", "edad", "nivel_triage", "fecha_hora_llegada", "motivo_consulta", "servicio_origen"])
        
        tiempo_actual = fecha_inicio
        
        for i in range(1, n_registros + 1):
            id_admision = f"ADM-{i:04d}"
            documento = str(random.randint(1000000000, 1099999999))
            nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"
            edad = random.randint(1, 85)
            
            # Selección de nivel de triage por probabilidad
            nivel = random.choices(niveles, weights=pesos_triage, k=1)[0]
            motivo = random.choice(motivos_triage[nivel])
            servicio = "Pediátrico" if edad < 15 else random.choice(servicios)
            
            # Simulación de llegada por intervalos (mínimos de Poisson / aleatorios entre 0 y 5 min)
            incremento_segundos = random.randint(10, 300)
            tiempo_actual += timedelta(seconds=incremento_segundos)
            fecha_str = tiempo_actual.strftime("%Y-%m-%d %H:%M:%S")
            
            writer.writerow([id_admision, documento, nombre_completo, edad, nivel, fecha_str, motivo, servicio])

if __name__ == "__main__":
    generar_datos_triage()