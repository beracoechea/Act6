from particulas import Particula

class Lista:

    def __init__ (self):
            self.__Lista = []

    def agregar_final(self, particulas:Particula ):
            self.__Lista.append(particulas)
        
     
    def agregar_inicio(self, particulas:Particula ):
            self.__Lista.insert(0, particulas)
            

    def mostrar(self):
            for particulas in self.__Lista:
                print(particulas)

    def __str__(self):
        return "".join(
           str(particulas) + '\n' for particulas in self.__Lista

        )
          

