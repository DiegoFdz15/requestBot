def main():
    
    n = 1

    while n > 0:
        n += 1
        
        peticion ()
        n -= 1


def peticion ():
    import requests
    import time

    url = "https://homew0rks.herokuapp.com/"
    cabecera = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    peticion = requests.get(url=url, headers=cabecera)
    time.sleep(600)
    stri = "  ////////////////////////////////////////////////////////////\n"
    stri += " /// " + url + "\tCode Status: " + str(peticion.status_code) + " //////\n"
    stri +="////////////////////////////////////////////////////////////\n\n"
    log(stri)


def log(log):
    f = open("log.txt", mode='a')
    f.write(log + "\n")
    f.close()

if (__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()