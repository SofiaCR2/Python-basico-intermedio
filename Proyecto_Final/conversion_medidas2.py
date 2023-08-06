class ConversionUnidadesGramos:
    """Es un programa con metodos para facilitar la convercion de todos los
        tipos de gramos a gramos o a otro tipo de gramo solamente metiendo la
        unidad degramos que queremos convertir.
        Ejemplo:
        le indicamos que queremos convertir de kilogramo a hectogramo, entonces
        ocupamos el metodo kilohectagramo() y entre los parentesis va el numero
        de kilogramos que tenemos"""

    def __init__(self, unidadinicial):
        self.unidadinicial = unidadinicial

    def kiloaHectagramo(unidadinicial):
        return unidadinicial * 10
    
    def hectaaDecagramo(unidadinicial):
        return unidadinicial * 10
    
    def decaaGramp(unidadinicial):
        return unidadinicial * 10
    
    def gramoaDecigramo(unidadinicial):
        return unidadinicial * 10
    
    def deciaCentigramo(unidadinicial):
        return unidadinicial * 10
    
    def centiaMiligramo(unidadinicial):
        return unidadinicial * 10
    
    def miliaCentigramo(unidadinicial):
        return unidadinicial / 10
    
    def centidecigramo(unidadinicial):
        return unidadinicial / 10
    
    def gramoaDecagramo(unidadinicial):
        return unidadinicial / 10
    
    def decaaHectogramo(unidadinicial):
        return unidadinicial / 10
    
    def hectaKiloGramo(unidadinicial):
        return unidadinicial / 10
    
    def miliaGramo(unidadinicial):
        return unidadinicial / 1000
    
    def centiaGramo(unidadinicial):
        return unidadinicial / 100

    def deciaGramo(unidadinicial):
        return unidadinicial / 10
    
    def hectaaGramo(unidadinicial):
        return unidadinicial * 100
    
    def kiloaGramo(unidadinicial):
        return unidadinicial * 1000
