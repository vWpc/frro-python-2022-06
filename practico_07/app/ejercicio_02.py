"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio

from typing import List, Optional

class DatosSocio():

    def __init__(self):
        pass # Completar
        engine1=create_engine('sqlite:///practico_07/socios.sqlite',connect_args={"check_same_thread": False})
        Base.metadata.create_all(engine1)
        Session=sessionmaker(bind=engine1)
        self.session=Session()


    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        pass # Completar
        consulta=self.session.query(Socio).filter_by(id_socio=id_socio).first()
        self.session.commit()
        if consulta is None:
            return None
        else:
            return consulta

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        pass # Completar
        consulta=self.session.query(Socio).filter_by(dni=dni_socio).first()
        self.session.commit()
        if consulta is None:
            return None
        else:
            return consulta
        
    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        pass # Completar
        print("llego hasta ACA")
        consulta=self.session.query(Socio).all()
        self.session.commit()
        return consulta

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        pass # Completar
        consulta=self.session.query(Socio).delete()
        self.session.commit()
        if consulta>0:
            return True
        else:
            return False
        

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        pass # Completar
        nuevosocio=Socio(socio.dni,socio.nombre,socio.apellido)
        self.session.add(nuevosocio)
        self.session.commit()
        return nuevosocio
        

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        pass # Completar
        consulta=self.session.query(Socio).filter_by(id_socio=id_socio).delete()
        self.session.commit()
        if consulta>0:
            return True
        else:
            return False
        

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        pass # Completar
        sociomodificar=self.session.query(Socio).filter(Socio.id_socio==socio.id_socio).first()
        sociomodificar.dni=socio.dni
        sociomodificar.nombre=socio.nombre
        sociomodificar.apellido=socio.apellido
        self.session.add(sociomodificar)
        self.session.commit()
        return sociomodificar
    
    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        pass # Completar
        consulta=self.session.query(Socio).count()
        self.session.commit()
        return consulta