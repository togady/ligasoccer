from fastapi import APIRouter
from config.db import conn
from models.jornada import ultimajornada 
from models.jornada import jornadas 
from models.jornada import tablageneral 
from models.jornada import proximajornada 
from models.jornada import jugadores
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

from cryptography.fernet import Fernet


ujornada = APIRouter()
@ujornada.get(
    "/ultimajornada"
)
def get_ultimajornada():
    return conn.execute(ultimajornada.select()).fetchall()



tjornadas = APIRouter()
@tjornadas.get(
    "/jornadas"
)
def get_jornadas():
    return conn.execute(jornadas.select()).fetchall()



ttablageneral = APIRouter()
@ttablageneral.get(
    "/tablageneral"
)
def get_tablageneral():
    return conn.execute(tablageneral.select()).fetchall()



tproximajornada = APIRouter()
@tproximajornada.get(
    "/proximajornada"
)
def get_proximajornada():
    return conn.execute(proximajornada.select()).fetchall()


tjugadores = APIRouter()
@tjugadores.get(
    "/jugadores/{equipo}"
)
def get_jugadores(equipo: str):
    return conn.execute(jugadores.select().where(jugadores.c.equipo == equipo)).fetchall()