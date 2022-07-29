# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 00:51:49 2022

@author: 082al
"""

### pandas

"""
hızlı güçlü esnek

"""

import pandas as pd

           ## sözzlük oluştur
           

dictionary = {"isim " : ["ali","veli","kenan","murat","ayşe","hilal"],
              "yaş  " : [15,16,17,33,45,66],
              "maaş ":  [100,150,240,350,110,220] } 


veri = pd.DataFrame(dictionary)

print(veri)

### ilk beş satır

print(veri.head())

## sutunları yazdırma 

print(veri.columns)

## veri bilgisi

print(veri.info())


## istatistikler

print(veri.describe())


## yas sütüunu

print(veri["yaş  "])



## veri ekleme

veri["şehir "] = ["Ankara","İstanbul","Konya","İzmir","Bursa","Antalya"]

print(veri
      )

### yas sutunu

print(veri.loc[:,"yaş  "])

print(veri.loc[:2,"yaş  "])






### yas ve şehir arası sutunu

print(veri.loc[:,"yaş  "])

print(veri.loc[:2,"yaş  ":"şehir "])


print(veri.loc[:2,["yaş  ","isim "]])

## tersten yazdırma 

print(veri.loc[::-1,:])

## yas sutuunu with iloc


print(veri.iloc[:,1])

print(veri.iloc[:2,[0,1]])
                

## iloc da sonuncu dahil değil 
                           
                                
                              
diy = {"isim " : ["ali","veli","kenan","murat","ayşe","hilal"],
              "yaş" : [15,16,17,33,45,66],
              "şehir ":  ["İzmir","Ankara","Konya","Ankara","Ankara","Antalya"] } 


veri = pd.DataFrame(diy)
                
print(veri)


### yaşa göre filtre

filtre1 = veri.yaş   > 22

filtrelenmişveri = veri[filtre1]
                
print(filtrelenmişveri)
                
                
                
ortalama_yaş = veri.yaş.mean()

veri["Yaşgrubu"] = ["kucuk" if ortalama_yaş > i else "buyuk" for i in veri.yaş]

print(veri)

## birleştirme 

sözlük1 = {"isim " : ["ali","veli","kenan"],
              "yaş" : [15,16,17],
              "şehir ":  ["İzmir","Ankara","Konya"] } 

                
                
                
veri1 = pd.DataFrame(sözlük1)        


     
                
sözlük2 = {"isim " : ["murat","ayşe","hilal"],
              "yaş" : [33,45,66],
              "şehir ":  ["Ankara","Ankara","Antalya"]} 
                
                

verim = pd.DataFrame(sözlük2)

veri_dikey = pd.concat([veri1,verim],axis = 0)


veri_yatay = pd.concat([veri1,verim], axis = 1)






