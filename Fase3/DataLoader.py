def loadDataFromFilteAt(path):
    return open(path, 'r', newline = '\r\n').read().splitlines()

def loadData():
    edades = loadDataFromFilteAt("../Archivos/edad.txt")
    edades = [int(i) for i in edades]

    estadosCiviles = loadDataFromFilteAt("../Archivos/estado_civil.txt") 
    escolaridades = loadDataFromFilteAt("../Archivos/escolaridad.txt")
    
    estratos = loadDataFromFilteAt("../Archivos/estrato.txt")
    estratos = [int(i) for i in estratos]

    generos = loadDataFromFilteAt("../Archivos/genero.txt")
    
    promedios = loadDataFromFilteAt("../Archivos/promedio.txt")
    promedios = [float(i) for i in promedios]

    regiones = loadDataFromFilteAt("../Archivos/region.txt")
    data = [edades, estadosCiviles, escolaridades, estratos, generos, promedios, regiones]
    return data
