from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models.categorias import Categorias

class CategoriasSchema(SQLAlchemyAutoSchema):
        class Meta:
            model = Categorias
            load_instance = True

categoria_schema = CategoriasSchema()
categorias_schema = CategoriasSchema(many=True)