"""def determina_anio(dias):
    if dias==366:
        print("Es año biciesto")
    else:
        print("No es año biciesto")
    
    
determina_anio(int(input("ingrese cantidad de dias que tiene el año:")))"""
class Vehiculo:
    Color = None
    Ruedas = None
    Puertas = None
    def __init__(self,color,ruedas,puertas):
        self.Color = color
        self.Ruedas = ruedas
        self.Puertas = puertas
        
class Coche(Vehiculo):
    Velocidad = None
    Cilindrada = None
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        Coche.Color = color
        Coche.Ruedas = ruedas
        Coche.Puertas = puertas
        Coche.Velocidad = velocidad
        Coche.Cilindrada = cilindrada
    def mostrar(self):
        print("El color de coche es ",Coche.Color," la cantidad de ruedas que tiene es ", Coche.Ruedas," la cantidad de puertas que tiene es ",Coche.Ruedas, " la Velocidad es ",Coche.Velocidad," las cilindrada es ",Coche.Cilindrada)
        

        

movil = Coche("azul",4,5,120,12)
movil.mostrar()