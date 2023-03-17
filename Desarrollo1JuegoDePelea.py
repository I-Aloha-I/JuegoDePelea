from os import system
import random
import time
import sys
from datetime import date

today = date.today()
diaActual=int(format(today.day))
mesActual=int(format(today.month))
añoActual=int(format(today.year))

class Personaje:

    def __init__(self,_nombre,_tipo,_vida,_distancia):
        self.nombre=_nombre
        self.tipo=_tipo
        self.vida=_vida
        self.distancia=_distancia
        self.golpe=0
        self.especial=True

    def Avanzar(self, _oponente):
        avanzar = random.randint(1, 2)
        self.distancia = self.distancia-avanzar
        _oponente.distancia = _oponente.distancia - avanzar
    
    def Retroceder(self, _oponente):
        retroceder = random.randint(1, 2)
        self.distancia = self.distancia + retroceder
        _oponente.distancia = _oponente.distancia + retroceder
    
    def Atacar(self, _oponente):
        if  self.tipo=="Espacio" or self.tipo=="espacio":
            if self.nombre == "Superman":
                self.golpe = random.randint(self.FuerzaMinima, self.FuerzaMaxima)
                self.golpe=self.golpe+self.golpe*0.2
            elif self.nombre == "Goku":
                self.golpe = random.randint(self.KiMinimo, self.KiMaximo)
                self.golpe=self.golpe+self.golpe*0.2
            elif self.nombre == "Iron Man":
                self.golpe = random.randint(self.EnergiaMinima, self.EnergiaMaxima)
                self.golpe=self.golpe+self.golpe*0.2
            elif self.nombre == objGuerrero.nombre:
                self.golpe = random.randint(self.PotenciaMinima, self.PotenciaMaxima)    
                self.golpe=self.golpe+self.golpe*0.2
        else:
            if self.nombre == "Superman":
                self.golpe = random.randint(self.FuerzaMinima, self.FuerzaMaxima)
            elif self.nombre == "Goku":
                self.golpe = random.randint(self.KiMinimo, self.KiMaximo)
            elif self.nombre == "Iron Man":
                self.golpe = random.randint(self.EnergiaMinima, self.EnergiaMaxima)
            elif self.nombre == objGuerrero.nombre:
                self.golpe = random.randint(self.PotenciaMinima, self.PotenciaMaxima)      

        print(self.nombre , "realiza un ataque de" , self.golpe , "de daño a" , _oponente.nombre)
        _oponente.vida = _oponente.vida - self.golpe

    def Defender(self, _oponente):
        if (_oponente.distancia>10 or _oponente.distancia<-10):
            dañoDefendido = _oponente.golpe * 0.8   # Se defienden un 80% del daño.
            self.vida = self.vida + dañoDefendido
        if ((_oponente.distancia<=10 and _oponente.distancia>=5) or (_oponente.distancia>=-10 and _oponente.distancia<=-5)):
            dañoDefendido = _oponente.golpe * 0.5   # Se defienden un 50% del daño.
            self.vida = self.vida + dañoDefendido
        elif (_oponente.distancia<5 and _oponente.distancia>-5):
            dañoDefendido = _oponente.golpe * 0.1   # Se defienden un 10% del daño.
            self.vida = self.vida + dañoDefendido
            

    def Descripcion(self):
        if self.tipo=="Tierra" or self.tipo=="tierra": # Tipo Tierra aumenta su vida en 20%
            self.vida=self.vida+self.vida*0.2
            print("\nNombre:\t   ", self.nombre,"\nTipo:\t   ",self.tipo,"\nVida:\t   ",self.vida,"\nDistancia: ",self.distancia)
        else:
            self.vida=self.vida-self.vida*0.2 # No es tipo Tierra baja su vida en 20%  pero en el metodo Atacar su golpe aumenta un 20%
            print("\nNombre:\t   ", self.nombre,"\nTipo:\t   ",self.tipo,"\nVida:\t   ",self.vida,"\nDistancia: ",self.distancia)
    
    def __del__(self):
        pass
      
