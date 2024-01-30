from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker


engine = create_engine('postgresql://postgres:Otabek2004@localhost/delivery_clone',
                       echo=True)

Base = declarative_base()
session = sessionmaker()




