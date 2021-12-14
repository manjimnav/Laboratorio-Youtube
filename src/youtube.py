# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:49:48 2019

@author: Toñi Reina
@Revisor: fermincruz, Mariano González
ÚLTIMA MODIFICACIÓN: 24/01/2020
"""

import csv

from collections import namedtuple
from datetime import datetime, date
from collections import Counter

Video = namedtuple('Video', 'id_video,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes')

def lee_trending_videos(fichero):
    '''
    Lee un fichero de entrada en formato CSV y devuelve una lista de tuplas
    de tipo Video conteniendo todos los datos almacenados en el fichero.    
    Use: datetime.strptime(cadena_fecha,'%d/%m/%Y').date() para convertir una cadena a fecha
    Recuerde que puede usar el parámetro delimiter en el reader
    Entrada:
     - fichero: ruta del fichero csv que contiene los datos en codificación utf-8 
         -> str

    Salida:
     - videos: lista de tuplas con la información del fichero
         -> [Video(str,date,str,str,str,int,int,int)]   
    '''
    pass

def media_visitas(videos, fecha):
    '''
    Devuelve la media de visitas de una fecha dada. Si para esa fecha
    no hay registros la función devuelve cero.
    Entrada:
     - video: lista de tuplas con la información de vídeos trending
         -> [Video(str,date,str,str,str,int,int,int)]
     - fecha: fecha -> date

    Salida:
     - media de visitas de esa fecha
         -> float
    '''    
    pass

def video_mayor_ratio_likes_dislikes(videos, categoria=None):
    '''
    Devuelve la tupla de tipo Video de la categoría dada como parámetro que ha tenido un mayor ratio 
    likes/dislikes. Si la categoría toma el valor None, se devolverá la tupla de tipo Video con mayor 
    ratio likes/dislikes de todas. El ratio likes/dislikes se calcula como el cociente entre el número 
    de likes y el número de dislikes. Tenga en cuenta que puede haber vídeos que no hayan recibido dislikes.
.
    Entrada:
     - videos: lista de tuplas con la información de vídeos trending
         -> [Video(str,date,str,str,str,int,int,int)]
     - categoria: nombre de la categoría del vídeo -> str

    Salida:
     - vídeo con mejor ratio likes/dislikes de la categoría dada o de todas.
         -> Video(str,date,str,str,str,int,int,int)
    '''
    pass

def canales_top(videos, n=3):
    '''
    Devuelve una lista de tuplas (canal, num_videos_trending) con los n canales que tienen
    más vídeos trending. Cada tupla contiene el nombre del canal y el número de vídeos 
    trending de ese canal, teniendo en cuenta que si un vídeo es trending durante d días, 
    contará d veces para el canal. La lista estará ordenada de mayor a menor número de vídeos trending. 
    Entrada:
     - videos: lista de tuplas con la información de vídeos trending
         -> [Video(str,date,str,str,str,int,int,int)]
     - n: número de vídeos que se incluiran en el ranking -> int

    Salida:
     - listas de tuplas (canal, num_videos_trending)
         -> [(str, int)]
    '''    
    pass

def video_mas_likeability_por_categoria(videos, k=20):
    '''
    Devuelve un diccionario que asocia las categorías(claves), con el vídeo de mayor índice 
    likeability de esa categoría. El índice likeability se calcula según la fórmula 
    que se indica en el enunciado.    
    Entrada:
     - videos: lista de tuplas con la información de vídeos trending
         -> [Video(str,date,str,str,str,int,int,int)]
     - k: constante usada para el cálculo del índice likeability -> int

    Salida:
     - diccionario de categorías (claves) y vídeos con más likeability de esa categoría
         -> {str:Video(str,date,str,str,str,int,int,int)}
    '''
    pass
    
def incrementos_visitas(videos, canal):
    '''
    Recibe una lista de tuplas de tipo Video y un canal. Devuelve una lista con el incremento (o 
    decremento) del total de visitas diarias de los vídeos trending de un día con respecto al día 
    anterior para el rango de fechas en que hay mediciones. Note que puede haber días para el que 
    se hayan tomado mediciones en los que no aparezca ningún video de un canal concreto, ya que los
    videos de ese canal no han sido tendencia ese día. Sin embargo, esos días habrá que tenerlos 
    en cuenta en el cálculo de los incrementos. Por ejemplo, el canal Mr. Tops no tiene ningún 
    vídeo trending el día 10/01/2017, y el día 11/01/2017 ha obtenido 200487 visitas en videos 
    que son tendencia. En este caso, en la lista resultado debe aparecer un incremento de 200487, 
    aunque no se haya registrado ningún dato de ese canal el día 10/01/2017.  
    Entrada:
     - videos: lista de tuplas con la información de vídeos trending
         -> [Video(str,date,str,str,str,int,int,int)]
     - canal: nombre del canal a analizar -> str

    Salida:
     - lista con incrementos/decrementos de visitas
         -> [int]
    '''
    pass