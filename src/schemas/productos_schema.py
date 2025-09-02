from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models.productos import Productos

class ProductosSchema(SQLAlchemyAutoSchema):
        class Meta:
            model = Productos
            load_instance = True

producto_schema = ProductosSchema()
productos_schema = ProductosSchema(many=True)