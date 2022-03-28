def correo():
        validacion = "@"
        while True:
            correo_electronico = str(input("Ingrese el correo electronico "))
            salir = 0
            for true in correo_electronico:

                if(validacion==true):
                    salir = 1
                    break
                
                elif( not validacion==true):
                   salir = 0 
            if salir==1:
                break
            else:
                print("la direccion de correo ",correo_electronico," no es valida")
        return correo_electronico
print(correo())