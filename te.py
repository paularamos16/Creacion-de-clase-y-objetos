
#numero1
class Te():
    duracion = 365
    
    def __init__(self, sabor, formato) :  #constructor de la clase
        self.sabor = sabor
        self.formato=formato
#numero2     
    @staticmethod    
    def obtener_tiempo_recomendacion(sabor):  #metodo
        if sabor == 1:  #te negro
            tiempo = 3
            recomendacion = "El té negro se recomienda consumir al desayuno"  
        elif sabor == 2:  #te verde
            tiempo = 5
            recomendacion= " el té verde al medio día"   
        elif sabor ==3:  #te de hierbas
            tiempo = 6
            recomendacion = "Te de hierbas al atardecer"
        return tiempo, recomendacion
#numero3   
    @staticmethod
    def obtener_precio(formato):
        if formato == 300:
            precio = 3000
        elif formato == 500:
            precio = 5000
        return precio
    
    def obtener_sabor(self):
        if self.sabor == 1:
            texto = "Te negro"
        elif self.sabor ==2:
            texto = "te Verde"
        elif self.sabor == 3:
            texto = "te de hierbas"
        return texto
        