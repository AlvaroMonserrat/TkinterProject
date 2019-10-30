#Thread Tutorial: Trabajando solo con 1 Hilo
#Daamon True: significa que el programa -thread main- termina y el thread secundario puede no ser terminado (Es como un apagon)
#Daemon False: El thread main termina y el thread secundario tambien termina (antes o despues)

"""Estructura no daemon:
    nameThread = threading.Thread(target= nameFuncion, args= (,))
    nameThread.start()
"""

import threading
import logging
import time


def thread_function(name):
    logging.info("Thread %s: comenzando", name)
    time.sleep(2)
    logging.info("Thread %s: Terminando", name)


if __name__ == '__main__':
    #Configurar mensajes de registro del programa
    format = "%(asctime)s - %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt= "%H:%M:%S")

    logging.info("Main: antes de crear el -thread-")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main: antes de correr el -thread-")
    x.start()
    logging.info("Main: esperando que termine el thread")
    #x.join() #Espera hasta que termine el thread
    logging.info("Main: programa terminado")
