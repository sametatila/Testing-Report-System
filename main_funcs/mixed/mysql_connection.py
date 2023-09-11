from sqlalchemy import create_engine

engine = create_engine("mysql://XXX", pool_recycle=60 * 5, pool_pre_ping=True)

