import time

print("RuningSomething")


""" COMANDOS GENERALES

$git init // Inicializa el repositorio

$git add . // Agrega todos los archivos a la lista de cambios
Este comando tambien se puede hacer en un archivo en espesifico.

$git commit -m "mensaje" // Agrega un comentario al commit y lo guarda
En este comando es importante poner el -m "mensaje" ya que sino te mandara a la consola de vim.
Cada commit debe tener un mensaje.

🔥 $git status // Muestra el estado de los archivos segun su estado de cambios
🔥 $git show // Muestra el estado del repositorio tambien se puede consultar un commit especifico por su numero de commit
🔥 $git log // Muestra el historial de los commits y su numero de commit
🔥 $git log biogragia.txt // Muestra los commits de un archivo
🔥 $git push origin master // Envia los cambios al repositorio remoto

🔥 $git diff commitIdA commitIdB // Muestra los cambios que se han hecho entre un commit X y uno Y, el orden determina la linealidad de los cambios
🔥 $git diff // freddy lo uso para ver los cambios entre lo que tengo en disco y lo que tengo en la ram

🔥 $git checkout // Cambia el estado de los archivos a la ultima version
🔥 $git checkout commitIDA // Cambia el estado de los archivos a la version especificada 
🔥 $git checkout commitIDA historia.txt // Cambia el estado de un archivo a el de una version espesifica

🔥 $git branch cabecera // Crea una nueva branch llamada cabecera
checkout tambien sirve para moverse entre las branches, cambiando el estado de los archivos


Comandos para moverse en la consola vim _ Shift + Esc + Z + Z // salir y guardar los cambios



"""