class GuerreroUT1(Personaje): # Guerrero Universo Tierra-1
    def __init__(self,_FuerzaMinima,_FuerzaMaxima,_nombre,_tipo,_vida,_distancia):
        
        super().__init__(_nombre,_tipo,_vida,_distancia)
        self.FuerzaMinima=_FuerzaMinima
        self.FuerzaMaxima=_FuerzaMaxima
        
    def Llamar_al_Compañero(self,_oponente): # HABILIDAD ESPECIAL DE SUPERMAN
        self.golpe = random.randint(self.FuerzaMinima, self.FuerzaMaxima + self.FuerzaMaxima*0.3)
        
        print(self.nombre , "Llamo a un compañero aumentando su rango de golpe en un 30%, y realiza un ataque especial de" , self.golpe , "de daño a" , _oponente.nombre)
        _oponente.vida = _oponente.vida - self.golpe

    def Descripcion(self):
        super().Descripcion()
        print("Fuerza Minima: ", self.FuerzaMinima,"\nFuerza Maxima: ",self.FuerzaMaxima, "\nHabilidad especial: Llamar a un companero para aumentar el rango de golpe en un 30%")


class GuerreroU7(Personaje): # Guerrero Universo 7
    def __init__(self,_KiMinimo,_KiMaximo,_nombre,_tipo,_vida,_distancia):
        
        super().__init__(_nombre,_tipo,_vida,_distancia)
        self.KiMinimo=_KiMinimo
        self.KiMaximo=_KiMaximo
        
    def Transformacion(self, _oponente): # HABILIDAD ESPECIAL DE GOKU
        self.golpe = random.randint(self.KiMinimo, self.KiMaximo)
        self.golpe=self.golpe+self.golpe*0.2
        
        print(self.nombre , "se transforma y realiza un ataque especial de" , self.golpe , "de daño a" , _oponente.nombre)
        _oponente.vida = _oponente.vida - self.golpe    
        
    def Descripcion(self):
        super().Descripcion()
        print("Ki Minimo: ", self.KiMinimo,"\nKi Maximo: ",self.KiMaximo, "\nHabilidad especial: Transformarse para aumentar su golpe en un 20%")


class GuerreroUT616(Personaje): # Guerrero Universo Tierra-616
    def __init__(self,_EnergiaMinima,_EnergiaMaxima,_nombre,_tipo,_vida,_distancia):
        
        super().__init__(_nombre,_tipo,_vida,_distancia)
        self.EnergiaMinima=_EnergiaMinima
        self.EnergiaMaxima=_EnergiaMaxima
        
    def SuperPoder(self,_oponente): # HABILIDAD ESPECIAL DE IRON MAN
        self.golpe = random.randint(self.EnergiaMinima, self.EnergiaMaxima)
        self.golpe=self.golpe+10
        
        print(self.nombre , "realiza un ataque especial (Super Poder) de" , self.golpe , "de daño a" , _oponente.nombre)
        _oponente.vida = _oponente.vida - self.golpe

    def Descripcion(self):
        super().Descripcion()
        print("Energia Minima: ", self.EnergiaMinima,"\nEnergia Maxima: ",self.EnergiaMaxima, "\nHabilidad especial: Realizar un super poder para aumentar su golpe en +10")

class GuerreroCreado(Personaje):
    def __init__(self,_PotenciaMinima,_PotenciaMaxima,_nombre,_tipo,_vida,_distancia):
        
        super().__init__(_nombre,_tipo,_vida,_distancia)
        self.PotenciaMinima=_PotenciaMinima
        self.PotenciaMaxima=_PotenciaMaxima
        
    def DefensaEspecial(self,_oponente): #HABILIDAD ESPECIAL DEL JUGADOR CREADO
        self.vida = self.vida + _oponente.golpe
        print(self.nombre , "realiza una defensa especial y bloquea el ultimo golpe recibido")

    def Descripcion(self):
        super().Descripcion()
        print("Potencia Minima: ", self.PotenciaMinima,"\nPotencia Maxima: ",self.PotenciaMaxima, "\nHabilidad especial: Bloquear todo el dano del ultimo golpe recibido")



def CrearGuerrero():
    global nombreC,tipoC,vidaC,ataMin,ataMax,objGuerrero
    print("********** CREACION DE GUERRERO **********")
    nombreC = input("Ingrese el nombre: ")
    tipoC = input("Ingrese el tipo 'Tierra' o 'Espacio': ")
    while(tipoC != "tierra" and tipoC != "Tierra" and tipoC != "espacio" and tipoC != "Espacio"):
        print("valor incorrecto")
        tipoC = input("Ingrese el tipo 'Tierra' o 'Espacio': ")
    vidaC = int(input("Ingrese su vida: "))
    while(vidaC<0):
        print("vida no valida")
        vidaC = int(input("Ingrese su vida: "))
    ataMin = int(input("Ingrese el ataque minimo de su personaje: "))
    while(ataMin<0):
        print("Ataque minimo no valido debe ser superior a 0")
        ataMin = int(input("Ingrese el ataque minimo de su personaje: "))
    ataMax = int(input("Ingrese el ataque maximo de su personaje: "))
    while(ataMin>ataMax):
        print("Ataque maximo no valido, debe ser superior o igual a", ataMin)
        ataMax = int(input("Ingrese el ataque maximo de su personaje: "))
    objGuerrero = GuerreroCreado(ataMin, ataMax, nombreC, tipoC, vidaC, 10)
    

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
  
