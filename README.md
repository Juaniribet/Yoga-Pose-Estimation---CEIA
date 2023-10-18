<p align="center">
<img src=doc/inicio.png>
</p>

## **Trabajo Final**

## Yoga Pose Estimation 

## Autor: Juan Ignacio Ribet

### Director:  Juan Pablo Pizarro (Globant)

### Programa de vinculacion con empresa Globant

Resumen

La presente memoria describe el desarrollo de un detector de postura de yoga o
asanas para la empresa Globant. Este trabajo pretende obtener el mínimo
producto viable de una aplicación para entrenamiento de yoga, en donde se
detecte la postura mediante algoritmos de aprendizaje de máquina y visión por
computadora, y se le de soporte al usuario para realizarlas de forma correcta.

Para su desarrollo fueron fundamentales los conocimientos adquiridos en la
carrera, en especial los vistos en las materias de visión por computadora con el
uso indispensable de la librería OpenCV como también los conceptos de
aprendizaje de máquina, análisis de datos y la comprensión del mecanismo de
funcionamiento de las de las redes neuronales convolucionales.

# Posturas o Asanas

La aplicación tiene la posibilidad de detectar las siguientes 4 posturas:


Downdog    -     Goddess
  
<img src=interface\pages\Data\images_display/downdog.png width='350'><img src=interface\pages\Data\images_display/goddess.png width='350'>

Tree     -     Warrior

<img src=interface\pages\Data\images_display/Tree.png width='350'><img src=interface\pages\Data\images_display/warrior.png width='350'>

En la notebook "Yoga_pose_detection.ipynb" podran encontar el siguiente contenido:

1.	Planteo del problema<br>
2.	Visualización de los datos<br>
3.	Creación del dataset para entrenar<br>
3.1.	Generación de cada dataset<br>
4.	Carga de los datasets generados<br>
5.	Verificación del balance de clases<br>
6.	Entrenamiento de los modelos<br>
7.	Verificación de modelo con imágenes de validación<br>
8.	Matriz de confusión en set de prueba<br>
9.	Optuna: Optimización de hiperparametros<br>
10.	Estimación de posturas en video<br>
11.	Interfaz<br>

**En la carpeta "interface" se encuentra la apliación final que pueden utilizarla corriendo el archivo "deploy.py"**

Al detectar la postura la aplicación medirá los ángulos característicos de la misma y los mostrará en pantalla para que el usuario pueda hacer las correcciones necesarias.

Tambien se podra ver un indicador led que se verá: 
  - Rojo: cuando no se detecte la postura. 
  - Verde-rojo: cuando se detecte la postura pero algún angulo este fuera de rango
  - Verde: Cuando la postura este correecta

<p align="center">
<img src=doc/video_interface.png>
</p>


