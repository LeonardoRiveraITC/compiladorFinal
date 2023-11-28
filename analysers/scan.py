def limpiarWhite(archivo):
    count = 0
    finalBuf=[]
    file=open(archivo,'r')
    while True:
        count+=1
        line=file.readline()
        if(line==''):
            return finalBuf
        #agregar sentinelas
        #eliminar whitespaces
        #eliminar comentarios
        comment=line.find("#") 
        if comment!=-1:
            line=line[:comment]
        line=line.replace("\n","") 
        if (line!=' '):
            line=line+'~'
            data={"buf":line,"line":count}
            finalBuf.append(data)

        
