# API CyclingDB con Django Rest Framework y Swagger

## Índice

* [Autores](#autores)
* [Requisitos](#requisitos)
* [Descripción](#descripción)

## Autores

- Marvin Ulanday Saludo

## Requisitos

Primero, creamos la base de datos en pgAmin 4 con el nombre de **cyclingDB**.

A continuación, en settings.py. modificamos la contraseña del usuario del postgres al que has seleccionado.

Después, desde la terminal, accedemos al directorio del proyecto y aplicamos el siguiente comando para crear las tablas de los modelos en la base de datos:

> python manage.py migrate

El comando python puede variar en el sistema operativo y tengais que usar el comando python acompañado de su versión instalada (Ejemplo: python3).

Las vistas son de tipo **genérico**, asi que en caso de que no se haya comentado las lineas debidas se tendrá que comentar las lineas necessarias del archivo generics.py mostradas a continuación:

![alt text](https://i.imgur.com/MelQQfD.jpg)

## Descripción

La aplicación consiste en un BackEnd de Ciclismo que se compone de los modelos: **Cyclist**, **Country**, **Team**, **Race**, **TeamRace**, **Stage** y **Specialty**. 

Toda documentación ha sido realizada con **Swagger** y se podrá ver las rutas para probar a insertar, recoger, modificar y eliminar datos sin necesidad de acceder a la ruta correspondiente.

Para iniciar el Backend, desde la terminal se debe insertar el comando:

> python manage.py runserver
