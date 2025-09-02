from sqlalchemy import Column, Integer, String
from src.models import session, Base

class Categorias(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(300), unique=True, nullable=False)

    
    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria

    def traer_categorias():
        categorias = session.query(Categorias).all()
        return categorias     
    
    def traer_categoria_por_id(id):
        categoria = session.query(Categorias).filter(Categorias.id == id).first()
        return categoria
    
    def crear_categoria(categoria):
        categoria = session.add(categoria)
        session.commit()
        return categoria