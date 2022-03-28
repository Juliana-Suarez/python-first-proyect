from ..models.person import Person

class View:
    def __init__(self):
        self.op1=''

    def seleccionar_opcion_menu(self):
        print("\n1. Crear Contacto ")
        print("2. Listar Contactos")
        print("3. Buscar Contactos")
        print("4. Crear Grupo de Contactos ")
        print("5. Exportar Contactos (JSON)")
        print("6. Cargar Contactos (JSON)")
        print("7. Salir")
        return int(input("Ingrese el valor: "))

    def formbasic_persona(self):
            nombre = str(input("Ingrese el nombre "))
            apellido = str(input("Ingrese el apellido "))
            apodo = str(input("Ingrese el apodo "))
            return nombre, apellido, apodo

    def telefono(self):
        telefono =str(input("Ingrese el telefono "))
        return telefono

    def agg_telefono(self):
        print("1. Agregar otro telefono ")
        print("2. Siguiente ")
        return int(input("Ingrese el valor: "))

    def correo(self):       
        correo_electronico = str(input("Ingrese el correo electronico "))
        return correo_electronico
        
    def date_cumpleaños(self):
        cumpleaños  = str(input("Ingrese Fecha de cumpleaños"))
        return cumpleaños

    def persona_creada_correctamente(self, nombre, apellido):
        print(f"Contacto {nombre} {apellido}, creado correctamente")
    
    def nombre_del_archivo(self):
        return str(input("Ingrese nombre del archivo: "))

    def mensaje_correcto(self):
        print("---//---//---//---//---//---//---//---//---")
        print("La petición fue ejecutada correctamente")
        print("---//---//---//---//---//---//---//---//---")

    def mensaje_incorrecto(self, message):
        print("---//---//---//---//---//---//---")
        print("La petición no se pudo realizar.")
        print(message)
        print("---//---//---//---//---//---//---")
            
    def telefono_existe(self):
        print("el Telefono ya existe en otro contacto")

    def correo_existe(self):
        print("el correo ya existe en otro contacto")

    def añadir_contact(self):
        opcion=int(input("1. Añadir contacto\n2. seguir "))
        return opcion
    
    def busqueda(self):
        return str(input("Buscar: "))

    def mensaje_error_busqueda(self):
        print("Ningín elemento coincide con el criterio de búsqueda")
    
    def sms_auto_guardado(self):
        print("guardado")
    def cumpleañeros(self,name):
        print("hoy esta cumpliendo años ",name," deseale un feliz cumpleaños")
        