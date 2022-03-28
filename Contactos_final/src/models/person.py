class Person:
    def __init__(self, nombre, apellido, apodo, telefono, telefono2, telefono3 ,correo_electronico,happybertday):
        self.nombre = nombre 
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono
        self.telefono2=telefono2
        self.telefono3=telefono3
        self.correo_electronico = correo_electronico
        self.happybertday = happybertday
        


    def expotar(self):
        return {
                    "nombre": self.nombre, 
                    "apellido": self.apellido, 
                    "apodo": self.apodo,
                    "telefono": self.telefono, 
                    "telefono2":self.telefono2,
                    "telefono3":self.telefono3,
                    "correo electronico": self.correo_electronico, 
                    "Fecha de happybertday": self.happybertday
                }

    def export_nombre(self):
        return self.nombre

    def export_apellido(self):
        return self.apellido

    def export_apodo(self):
        return self.apodo

    def exportar_telefono(self):
        return self.telefono

    def exportar_telefono2(self):
        return self.telefono2
        
    def exportar_telefono3(self):
        return self.telefono3

    def export_correo(self):
        return self.correo_electronico
        
    def export_happybertday(self):
        return self.happybertday