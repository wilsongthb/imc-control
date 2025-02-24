from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ControlPesoAltura(Base):
    __tablename__ = 'control_peso_altura'

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    peso_kg = Column(Float, nullable=False)
    altura_m = Column(Float, nullable=False)
    imc = Column(Float, nullable=False)

    def __repr__(self):
        return f"<ControlPesoAltura(fecha={self.fecha}, peso_kg={self.peso_kg}, altura_m={self.altura_m}, imc={self.imc})>"
    


engine = create_engine('sqlite:///control_peso_altura.db')
Session = sessionmaker(bind=engine)
session = Session()