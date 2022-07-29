# -*- coding: utf-8 -*-
"""

KKAAAN HAY SENIN MUCUK

"""


"""
Created on Tue Jul 19 22:44:24 2022

@author: 082al
"""

### %% yield 
"""
iterasyonlar yineleme

generator 
bellekte saklamaz yeri gelince anında üretirler

yield
"""

liste = [1,2,3]

for i in liste:
    
    print(i)
    
    
generator = (x for x in range(1,4)) 

for i in generator:
    
    print(i)
    
    
"""
fonksiyon return olarak return olarak generatır döndürecekse bunu return yerine yapar
"""


def createGenerator():
    liste = range(1,4)
    for i in liste:
        yield i
        
        
print(createGenerator())


## numpy

"""
matrisler için hesaplama kolaylığı sağlar

"""

import numpy as np


## 1*15 array-dizi


dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(dizi)

print(dizi.shape) ## arrayin boyu


dizi2 = dizi.reshape(3,5)

print("Şekil: ",dizi2.shape)
print("Boyut: ",dizi2.ndim)
print("Boy: ",dizi2.size)
print("Veri tipi",dizi2.dtype.name)


## array type 

print("Type: ",type(dizi2))



dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

print(dizi2D)


## sıfırlardan oluşan bir array 


sifir_dizi = np.zeros((3,4))
print(sifir_dizi)


## birlerden oluşan bir array 


bir_dizi = np.ones((3,4))
print(bir_dizi)



### boş array

bos_dizi = np.empty((3,4))

print(bos_dizi)


## arange(x,y,basamak)


dizi_aralik = np.arange(10,50,5)

print(dizi_aralik)


#### linspace(x,y,basamak)

dizi_bosluk = np.linspace(10,20,5)


## float  array 
float_array = np.float32([[1,2],[3,4]])
print(float_array)



## matemetiksel işlemler 

a = np.array([1,2,3])
b = np.array([4,5,6])


print(a+b)
print(a*b)
print(a-b)
print(a**2)


## dizi elemanı toplama

print(np.sum(a))

print(np.max(a))

print(np.min(a))
##ortalama
print(np.mean(a))

## rastgele sayı üretme [0,1] sürekli uniform 3*3



rastgele_dizi = np.random.random((3,3))

print(rastgele_dizi)

## index 

dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])

print(dizi[0:4])
## 4. dahil değil


print(dizi[::-1])


dizi2p = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2p)




## dizinin 1. satır ve sütunu yazdır


print(dizi2p[1,1])
print(dizi2p[:,1])


## satır1, sütun 1,2,3

print(dizi2p[1,1:4])


dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

## VEKTOR haline getirir 
vektor = dizi2D.ravel()
print(vektor)


maksimum_sayının_indeksi = vektor.argmax()
print(maksimum_sayının_indeksi)















































