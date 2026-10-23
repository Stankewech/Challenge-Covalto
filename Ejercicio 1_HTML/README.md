## Tabla de Contenidos
1. [Información General](#informacion-general)
2. [Tecnologías](#tecnologias)
3. [Instalación](#instalacion)
4. [Colaboración](#colaboracion)
5. [Preguntas Frecuentes](#preguntas-frecuentes)

### Información General
***
Este proyecto es el QA Challenge, enfocado en corregir errores de una página web de prueba. El proyecto está terminado después de revisar el código original. Los archivos que checamos incluyen index1.html, estilos.css, main.js, filtro.js y la carpeta img/. Se encontraron y arreglaron un total de 19 errores divididos en 4 áreas: Estructura HTML, Lógica JavaScript, Estilos CSS y Sistema de Archivos.



## Tecnologías
***
Lista de tecnologías que usamos en el proyecto:
- [HTML5](https://developer.mozilla.org/es/docs/Web/HTML): Estructura para arreglar la página y los enlaces.
- [CSS3](https://developer.mozilla.org/es/docs/Web/CSS): Estilos, colores y diseño para que se vea bien en celulares.
- [JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript): Control del menú y detalles interactivos.

## Instalación
***
Una pequeña guía para empezar. 
```
$ git clone https://github.com/Stankewech/Challenge-Covalto.git
$ cd Challenge-Covalto/Ejercicio 1_HTML
$ start index.html
```
Nota: Para ver el resumen especial del proyecto, abre el archivo ```Reporte de fallos.html```. Ahí podrás ver una lista interactiva con los 19 errores que reparamos.

## Colaboración
***
Instrucciones sobre cómo ayudar en el proyecto.
> Si quieres proponer cambios o avisarnos de un error nuevo, por favor abre un "issue" en el repositorio.
> Asegúrate de anotar el ID del error, qué tan grave es y el archivo afectado, igual que en nuestro reporte.
> Todo el código debe mantener el mismo orden que ya usamos.

## Preguntas Frecuentes
***
Lista de preguntas más comunes
1. **¿Cuál fue el error más grave encontrado en el HTML?**
La palabra _href_ estaba mal escrita como _hred_ en los 5 enlaces del menú, por lo que no funcionaba ninguno.

2. __¿Cómo se clasificó la gravedad de los 19 errores?__ 
Para responder a esta pregunta, usamos esta lista:
- 5 Críticos (No dejaban funcionar la página)
- 8 Altos (Fallos visuales o enlaces rotos)
- 6 Medios y Bajos (Detalles para mejorar el código)

3. **¿Por qué no se veía bien la animación de carga inicial?**
El nombre de la clase estaba mal escrito en el HTML como *centradoo* con doble o, así que no tomaba el diseño correcto del archivo CSS.

4. **¿Cuáles son las 4 áreas revisadas en este proyecto?**
| Área revisada | Archivos afectados | Total de errores |
|:--------------|:-------------:|--------------:|
| Estructura HTML | index1.html | 13 |
| Lógica JavaScript | filtro.js, main.js | 2 |
| Estilos CSS | estilos.css | 2 |
| Sistema de Archivos | img/, js/ | 2 |
