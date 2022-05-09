from sqlalchemy import create_engine, MetaData

engine=create_engine("mysql+pymysql://admin:ALVmorso1987#.@morso.cyjkiphsseaw.us-east-1.rds.amazonaws.com:3306/morsodb")

meta=MetaData()

conn=engine.connect()


