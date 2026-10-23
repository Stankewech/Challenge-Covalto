## Tabla de Contenidos
1. [Información General](#informacion-general)
2. [Tecnologías](#tecnologias)
3. [Instalación](#instalacion)

### Información General
***
Este proyecto es un Reto de API enfocado en obtener y mostrar datos de la serie Rick and Morty. Los archivos principales incluyen buscador.html, app.js y un archivo de pruebas en Python llamado Test.py. El sistema carga la información de los 5 personajes principales, mide el tiempo de respuesta de la conexión y muestra los resultados en tarjetas. Además, incluye un script de pruebas para confirmar que los datos lleguen correctamente y que los personajes estén marcados como vivos.


## Tecnologías
***
Lista de tecnologías que usamos en el proyecto:
- [HTML5](https://developer.mozilla.org/es/docs/Web/HTML): Estructura visual del buscador de personajes.
- [CSS3](https://developer.mozilla.org/es/docs/Web/CSS): Diseño general de la página.
- [JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript): Código encargado de conectarse a la API y dibujar la información en pantalla.
- [Python 3](https://www.python.org/): Usado en el archivo Test.py para revisar automáticamente que la API responda bien.

## Instalación
***
Una pequeña guía para empezar a usar el proyecto y correr las pruebas. 

Para ver la página web:
```
$ git clone https://github.com/tu-usuario/tu-repo.git
$ cd tu-repo
$ start buscador.html
```

Para correr las pruebas automáticas en Python:
```
$ pip install -r requirements.txt
$ python Test.py
```
Nota: Las pruebas de Python revisarán que la conexión devuelva un código 200 (que significa que todo salió bien) y confirmará que los primeros dos personajes estén vivos según los datos.
