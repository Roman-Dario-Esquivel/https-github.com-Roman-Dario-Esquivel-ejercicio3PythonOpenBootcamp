"""def determina_anio(dias):
    if dias==366:
        print("Es año biciesto")
    else:
        print("No es año biciesto")
    
    
determina_anio(int(input("ingrese cantidad de dias que tiene el año:")))"""
class Vehiculo:
    def __init__(self,color,ruedas,puertas):
        self.Color = color
        self.Ruedas = ruedas
        self.Puertas = puertas
        
class Coche(Vehiculo):
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        super().__init__(color,ruedas,puertas)
        self.Velocidad = velocidad
        self.Cilindrada = cilindrada
    def mostrar(self):
        print("El color de coche es ",self.Color," la cantidad de ruedas que tiene es ", self.Ruedas," la cantidad de puertas que tiene es ",self.Ruedas, " la Velocidad es ",self.Velocidad," las cilindrada es ",self.Cilindrada)
        

        

movil = Coche("azul",4,5,120,12)
movil.mostrar()