def salir():
    system("cls")
    delay_print     ("\n\n\t\t \033[0;37;45m" + "|**|    Juego programado por:      |**|" + "\033[0;m \n")
    delay_print         ("\t\t \033[0;37;45m" + "|**|    - Nicolas Cortes Alfaro    |**|" + "\033[0;m \n")
    delay_print         ("\t\t \033[0;37;45m" + "|**|    - Ignacio Lamilla Rojas    |**|" + "\033[0;m \n")
    delay_print       ("\n\t\t \033[0;37;45m" + "|**|    Gracias por jugar!  :)     |**|" + "\033[0;m \n")
    time.sleep(2)
    
    system("cls")
    print ("Cerrando Juego..")
    time.sleep(0.8)
    system("cls")
    print ("Cerrando Juego...")
    time.sleep(0.8)
    system("cls")
    print ("Cerrando Juego....")
    time.sleep(0.8)
    
    exit()    
    
def main():
    empezar=int(input("\t\t\t******** GUERRA DE LOS UNIVERSOS ********\n\nDesea ingresar al juego? 1) SI  2) NO: "))
    while(empezar<1 or empezar>2):
        print("valor no valido")
        empezar=int(input("Desea ingresar al menu 1) SI  2) NO: "))
    while empezar==1:
        Superman= GuerreroUT1(100, 200, "Superman", "Espacio", 1000, 10)
        Goku= GuerreroU7(100, 200, "Goku", "Tierra", 1000, 10)
        IronMan= GuerreroUT616(100, 200, "Iron Man", "Tierra", 500, 10)
        if 'objGuerrero' in globals():
            objGuerrero = GuerreroCreado(ataMin, ataMax, nombreC, tipoC, vidaC, 10)  
        system("cls")
        print("\n")
        print("|****************************|")
        print("|**|      MENU DEL        |**|")
        print("|**|       JUEGO          |**|")
        print("|****************************|")
        print("Fecha actual:",diaActual,"-",mesActual,"-",añoActual)
        print("\nSeleccione una de las siguientes opciones:");
        print("1.- REGLAS DEL JUEGO")
        print("2.- DESCRIPCION DE GUERREROS")
        print("3.- ELECCION DE GUERREROS")
        print("4.- COMENZAR BATALLA")
        print("5.- CREA A TU GUERRERO")
        print("6.- Salir\n")

        opcion = int(input("Opcion: "))
        
        if opcion == 1:
            system("cls")
            print("\nEste es un juego de dos jugadores, en el que cada jugador debe elegir a uno de los guerreros disponibles para posteriormente batallar")
            print("Es un juego por rondas. En cada ronda ambos jugadores tienen un turno para realizar dos acciones: ")
            print("1. Avanzar o retroceder (1 o 2 metros dependiendo del azar)")
            print("2. Atacar, defender o realizar una habilidad especial (esta solo se puede activar una vez por partida)")
            print("El dano defendido dependera de la distancia en la que se encuentren los guerreros")
            print("10 metros o mas: 80% del dano defendido")
            print("Entre 10 y 5 metros: 50% del dano defendido")
            print("Menos de 5 metros: 10% del dano defendido")
            print("\nNOTA: Si el guerrero es tipo 'TIERRA' su vida tiene un aumento del 20%, en cambio si su guerrero es tipo 'ESPACIO' tiene un descuento de vida del 20% pero un aumento de ataque del 20%")
            print("\nGana el jugador que en alguna de las rondas, logre dejar al oponente con 0 de vida ")
            print("En el caso que ambos jugadores terminen una ronda con 0 de vida, el resultado de la partida sera un empate")
            input("\nPresione ENTER para continuar...")

        elif opcion == 2:
            system("cls")
            print("\nGUERREROS UNIVERSO TIERRA-1")
            Superman.Descripcion() 
            
            print("\nGUERREROS UNIVERSO 7")
            Goku.Descripcion()
            
            print("\nGUERREROS UNIVERSO TIERRA-616")
            IronMan.Descripcion()
            
            if 'objGuerrero' in globals():
                print("\nGUERRERO CREADO")
                objGuerrero.Descripcion()
            
            input("\nPresione ENTER para continuar...")
       
        elif opcion ==3:
            system("cls")
            if 'objGuerrero' in globals():
                Jugador1=int(input("Jugador 1, elige a un guerrero.  1) Superman  2) Goku  3) Iron Man 4) Jugador Creado: "))
                if Jugador1==1:
                    Jugador1=Superman
                elif Jugador1==2:
                    Jugador1=Goku
                elif Jugador1==3:
                    Jugador1=IronMan
                elif Jugador1==4:
                    Jugador1=objGuerrero
                
                Jugador2=int(input("\nJugador 2, elige a un guerrero.  1) Superman  2) Goku  3) Iron Man 4) Jugador Creado: "))
                if Jugador2==1:
                    Jugador2=Superman
                elif Jugador2==2:
                    Jugador2=Goku
                elif Jugador2==3:
                    Jugador2=IronMan
                elif Jugador2==4:
                    Jugador2=objGuerrero
                    
                print("\nJugador 1 tu Guerrero elegido Fue:")    
                Jugador1.Descripcion()
                print("\nJugador 2 tu Guerrero elegido Fue:")
                Jugador2.Descripcion()    
            else:    
                Jugador1=int(input("Jugador 1, elige a un guerrero.  1) Superman  2) Goku  3) Iron Man : "))
                if Jugador1==1:
                    Jugador1=Superman
                elif Jugador1==2:
                    Jugador1=Goku
                elif Jugador1==3:
                    Jugador1=IronMan 
               
                
                Jugador2=int(input("\nJugador 2, elige a un guerrero.  1) Superman  2) Goku  3) Iron Man: "))
                if Jugador2==1:
                    Jugador2=Superman
                elif Jugador2==2:
                    Jugador2=Goku
                elif Jugador2==3:
                    Jugador2=IronMan   
                    
                print("\nJugador 1 tu Guerrero elegido Fue:")    
                Jugador1.Descripcion()
                print("\nJugador 2 tu Guerrero elegido Fue:")
                Jugador2.Descripcion()
            
            input("\nPresione ENTER para continuar...")
        
        elif opcion ==4:
            system("cls")
            
            print("\t\t|****************************|")
            print("\t\t|**  COMIENZA LA BATALLA!  **|")
            print("\t\t|****************************|")
            
            ronda = 1
            while(Jugador1.vida>0 and Jugador2.vida>0):
                
                print("\n\n\t\t \033[0;37;44m" + " *** RONDA NUMERO" , ronda , "***" + "\033[0;m")
                print("\n \033[0;37;44m" + " TURNO DE JUGADOR 1   (" , Jugador1.nombre , ")" + "\033[0;m \n")
    
                #-------------JUGADOR 1----------------AVANZAR O RETROCEDER-------------------------------------------
    
                avanzarRetroceder=int(input("Presione 1 para avanzar o 2 para retroceder: "))
                while(avanzarRetroceder<1 or avanzarRetroceder>2):
                    print("valor no valido")
                    avanzarRetroceder=int(input("Presione 1 para avanzar o 2 para retroceder: "))
                
                #caso decide avanzar
                if avanzarRetroceder == 1:
                    Jugador1.Avanzar(Jugador2)
                    if Jugador1.distancia<0:
                        print("***" , Jugador1.nombre , "avanza. Los jugadores cambiaron de lado ahora la distancia entre los guerreros es de" , (-1)*Jugador1.distancia , "metros ***")
                    else:
                        print("***" , Jugador1.nombre , "avanza. Ahora la distancia entre los guerreros es de" , Jugador1.distancia , "metros ***")

                #caso decide retroceder
                elif avanzarRetroceder == 2:
                    Jugador1.Retroceder(Jugador2)
                    if Jugador1.distancia<0:
                        print("***" , Jugador1.nombre , "retrocede. Los jugadores cambiaron de lado ahora la distancia entre los guerreros es de" , (-1)*Jugador1.distancia , "metros ***")
                        
                    else:    
                        print("***" , Jugador1.nombre , "retrocede. Ahora la distancia entre los guerreros es de" , Jugador1.distancia , "metros ***")
    
                #-------------JUGADOR 1----------------ATACAR, HABILIDAD ESPECIAL O DEFENDER-------------------------------------------
    
                atacarDefender=int(input("\nPresione (1) para atacar || (2) para una habilidad especial || (3) para defender: "))
                while(atacarDefender<1 or atacarDefender>3):
                    print("valor no valido")
                    atacarDefender=int(input("Presione (1) para atacar || (2) para una habilidad especial || (3) para defender: "))
    
                while(atacarDefender == 2 and Jugador1.especial == False):
                    print("Ya usaste tu habilidad especial, por favor selecciona otra opcion")
                    atacarDefender=int(input("Presione (1) para atacar || (2) para una habilidad especial || (3) para defender: "))
                    while(atacarDefender<1 or atacarDefender>3):
                        print("valor no valido")
                        atacarDefender=int(input("Presione (1) para atacar || (2) para una habilidad especial || (3) para defender: "))
    
                #caso decide atacar
                if atacarDefender == 1:
                    Jugador1.Atacar(Jugador2)
                    print("\033[0;37;41m" + "*** La vida de" , Jugador2.nombre , "baja a" , Jugador2.vida , "***" + "\033[0;m")
                
                #caso decide habilidad especial)
                elif atacarDefender==2:
                    if Jugador1.especial == True:
                        if Jugador1.nombre=="Superman":
                            Jugador1.Llamar_al_Compañero(Jugador2)
                            print("\033[0;37;41m" + "*** La vida de" , Jugador2.nombre , "baja a" , Jugador2.vida, "***" + "\033[0;m")
                        elif Jugador1.nombre=="Goku":
                            Jugador1.Transformacion(Jugador2)
                            print("\033[0;37;41m" + "*** La vida de" , Jugador2.nombre , "baja a" , Jugador2.vida, "***" + "\033[0;m")
                        elif Jugador1.nombre=="Iron Man":
                            Jugador1.SuperPoder(Jugador2)
                            print("\033[0;37;41m" + "*** La vida de" , Jugador2.nombre , "baja a" , Jugador2.vida, "***" + "\033[0;m")
                        elif Jugador1.nombre==objGuerrero.nombre:
                            Jugador1.DefensaEspecial(Jugador2)
                            print("\033[0;37;42m" + "*** La vida de" , Jugador1.nombre , "aumenta a" , Jugador1.vida, "***" + "\033[0;m")
                        Jugador1.especial=False # Se cambia al atributo especial a "False", para que el jugador no pueda volver a utilizar la habilidad especial
    
                #caso decide defender
                elif atacarDefender == 3:
                    Jugador1.Defender(Jugador2)
                    print("\033[0;37;42m" + "***" , Jugador1.nombre , "se defendio de" , Jugador2.nombre , ". La vida de" , Jugador1.nombre , "ahora es de" , Jugador1.vida , "***" + "\033[0;m")
    
                
                '''-------------------------------------------------------------------------------------------------------------------------------
                ----------------------------------------------------------------------------------------------------------------------------------
                -------------------------------------------------------------------------------------------------------------------------------'''
    
                print("\n\n \033[0;37;44m" + " TURNO DE JUGADOR 2   (" , Jugador2.nombre , ")" + "\033[0;m \n")
    
                #-------------JUGADOR 2----------------AVANZAR O RETROCEDER-------------------------------------------
    
                avanzarRetroceder=int(input("Presione 1 para avanzar o 2 para retroceder: "))
                while(avanzarRetroceder<1 or avanzarRetroceder>2):
                    print("valor no valido")
                    avanzarRetroceder=int(input("Presione 1 para avanzar o 2 para retroceder: "))
                #caso decide avanzar
                if avanzarRetroceder == 1:
                    Jugador2.Avanzar(Jugador1)
                    if Jugador2.distancia<0:
                        print("*** ",Jugador2.nombre , "avanza. Los jugadores cambiaron de lado ahora la distancia entre los guerreros es de" , (-1)*Jugador2.distancia , "metros ***")
                   
                    else:
                        print("*** ",Jugador2.nombre , "avanza. Ahora la distancia entre los guerreros es de" , Jugador2.distancia , "metros ***")
                #caso decide retroceder
                elif avanzarRetroceder == 2:
                    Jugador2.Retroceder(Jugador1)
                    if Jugador2.distancia<0:
                        print("*** ",Jugador2.nombre , "retrocede. Los jugadores cambiaron de lado ahora la distancia entre los guerreros es de" , (-1)*Jugador2.distancia , "metros ***")

                    else:    
                        print("*** ",Jugador2.nombre , "retrocede. Ahora la distancia entre los guerreros es de" , Jugador2.distancia , "metros ***")
    
                #-------------JUGADOR 2----------------ATACAR, HABILIDAD ESPECIAL O DEFENDER-------------------------------------------
    
                atacarDefender=int(input("\nPresione (1) para atacar || (2) para una habilidad especial|| (3) para defender: "))
                while(atacarDefender<1 or atacarDefender>3):
                    print("valor no valido")
                    atacarDefender=int(input("Presione (1) para atacar || (2) para una habilidad especial|| (3) para defender: "))
    
                while(atacarDefender == 2 and Jugador2.especial == False):
                    print("Ya usaste tu habilidad especial, por favor selecciona otra opcion")
                    atacarDefender=int(input("Presione (1) para atacar || (2) para una habilidad especial || (3) para defender: "))
                    while(atacarDefender<1 or atacarDefender>3):
                        print("valor no valido")
                        atacarDefender=int(input("Presione (1) para atacar || (2) para una habilidad especial || (3) para defender: "))
                
                #caso decide atacar
                if atacarDefender == 1:
                    Jugador2.Atacar(Jugador1)
                    print("\033[0;37;41m" + "*** La vida de" , Jugador1.nombre , "baja a" , Jugador1.vida, "***" + "\033[0;m")
                
                #caso decide habilidad especial
                elif atacarDefender==2:
                    if Jugador2.especial == True:
                        if Jugador2.nombre=="Superman":
                            Jugador2.Llamar_al_Compañero(Jugador1)
                            print("\033[0;37;41m" + "*** La vida de" , Jugador1.nombre , "baja a" , Jugador1.vida, "***" + "\033[0;m")
                        elif Jugador2.nombre=="Goku":
                            Jugador2.Transformacion(Jugador1)
                            print("\033[0;37;41m" + "*** La vida de" , Jugador1.nombre , "baja a" , Jugador1.vida, "***" + "\033[0;m")
                        elif Jugador2.nombre=="Iron Man":
                            Jugador2.SuperPoder(Jugador1)
                            print("\033[0;37;41m" + "*** La vida de" , Jugador1.nombre , "baja a" , Jugador1.vida, "***" + "\033[0;m")
                        elif Jugador2.nombre==objGuerrero.nombre:
                            Jugador2.DefensaEspecial(Jugador1)
                            print("\033[0;37;42m" + "*** La vida de" , Jugador2.nombre , "aumenta a" , Jugador2.vida, "***" + "\033[0;m")
                        Jugador2.especial=False # Se cambia al atributo especial a "False", para que el jugador no pueda volver a utilizar la habilidad especial
                
                #caso decide defender
                elif atacarDefender == 3:
                    Jugador2.Defender(Jugador1)
                    print("\033[0;37;42m" + "***" , Jugador2.nombre , "se defendio de" , Jugador1.nombre , ". La vida de" , Jugador2.nombre , "ahora es de" , Jugador2.vida , "***" + "\033[0;m")
                
                ronda+=1
    
            #-------------GANADOR------------- 
    
            if (Jugador1.vida<=0 and Jugador2.vida<=0 ):
                print("\n\n\t \033[0;37;43m" + " SE TERMINO LA BATALLA, ESTO FUE UN EMPATE" + "\033[0;m")
                
            elif (Jugador1.vida<=0):
                print("\n\n\t \033[0;37;43m" + " SE TERMINO LA BATALLA, GANADOR:", Jugador2.nombre + "\033[0;m")
                print("\t \033[0;37;43m" + " ¡FELICITACIONES!" + "\033[0;m")
            elif (Jugador2.vida<=0):
                print("\n\n\t \033[0;37;43m" + " SE TERMINO LA BATALLA, GANADOR:", Jugador1.nombre + "\033[0;m")
                print("\t \033[0;37;43m" + " ¡FELICITACIONES!" + "\033[0;m")
                   
            #---------------------

            input("\nPresione ENTER para continuar...")
        
        elif opcion ==5:
            system("cls")
            CrearGuerrero()
            input("\nPresione ENTER para continuar...")
        
        elif opcion ==6:
            system("cls")
            empezar=2
          
    while empezar==2 :
        salir()


if __name__ == '__main__':
    main();