from fastapi import FastAPI 
import pandas as pd

#Ingesta del archivo "netflix.csv"
df_Netflix=pd.read_csv("./csv/netflix.csv" , sep="," , encoding="utf-8")

#Cambia el tipo de la columna date_added a datetime
df_Netflix["date_added"]=df_Netflix["date_added"].astype("datetime64")

#Ordena de mas antiguo a mas reciente
df_Netflix_ord=df_Netflix.sort_values(by=['date_added'])

#Reemplaza en la columna "director" el valor "Not Given" por Non
df_Netflix_ord["director"]=df_Netflix_ord["director"].replace("Not Given", "None")

#Usando mascaras dividir en 3 dataframes distintos, "release_year" 2019, 2020, 2021
##Dataframe correspondiente al año 2019
mask19=df_Netflix_ord[(df_Netflix_ord["release_year"]==2019)]

##Dataframe correspondiente al año 2020
mask20=df_Netflix_ord[(df_Netflix_ord["release_year"]==2020)]

##Dataframe correspondiente al año 2021
mask21=df_Netflix_ord[(df_Netflix_ord["release_year"]==2021)]

#Transformar los 3 dataframes en 3 diccionarios distintos

##Dicionario correspondiente al DataFrame "mask19" 
dic19=mask19.reset_index().to_dict(orient="index")

##Dicionario correspondiente al DataFrame "mask20" 
dic20=mask20.reset_index().to_dict(orient="index")

##Dicionario correspondiente al DataFrame "mask21" 
dic21=mask21.reset_index().to_dict(orient="index")


#Instancio la API creada con la libreria fastapi
app=FastAPI() 

#Creación de decoradores

#Decorador correspondiente al año 2019 "dic19" 
@app.get("/2019") 
async def index(): #Creo la función que se ejecutará en la dirección indicada despues del "/"
    return dic19

#Decorador correspondiente al año 2020 "dic20"
@app.get("/2020")
async def index():
    return dic20

#Decorador correspondiente al año 2021 "dic21"
@app.get("/2021")
async def index():
    return dic21
