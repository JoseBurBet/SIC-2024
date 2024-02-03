jugables={
    "raza":{
        "humano":{
            "clase":{
                "guerrero":{
                    "stats":{
                        "vida":"1200",
                        "mana":"900"
                        }
                    },
                "cazador":{
                    "stats":{
                        "vida":"800",
                        "mana":"1200"
                        }
                    }
                }
           },
        "orco":{
            "clase":{
                "chaman":{
                    "stats":{
                        "vida":"900",
                        "mana":"1500"
                        }
                    },
                "brujo":{
                    "stats":{
                        "vida":"600",
                        "mana":"2000"
                        }
                    }
                }
            },
        "elfo":{
            "clase":{
                "druida":{
                    "stats":{
                        "vida":"2000",
                        "mana":"1300"
                        }
                    },
                "mago":{
                    "stats":{
                        "vida":"600",
                        "mana":"1800"
                        }
                    }
                }
            }
        }
    }


#03/02/2024
#Ejemplo de tutoria
#Profe Jose
#Simulador de creacion de personajes para WoW empleando todo
#lo visto en las bases de programacion

#_________________________librerias_______________________
import uuid
import json
#_________________________variables globales______________
data={}
data["personajes_creados"]=[]


#__________________________clases__________________________

class personaje():

    def __init__(self,nombre,raza,clase,vida,mana):
        self.nombre=nombre
        self.raza=raza
        self.clase=clase
        self.vida=vida
        self.mana=mana

    #________________getters_____________________

    def get_nombre(self):
        return self.nombre
    def get_raza(self):
        return self.raza
    def get_clase(self):
        return self.clase
    def get_vida(self):
        return self.vida
    def get_mana(self):
        return self.mana

    #________________setters________________________


    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_raza(self,raza):
        self.raza=raza
    def set_clase(self,clase):
        self.clase=clase
    def set_vida(self,vida):
        self.vida=vida
    def set_mana(self,mana):
        self.mana=mana
    
#____________________________Metodos___________________________


    def guardar_personaje(self,datos):
        data["personajes_creados"].append(datos) # agrega datos a la lista de personajes
        pjs=data["personajes_creados"]
        archivo=open("personajes.json","w")
        json.dump(pjs,archivo,indent=4)
        

    
    def crear_personaje(self,raza,clase):
        
        vida=jugables["raza"][raza]["clase"][clase]["stats"]["vida"]
        mana=jugables["raza"][raza]["clase"][clase]["stats"]["mana"]
        
        nombre=input("\n Ingresa el nombre de tu personaje \n > ")
        
        nuevo_pj=personaje(nombre,raza,clase,vida,mana)
        #El diccionario de datos es lo que guardare en la memoria, NO GUARDO UN OBJETO
        datos={
            "id":str(uuid.uuid4()),
            "nombre":nuevo_pj.get_nombre(),
            "raza":nuevo_pj.get_raza(),
            "clase":nuevo_pj.get_clase(),
            "vida":nuevo_pj.get_vida(),
            "mana":nuevo_pj.get_mana()
            }
        
        self.guardar_personaje(datos)
        print(f"\n El personaje {nombre} ha sido creado")

        
    def menu_creacion(self):
        print("\n ¿que personaje desea crear? \n 1) humano \n 2) orco \n 3) elfo")
        raza=input("\n > ")

        try:
            if raza=="1" or raza=="humano" or raza=="Humano" or raza=="HUMANO":
                raza="humano"
                print("\n Que clase desea jugar? \n 1) guerrero \n 2) cazador")
                clase=input("\n > ")
                if clase=="1" or clase=="guerrero" or clase=="GUERRERO":
                    clase="guerrero"
                    self.crear_personaje(raza,clase)
                elif clase=="2" or clase=="cazador" or clase=="CAZADOR":
                    clase="cazador"
                    self.crear_personaje(raza,clase)
                else:
                    print("comando invalido en la seleccion de clase")
                
            elif raza=="2" or raza=="orco" or raza=="Orco" or raza=="ORCO":
                raza="orco"
                print("\n Que clase desea jugar? \n 1) chaman \n 2) brujo")
                clase=input("\n > ")
                if clase=="1" or clase=="chaman" or clase=="CHAMAN":
                    clase="chaman"
                    self.crear_personaje(raza,clase)
                elif clase=="2" or clase=="brujo" or clase=="BRUJO":
                    clase="brujo"
                    self.crear_personaje(raza,clase)
                else:
                    print("comando invalido en la seleccion de clase")
            elif raza=="3" or raza=="elfo" or raza=="Elfo" or raza=="ELFO":
                raza="elfo"
                print("\n Que clase desea jugar? \n 1) druida \n 2) mago")
                clase=input("\n > ")
                if clase=="1" or clase=="druida" or clase=="DRUIDA":
                    clase="druida"
                    self.crear_personaje(raza,clase)
                elif clase=="2" or clase=="mago" or clase=="MAGO":
                    clase="mago"
                    self.crear_personaje(raza,clase)
                else:
                    print("comando invalido en la seleccion de clase")
            else:
                print("comando invalido en la seleccion de raza")
                
        except Exception as e:
                print(f"Error : {e}")

                   

    def interfaz(self):

        while True:
            print("\n Bienvenido al creador de personajes. \n ¿que desea hacer? \n 1) crear personaje \n 2) ver los personajes creados \n 3) salir del programa")
            opcion=input("\n > ")

            try:
                if opcion == "1":
                    self.menu_creacion()
                elif opcion=="2":
                    self.ver_personajes()
        
                elif opcion=="3":
                    print("\n Cerrando el programa")
                    quit()
                else:
                    print("comando incorrecto")
                   
            except Exception as e:
                    print(f"Error : {e}")
    def ver_personajes(self):
                        
                        archivo = open("personajes.json", "r")
                        # abre el archivo en modo lectura
                        pjs = json.load(archivo)
                        # carga los datos del archivo
                        print("\nPersonajes creados\n")
                        for pj in pjs:
                            print(f'ID: {pj["id"]}')
                            print(f'Nombre: {pj["nombre"]}')
                            print(f'Raza: {pj["raza"]}')
                            print(f'Clase: {pj["clase"]}')
                            print(f'Vida: {pj["vida"]}')
                            print(f'Mana: {pj["mana"]}')
                            print("\n")
                            archivo.close()
                        wait = input("\nPresione enter para continuar")
                            
class iniciar(personaje):

    def __init__(self):
        self.interfaz()
     


#______________________________Main______________________________


#driver

if __name__=='__main__':
    iniciar()
    




