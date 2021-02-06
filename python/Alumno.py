class Alumno:
    def __init__(self, nombre, grado, nota_media, es_repetidor):
        self.nombre = nombre
        self.grado = grado
        self.nota_media = nota_media
        self.es_repetidor = es_repetidor
        
    def tiene_matricula_de_honor(self):
        if self.nota_media >= 9.0:
            return True
        else:
            return False