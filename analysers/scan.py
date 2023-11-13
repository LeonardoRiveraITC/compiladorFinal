def limpiarWhite(archivo):
    finalBuf=''
    file=open(archivo,'r')
    while True:
        line=file.readline()
        if(line==''):
            return finalBuf
        finalBuf+=line.replace(" ","").replace("\n","")
