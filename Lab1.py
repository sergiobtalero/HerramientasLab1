# f = open(file, mode, encoding newline)


def getValuesFrom(fileAtPath):
    dataFromFile = open(fileAtPath, "r")
    data = dataFromFile.readlines()
    return data

agesData = getValuesFrom("Archivos/edad.txt")
scholarityData = getValuesFrom("Archivos/escolaridad.txt")
civilStatusData = getValuesFrom("Archivos/estado_civil.txt")
economicClassData = getValuesFrom("Archivos/estrato.txt")
genderData = getValuesFrom("Archivos/genero.txt")
scoreData = getValuesFrom("Archivos/promedio.txt")
regionData = getValuesFrom("Archivos/region.txt")


def sustituir(cadena):
    return cadena[0] + cadena[-2] + cadena[2:-2]+ cadena[1] + cadena[-1]

cadena = "Archivos de texto"
newValue = sustituir(cadena)
print(len(newValue))