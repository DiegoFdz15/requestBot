from datetime import datetime
import requests
import time
import argparse

def main():

    parser = argparse.ArgumentParser(description='''Usalo para mantener activo una aplicacion de heroku,
    realiza peticiones de acuerdo al tiempo que le indiques para luego guardarlo en un archivo log''')

    parser.add_argument('-u','--url',help='Con esta opcion proporcionas la url a realizar la peticion')
    parser.add_argument('-d','--dir',help='Especifica la direccion a donde guardar el archivo log (Default " ./ " )', default='./')
    parser.add_argument('-t','--time',help='Especifica el tiempo en segundos (Default: 10seg.)', default=10, type=int)

    args = parser.parse_args()
    
    if  not (str(args.url).__contains__('http') or str(args.url).__contains__('https')):
        args.url = "http://" + args.url
        print(args.url)
    
    try:
        temp = requests.get(args.url)
    except:
        print('Ingrese una url valida.')
        exit()  

    while True:
        peticion (args.url, args.dir, int(args.time))


def peticion (url, direc, timeSleep):

    cabecera = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    peticion = requests.get(url=url, headers=cabecera)
    stri = "  ////////////////////////////////////////////////////////////\n"
    stri += " /// " + url + "\tCode Status: " + str(peticion.status_code) + "\n"
    stri +="////////////////////////////////////////////////////////////\n"
    stri += str(datetime.now()) + "\n"
    print(stri)
    log(stri, direc)
    time.sleep(timeSleep)


def log(log, dir):
    f = open(dir + "log.txt", mode='a')
    f.write(log + "\n")
    f.close()

if (__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()
    #except TypeError:
    #    print('Debes especificar la url')