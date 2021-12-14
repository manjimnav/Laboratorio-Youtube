# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:50:04 2019

@author: Toñi Reina
@Revisor: fermincruz, Mariano González
ÚLTIMA MODIFICACIÓN: 24/01/2020
"""

from youtube_sol import *

def test_lee_trending_videos(videos):        
    print ("Leidos ...", len(videos), "vídeos")
    print("Los tres primeros vídeos son:", videos[:3])
    print("Los tres últimos vídeos son:", videos[-3:])

def test_media_visitas(videos):
    fecha_str = '15/11/2017'
    fecha = datetime.strptime(fecha_str, '%d/%m/%Y').date()
    print ("La media de visitas del día", fecha_str, "es", media_visitas(videos, fecha))    
    
    fecha_str = '11/1/2000'
    fecha = datetime.strptime(fecha_str, '%d/%m/%Y').date()
    print ("La media de visitas del día", fecha_str, "es", media_visitas(videos, fecha))

def test_video_mayor_ratio_likes_dislikes(videos):
    print ("El vídeo con mayor ratio de todos es:")
    print(video_mayor_ratio_likes_dislikes(videos))    
    
    print ("El vídeo con mayor ratio de la categoría Education es:")
    print(video_mayor_ratio_likes_dislikes(videos, 'Education'))

def test_canales_top(videos):
    print ("El top-3 de canales es:")
    print(canales_top(videos))
    
    print ("El top-5 de canales es:")
    print(canales_top(videos, 5))
    
def test_video_mas_likeability_por_categoria(videos):
    k = 20
    print("Vídeo con más likeability por categoría con constante", k)
    dicc = video_mas_likeability_por_categoria(videos, k)
    for categoria, id_video in dicc.items():
        print(categoria, '-->', id_video)

def test_incrementos_visitas(videos):
    canal = 'Exatlón'
    print("Incrementos de visitas para el canal", canal)
    print(incrementos_visitas(videos, canal))
    
    canal = 'Mr. Tops'
    print("Incrementos de visitas para el canal", canal)
    print(incrementos_visitas2(videos, canal))
  
    
if __name__=="__main__":
    print("\nEJERCICIO 1")
    videos = lee_trending_videos("../data/MX_youtube_2017_utf8.csv")
    test_lee_trending_videos(videos)
    
    print("\nEJERCICIO 2")  
    test_media_visitas(videos)
    print("\nEJERCICIO 3")  
    test_video_mayor_ratio_likes_dislikes(videos)
    print("\nEJERCICIO 4")  
    test_canales_top(videos)
    print("\nEJERCICIO 5")  
    test_video_mas_likeability_por_categoria(videos)
    print("\nEJERCICIO 6")  
    test_incrementos_visitas(videos)
