import json
from pickle import FALSE
from ..models.person import Person
from ..view.View import View
from datetime import datetime

class Controller:
    
    def __init__(self):
        self.valor_seleccionado = 0
        self.vista = View()
        self.personas = []
        self.val_tel_count = 0
        self.val_email_count = 0
        self.copia=0

    def acciones(self):
        while self.valor_seleccionado != 7:
            self.carga_inicial()
            self.person_happybertday()
            self.valor_seleccionado = self.vista.seleccionar_opcion_menu()
            if self.valor_seleccionado == 1:
                self.crear_persona()
                self.auto_guardado()
            if self.valor_seleccionado == 2:
                self.listar_personas()
            if self.valor_seleccionado == 3:
                self.buscar_contactos()
            if self.valor_seleccionado == 4:
                self.grupo_contactos()
                self.auto_guardado()
            if self.valor_seleccionado == 5:
                self.exportar_personas()
            if self.valor_seleccionado == 6:
                self.cargar_personas()
                self.auto_guardado()


    def crear_persona(self):
        nombre,apellido,apodo = self.vista.formbasic_persona()#"s","s","d"
        while True:
            telefono_val =self.vista.telefono()        
            tel_message = self.validar_telefono(telefono_val)
        
            if tel_message== "repetido":    
                self.vista.telefono_existe()
            else:
                telefono = telefono_val
                telefono2=""
                telefono3=""
                break
        opcion =self.vista.agg_telefono()
        if opcion==1:
            while True:
                telefono_val2 =self.vista.telefono()
                tel_message = self.validar_telefono(telefono_val2)
            
                if tel_message== "repetido":    
                    self.vista.telefono_existe()
                else:
                    telefono2=telefono_val2
                    telefono3=""
                    break
            opcion =self.vista.agg_telefono()
                    
            if opcion==1:
                while True:
                    telefono_val3 =self.vista.telefono()
                    tel_message = self.validar_telefono(telefono_val3)
                
                    if tel_message== "repetido":    
                        self.vista.telefono_existe()
                    else:
                        telefono3=telefono_val3
                        break
        while True:          
            correo_val = self.vista.correo()
            correo_message = self.validar_correo(correo_val)
            if correo_message== "repetido":
                self.vista.correo_existe()
                correo_val=''
            else:
                correo_electronico=correo_val
                break
        happybertday=self.vista.date_cumpleaños()
        persona = Person(nombre, apellido, apodo, telefono, telefono2, telefono3, correo_electronico, happybertday)
        self.personas.append(persona)
        self.vista.persona_creada_correctamente(persona.nombre, persona.apellido)

    def listar_personas(self):
        for persona in self.personas:
            print(persona.expotar())

    def exportar_personas(self):
        nombre_del_archivo = self.vista.nombre_del_archivo()
        lista_para_exportar = []
        for persona in self.personas:
            lista_para_exportar.append(persona.expotar())

        with open(f"data/{nombre_del_archivo}.json", "w") as fp:
            json.dump(lista_para_exportar, fp)

        self.vista.mensaje_correcto()

    def cargar_personas(self):
        nombre_del_archivo = self.vista.nombre_del_archivo()
        try:
            with open(f"data/{nombre_del_archivo}.json", "r") as fp:
                data = json.load(fp)

            for persona in data:
                self.personas.append(
                    Person(
                        nombre=persona["nombre"],
                        apellido=persona["apellido"],
                        apodo = persona["apodo"],
                        telefono=persona["telefono"],
                        telefono2=persona["telefono2"],
                        telefono3=persona["telefono3"],
                        correo_electronico=persona["correo electronico"],
                        happybertday = persona["Fecha de happybertday"]
                    )
                )
        except Exception as e:
            self.vista.mensaje_incorrecto(e)

    def salir(self):
        pass

    def validar_telefono(self, telefono_val):
        telefonos=[]
        for persona in self.personas:
            tel1=persona.exportar_telefono()
            tel2=persona.exportar_telefono2()
            tel3=persona.exportar_telefono3()
            telefonos.append(tel1)
            telefonos.append(tel2)
            telefonos.append(tel3)
        for true in telefonos:

            if(telefono_val==true):
                self.val_tel_count=1
                break
            
            elif( not telefono_val==true):
                self.val_tel_count=2
                        
        if (self.val_tel_count==1):
           return f"repetido"
        else:
            return f"nuevo" 
        
    def validar_correo(self, correo_val):
        correos=[]
        for persona in self.personas:
            correos.append(persona.export_correo())
        for true in correos:

            if(correo_val==true):
                self.val_email_count=1
                break
            
            elif( not correo_val==true):
                self.val_email_count=2
                        
        if (self.val_email_count==1):
            return f"repetido"
        else:
            return f"nuevo"

    def buscar_contactos(self):
        buscar_contacto=self.vista.busqueda()

        for elemento in self.personas:

            if(buscar_contacto==elemento.nombre):
                vista = elemento.expotar()
                print(vista)
                contact_count=1
                break
                
            elif( not buscar_contacto==elemento.nombre):
                contact_count=2
                        
        if (contact_count==2):
            self.vista.mensaje_error_busqueda()

    def auto_guardado(self):
        nombre_del_archivo = "copia_de_seguridad"
        lista_para_exportar = []
        for persona in self.personas:
            lista_para_exportar.append(persona.expotar())

        with open(f"data/{nombre_del_archivo}.json", "w") as fp:
            json.dump(lista_para_exportar, fp)

        self.vista.sms_auto_guardado()
        

    def carga_inicial(self):
        try:
            with open(f"data/copia_de_seguridad.json", "r") as fp:
                data = json.load(fp)

            for persona in data:
                self.personas.append(
                    Person(
                        nombre=persona["nombre"],
                        apellido=persona["apellido"],
                        apodo = persona["apodo"],
                        telefono=persona["telefono"],
                        telefono2=persona["telefono2"],
                        telefono3=persona["telefono3"],
                        correo_electronico=persona["correo electronico"],
                        happybertday = persona["Fecha de happybertday"]
                    )
                )
        except Exception as e:
            pass
    
    def person_happybertday(self):
        date=datetime.today().strftime('%d-%m-%Y')

        for elemento in self.personas:

            if(date==elemento.happybertday):
                name = elemento.export_nombre()
                self.vista.cumpleañeros(name)
                break




        
