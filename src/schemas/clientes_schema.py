from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.models.clientes import Clientes

class ClientesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Clientes
        load_instance = True

cliente_schema = ClientesSchema()
clientes_schema = ClientesSchema(many=True)