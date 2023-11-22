def limpiarWhite(archivo):
    count = 0
    finalBuf=[]
    file=open(archivo,'r')
    while True:
        count+=1
        line=file.readline()
        #eliminar comentarios
        comment=line.find("#") 
        if comment!=-1:
            line=line[:comment]
        #eliminar whitespaces
        line=line.replace("\n","") 
        if(line==''):
            return finalBuf
        #agregar sentinelas
        line=line+'~'
        data={"buf":line,"line":count}
        finalBuf.append(data)
