# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 07:08:21 2020

@author: Sebastian
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 06:52:33 2020

@author: Sebastian
"""
import numpy as np
import gc

class Pila:
  def __init__(self):
    self.items=[]
    self.nele=0
  
  def push(self, elemento):
    self.items.insert(0,elemento)
    self.nele+=1
  
  def pop(self, lista, indicie):
    if not lista.es_vacia():
      self.items.pop(indicie)
      self.nele-=1
      return(True)
    else:
      return(False)
  
  def imprimir_pila(self):
    for i in range(len(self.items)):
        print(i , ": ", self.items[i])
        
  def imprimir_elemento(self, lista, indice):
    return self.items[indice]
  
  def tiempo_total(self):
    tiemposumado = 0
    for i in range(int(milista.num_elementos() or 0)):
        tiemposumado = tiemposumado + int(self.imprimir_elemento(milista, i).tiempo or 0)
    return tiemposumado

  def tiempo_elemento(self, lista, indice):
    return self.items[indice].tiempo

  def tiempo_demora_total_cada_cliente(self, lista, indice):
    slicelist = self.items[indice:int(milista.num_elementos())]
    sumatiempo = 0
    for item in slicelist:
        sumatiempo = sumatiempo + item.getTiempo()
    return sumatiempo
      
  def mover_elementos(self, el1, el2):
    aux = self.items[el2]
    self.items[el2] = self.items[el1]
    self.items[el1] = aux

  def num_elementos(self):
    return len(self.items)

  def es_vacia(self):
    return(self.nele==0)

class cliente:
   def __init__(self, nombre, tipoCliente, terceraEdad, tipoOperacion):
       self.nombre = nombre;
       self.tipoCliente = tipoCliente;
       self.terceraEdad = terceraEdad;
       self.tipoOperacion = tipoOperacion;
       self.tiempo = 0
       
       if(self.tipoOperacion=='Consignacion'):
           if(self.terceraEdad=='True'):
               self.tiempo = 12
           else:
               self.tiempo = 8
       elif(self.tipoOperacion=='Retiro'):
           if(self.terceraEdad=='True'):
               self.tiempo = 9
           else:
               self.tiempo = 6
       elif(self.tipoOperacion=='Transferencia'):
           if(self.terceraEdad=='True'):
               self.tiempo = 10
           else:
               self.tiempo = 6
       
   def getNombre(self):
       return self.nombre
   def getTipoOperacion(self):
       return self.tipoOperacion
   def getTiempo(self):
       return self.tiempo
   def getTipoCliente(self):
       return self.tipoCliente
   def getTerceraEdad(self):
       return self.terceraEdad
   def __repr__(self):
       return cliente()
   def __str__(self):
       return "Nombre: %s, Tipo de cliente: %s, Tercera edad: %s, Tipo Operacion: %s, Tiempo que se demora: %s" % (self.getNombre(), 
                                                                                                                   self.getTipoCliente(), 
                                                                                                                   self.getTerceraEdad(), 
                                                                                                                   self.getTipoOperacion(), 
                                                                                                                   self.getTiempo())


file = 'data_set.txt'

data = np.loadtxt(file,dtype=bytes, delimiter=',', usecols=(0,1,2,3)).astype(str)

lista = {}
lista_objetos = []

for i in range(len(data)):
    lista[i] = data[i,:]
    globals()['cliente{}'.format(i)] = cliente(lista[i][0],lista[i][1],lista[i][2],lista[i][3])

for obj in gc.get_objects():
    if isinstance(obj, cliente):
        lista_objetos.append(obj)
        
milista = Pila()
sumatotaltiempos = 0
for i in range(len(lista_objetos)):
    milista.push(lista_objetos[i])
    try:
        if(milista.imprimir_elemento(milista, 0).tipoCliente == 'Preferencial' 
           and milista.imprimir_elemento(milista, 1).tipoCliente!='Preferencial'
           and milista.imprimir_elemento(milista, 2).tipoCliente!='Preferencial'):
            milista.mover_elementos(0,2);
        elif(milista.imprimir_elemento(milista, 0).tipoCliente == 'Preferencial' 
           and milista.imprimir_elemento(milista, 1).tipoCliente!='Preferencial'):
            milista.mover_elementos(0,1);
            
        if(milista.imprimir_elemento(milista, 0).terceraEdad == 'True' 
           and milista.imprimir_elemento(milista, 1).terceraEdad!='True'
           and milista.imprimir_elemento(milista, 2).terceraEdad!='True'
           and milista.imprimir_elemento(milista, 3).terceraEdad!='True'):
            milista.mover_elementos(0,3);
        elif(milista.imprimir_elemento(milista, 0).terceraEdad == 'True' 
           and milista.imprimir_elemento(milista, 1).terceraEdad!='True'
           and milista.imprimir_elemento(milista, 2).terceraEdad!='True'):
            milista.mover_elementos(0,2);
        elif(milista.imprimir_elemento(milista, 0).terceraEdad == 'True' 
           and milista.imprimir_elemento(milista, 1).terceraEdad!='True'):
            milista.mover_elementos(0,1);
    except:
            continue;
    
print("""
      -------------------------------------------------------------------------------------
      Imprimiendo la lista inicial(lista en reversa sin modificaciones de orden adicionales)
      -------------------------------------------------------------------------------------
      """)
i = 0
for item in reversed(lista_objetos):
    print(i,": ",item)
    i+=1
    
print("""
      --------------------------------------------------
                Imprimiendo la cola organizada
      --------------------------------------------------
      """)
milista.imprimir_pila()

print("""
      ----------------------------------------------------------
           Tiempo total para atender a todos los clientes
      ----------------------------------------------------------
      """)

print(milista.tiempo_total()," minutos")
print("""
      ----------------------------------------------------------
          Promedio general del tiempo de la transaccion
      ----------------------------------------------------------
      """)

print((milista.tiempo_total()/milista.num_elementos())," minutos")


print("""
      ----------------------------------------------------------
            Tiempo promedio que se demora un preferencial
      ----------------------------------------------------------
      """)


nombreAux = 'Preferencial'
indiceAux = []
tiempoAux = 0
for i in range(milista.num_elementos()):
    if(milista.imprimir_elemento(milista, i).tipoCliente==nombreAux):
        indiceAux.append(i)
    else:
        continue

tiempoPreferencialtotal = 0
for i in range(len(indiceAux)):
    tiempoAux = milista.tiempo_demora_total_cada_cliente(milista, indiceAux[i])
    tiempoPreferencialtotal += tiempoAux

print(tiempoPreferencialtotal/len(indiceAux) ," minutos")

print("""
      ------------------------------------------------------------
      Tiempo promedio que se demora una persona de la tercera edad
      ------------------------------------------------------------
      """)


nombreAux = 'True'
indiceAux = []
tiempoAux = 0
for i in range(milista.num_elementos()):
    if(milista.imprimir_elemento(milista, i).terceraEdad==nombreAux):
        indiceAux.append(i)
    else:
        continue

tiempoTerceraEdadTotal = 0
for i in range(len(indiceAux)):
    tiempoAux = milista.tiempo_demora_total_cada_cliente(milista, indiceAux[i])
    tiempoTerceraEdadTotal += tiempoAux

print(tiempoTerceraEdadTotal/len(indiceAux) ," minutos")
