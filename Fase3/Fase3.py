from DataLoader import loadData
import functools

# Load Data
(edades, estadosCiviles, escolaridades, estratos, generos, promedios, regiones) = loadData()

class Estudiante:
    def __init__(self, id, edad, estadoCivil, escolaridad, estrato, genero, promedio, region):
        self.id = id
        self.edad = edad
        self.estadoCivil = estadoCivil
        self.escolaridad = escolaridad
        self.estrato = estrato
        self.genero = genero
        self.promedio = promedio
        self.region = region
        
students = []
for idx in list(range(0, 500)):
    estudiante = Estudiante(idx, 
    edades[idx],
    estadosCiviles[idx],
    escolaridades[idx],
    estratos[idx],
    generos[idx],
    promedios[idx],
    regiones[idx])

    students.append(estudiante)

# Parameters
scholarshipsNumber = 30
minAge = 20
maxAge = 40
isGenderSelected = False
isEstratoSelected = False
isRegionSelected = True

characteritics = [isGenderSelected, isEstratoSelected, isRegionSelected]

# Filtering students by age
filteredStudents = list(filter(lambda e: e.edad >= minAge and e.edad <= maxAge, students))


# Selecting strategy
conditionsCount = len(list(filter(lambda c: c, characteritics)))
assert(conditionsCount > 0)

if conditionsCount == 1:
    print('One option selected')
elif conditionsCount == 2:
    print('Two options selected')
else print('Three options selected')
