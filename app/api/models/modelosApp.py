from sqlalchemy import colums,integer,string,Float,date
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base 

#Crear una instancia de la base para crear tablas 
Base=declarative_base()

#Listado de modelos de la APLICACION
#Usuario
class Usuario(Base):
    __tablename__='Usuario'
    id=column(integer, primary_key=True,autoincrement=True)
    nombres=column(string(50))
    Edad=column(integer )
    Telfono=column(string(12))
    Correo=column(string(20))
    Contraseña=column(string(10))
    FechaDeRegistro=column(date)
    Ciudad=column(string(50))
#Gasto
class Gasto(Base):
    __tablename__='Gasto'
    id=column(integer, primary_key=True,autoincrement=True)
    monto=column(integer)
    fecha=column(date)
    descripcion=column(string(200))
    nombre=column(string(50))
#Categoria
class Categoria(Base):
    __tablename__='Categoria'
    id=column(integer, primary_key=True,autoincrement=True)
    nombreCategoria=column(string(20))
    descripcion=column(string(200))
    fotoIcono=column(string(1000))
#Metodos de pago
class Metodos(Base):
    __tablename__='Metodos'
    id=column(integer, primary_key=True,autoincrement=True)
    nombreMetodo=column(string(15))
    descripcion=column(string(200))
#Factura
class Factura(Base):
    __tablename__='Factura'