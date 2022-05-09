from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

ultimajornada = Table(
    "ultimajornada",
    meta,
                Column("id", Integer, primary_key=True),
                Column("categoria", String(255)),
                Column("jornada", String(50)),
                Column("fechajornada", String(100)),
                Column("dia", String(50)),
                Column("diames", String(50)),
                Column("hora", String(50)),
                Column("ubicacion", String(255)),
                Column("equipolocal", String(255)),
                Column("equipovisitante", String(255)),
                Column("goleslocal", Integer),
                Column("golesvisitante", Integer),
                Column("arbitro", String(255)),
                Column("puntoslocal", Integer),
                Column("puntosvisitante", Integer),
                Column("ganolocal", Integer),
                Column("ganovisitante", Integer),
                Column("empato", Integer),
)


jornadas = Table(
    "jornadas",
    meta,
                Column("id", Integer, primary_key=True),
                Column("categoria", String(255)),
                Column("jornada", String(50)),
                Column("fechajornada", String(100)),
                Column("dia", String(50)),
                Column("diames", String(50)),
                Column("hora", String(50)),
                Column("ubicacion", String(255)),
                Column("equipolocal", String(255)),
                Column("equipovisitante", String(255)),
                Column("goleslocal", Integer),
                Column("golesvisitante", Integer),
                Column("arbitro", String(255)),
                Column("puntoslocal", Integer),
                Column("puntosvisitante", Integer),
                Column("ganolocal", Integer),
                Column("ganovisitante", Integer),
                Column("empato", Integer),
)



tablageneral = Table(
    "tablageneral",
    meta,
                Column("id", Integer, primary_key=True),
                Column("posicion", Integer),
                Column("equipo", String(255)),
                Column("juegosjugados", Integer),
                Column("juegosganados", Integer),
                Column("juegosempatados", Integer),
                Column("juegosperdidos", Integer),
                Column("puntos", Integer),
            
)


proximajornada = Table(
    "proximajornada",
    meta,
                Column("id", Integer, primary_key=True),
                Column("categoria", String(255)),
                Column("jornada", String(50)),
                Column("fechajornada", String(100)),
                Column("dia", String(50)),
                Column("diames", String(50)),
                Column("hora", String(50)),
                Column("ubicacion", String(255)),
                Column("equipolocal", String(255)),
                Column("equipovisitante", String(255)),
)


jugadores = Table(
    "jugadores",
    meta,
                Column("id", Integer, primary_key=True),
                Column("equipo", String(255)),
                Column("nombre", String(255)),                
                Column("apaterno", String(100)),
                Column("amaterno", String(100)),
                Column("fechanacimiento", String(50)),
                Column("posicion", String(100)),
                Column("numerojugador", Integer),
                Column("numperoregistro", Integer),
)


meta.create_all(engine)