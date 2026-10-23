## Tabla de Contenidos
1. [Información General](#informacion-general)
2. [Tecnologías](#tecnologias)
3. [Instalación](#instalacion)

### Información General
***
Este proyecto contiene una lista de pruebas (Matriz de Pruebas) diseñadas para la página de compras de Swag Labs (saucedemo.com). El proyecto incluye un archivo web interactivo (prueba final.html) donde se muestran 10 casos de prueba detallados, evaluando cosas como el inicio de sesión, el carrito y el formulario de compra. Además, incluye un script en Python (Auto.py) que hace dos de estas pruebas de forma automática simulando a un usuario real navegando por la página.


## Tecnologías
***
Lista de tecnologías que usamos en el proyecto:
- [HTML5](https://developer.mozilla.org/es/docs/Web/HTML): Para la estructura de la página que muestra la lista de pruebas.
- [CSS3](https://developer.mozilla.org/es/docs/Web/CSS): Para darle diseño y formato a las tablas de información.
- [JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript): Para que funcionen los filtros de búsqueda y el botón de descarga del PDF.
- [Python 3](https://www.python.org/): Lenguaje usado para escribir las pruebas automáticas.
- [Selenium WebDriver](https://www.selenium.dev/): Herramienta para controlar el navegador (Microsoft Edge) de forma automática.

## Instalación
***
Una pequeña guía para empezar a ver el proyecto y correr las pruebas automáticas.

Para ver la página web con la lista de pruebas:
```
$ git clone https://github.com/tu-usuario/tu-repo.git
$ cd tu-repo
$ start "prueba final.html"
```

Para correr las pruebas automáticas en Python, primero necesitas instalar la librería de Selenium. Ejecuta lo siguiente en tu terminal:
```
$ pip install -r requirements.txt
$ python Auto.py
```
Nota: El script abrirá automáticamente una ventana del navegador Edge y realizará el proceso de compra completo y la validación de un usuario bloqueado.
