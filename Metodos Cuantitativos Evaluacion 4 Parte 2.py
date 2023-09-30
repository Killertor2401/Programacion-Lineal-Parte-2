# Evaluacion #4 Metodos Cuantitativos Programacion Entera: Parte 2

# Se procede a importar las librerias a utilizar

# Importamos la libreria PuLP
import pulp

# Primero, procedemos a definir los profesores y los cursos que nos da el problema:
profesors = ["A", "B", "C", "D", "E"]
courses = ["C1", "C2", "C3", "C4", "C5"]

# Luego, procedemos a crear el problema de maximización:
problem = pulp.LpProblem("Asignacion_de_Profesores", pulp.LpMaximize)

# Despues, procedemos a crear las variables binarias para la asignación de profesores a los cursos:
assignment = pulp.LpVariable.dicts("Asignacion", [(profesor, course) for profesor in profesors for course in courses], cat='Binary')

# Ahora, definimos la matriz de preferencias de profesores:
preferences = {
    "A": {"C1": 5, "C2": 7, "C3": 9, "C4": 8, "C5": 6},
    "B": {"C1": 8, "C2": 2, "C3": 10, "C4": 7, "C5": 9},
    "C": {"C1": 5, "C2": 3, "C3": 8, "C4": 9, "C5": 9},
    "D": {"C1": 9, "C2": 6, "C3": 9, "C4": 7, "C5": 10},
    "E": {"C1": 7, "C2": 8, "C3": 8, "C4": 8, "C5": 5}
}

# Despues, definimos la función objetivo (total de preferencias):
problem += pulp.lpSum(preferences[profesor][course] * assignment[(profesor, course)] for profesor in profesors for course in courses)

# Restricciones:

# Restricción #1: Cada profesor debe dictar solo un curso:
for profesor in profesors:
    problem += pulp.lpSum(assignment[(profesor, course)] for course in courses) == 1

# Restricción #2: Cada curso debe tener un profesor:
for course in courses:
    problem += pulp.lpSum(assignment[(profesor, course)] for profesor in profesors) == 1

# Para terminar, resolvemos el problema con la funcion "solve":
problem.solve()

# Despues, mostramos la asignación óptima del problema:
print("Asignación óptima de profesores a cursos:")
for profesor in profesors:
    for course in courses:
        if pulp.value(assignment[(profesor, course)]) == 1:
            print(f"Profesor {profesor} -> Curso {course} (Preferencia: {preferences[profesor][course]})")

# Y por ultimo, mostramos el valor óptimo de la función objetivo:
print(f"Total de preferencias maximizado: {pulp.value(problem.objective)}")