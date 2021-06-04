# Búsqueda: búsqueda heurística

#### Ana Cecilia Caiceros Lagunes, Miguel Angel Lopez Sandria y Kenia Karla Iasaret Sánchez Ortiz

## **I. Introducción**
Este es un trabajo sobre la _búsqueda heurística_, iniciaremos definiendo lo que son las **búsquedas**.
Las búsqueda son una serie de esquemas que ayudan a la representación de diversos algoritmos, los cuales nos permite resolver problemas dando idea a lo que refiere el algoritmo.
Es decir, son métodos en los que un agente puede seleccionar acciones, para poder encontrar la solución de un problema. En tales casos, el agente puede construir secuencias de acciones que nos permiten alcanzar los objetivos; a este proceso se le llama búsqueda.
Los elementos que integran las búsqueda son:
* CONJUNTO DE ESTADO:
Todas las configuraciones posibles en el dominio.
* ESTADOS INICIALES:
Estados desde los que partimos, es decir nuestro punto inicial.
* ESTADOS FINALES:
Las soluciones del problema.
* OPERADORES:
Se aplica para pasar de un estado a otro.
* SOLUCIONADOR:
Mecanismo que nos permite evolucionar de un estado a otro mediante un algoritmo.

Las búsquedas se clasifican en:
*No heurística:
Este tipo de búsqueda intenta encontrar  la  primer solución sin importar que tan optima sea, no detecta si está aproximando o alejado de la solución.
entre estas tenemos:
  * Por amplitud
  * Costo uniforme
  * Por profundidad

*Heurística:
Las heurísticas son criterios, métodos o principios para decidir cual de entre varias acciones promete ser la mejor para alcanzar una determinada meta.
Entre estas tenemos:

  * Greedy
  * A*
  * Algoritmos genéticos

Nos enfocaremos en el método de búsqueda heurística.

## **II. Búsquedas heurísticas**

En las búsquedas, nos podemos guiar con heurísticas que nos den una indicacion acerca de que tan bueno o prometedor es un determinado estado u operador.
>*El uso de heuríscicas nos permite guiar nuestra búsqieda de una solución más rápidamente que si hubieramos utilizado estrategias _no heurísticas_.

>*Una heurística será una función que utilizaremos para estimar qué tan cerca estamos de una solución. Cada una estará diseñada para un problema de búsqueda en particular.

La heurística consta de varios procesos, tales como:

| Búsqueda voraz _Primero el mejor_    |
| :-----------------------------------:|
| Distancia en línea recta             |
| Búsqueda A*                          |
| Heurística admisible                 |
| Consistencia                         |
| Monotonía                            |
| Desigualdad triangular               |
| Curvas de nivel                      | 
| Poda                                 |
| Optimamente eficiente                |


## **III. Experimento**
En este apartado se explicará y se llevará acabo la explicación a pequeños rasgos del trabajo realizado.

>Se inicia mostrando un listado de lugares dentro del estado de Veracruz para elegir.

![estados](https://user-images.githubusercontent.com/79228016/120760918-471e1300-c4da-11eb-8a5a-328ebdcfd895.jpg).

>Primero debes seleccionar tu lugar de origen.

![origen](https://user-images.githubusercontent.com/79228016/120845370-5c288f80-c536-11eb-8a4c-1a78e41ce6e5.jpg).

>De esta lista se selecciona el destino para iniciar la ruta.

![destino](https://user-images.githubusercontent.com/79228016/120844969-c42aa600-c535-11eb-9e17-27426656275a.jpg).

>Eliges el método con el que quieres trabjar tu ruta, entre ellos está el método _Greedy_ y _A*_

![metodo](https://user-images.githubusercontent.com/79228016/120845673-c2adad80-c536-11eb-8629-2035332890c7.jpg)

>Seguido de eso está un boton con el nombre de _BUSCAR_, éste hará el comienzo del proceso una vez se haya seleccionado toda la información.
 
 ![buscar](https://user-images.githubusercontent.com/79228016/120845894-06a0b280-c537-11eb-878f-4084ef70fb67.jpg)
 
 >Finalmente, aparecerá la ruta que se encontró y que para el programa resulta más conveniente.
 
 ![ruta](https://user-images.githubusercontent.com/79228016/120846294-84fd5480-c537-11eb-8e8f-ea2d5ac519e3.jpg)


## **. Bibliografía**

* [1] Stuart J. Russell y Peter Norvig. Inteligencia artificial, un enfoque moderno. _Segunda edición_ .

* [2] Video Clandestina: http://clandestina-hds.com/busquedasFinalProyect/busquedasFinalProyect.html 

* [3] Búsqueda heurística: https://elvex.ugr.es/decsai/iaio/slides/A5%20Heuristic%20Search.pdf

