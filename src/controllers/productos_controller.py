from flask import request, jsonify
from flask_controller import FlaskController
from src.models.productos import Productos
from src.app import app
from src.schemas.productos_schema import productos_schema, producto_schema
import re

class ProductosController(FlaskController):

    @app.route('/api/v1/productos', methods=['GET'])
    def lista_productos():
        try:
            productos = Productos.traer_productos()
            return productos_schema.dump(productos)
        except:
            return jsonify({ 'error': 'Error de conexión a la base de datos.' }), 400 
        
    @app.route('/api/v1/productos/<id>', methods=['GET'])
    def producto_por_id(id):
        try:
            producto = Productos.traer_producto_por_id(id)
            return producto_schema.dump(producto)
        except:
            return jsonify({ 'error': 'Error de conexión a la base de datos.' }), 400   

    @app.route('/api/v1/productos', methods=['POST'])
    def crear_producto():        
        producto_almacenar = Productos(codigo=request.json["codigo"]
                             , descripcion=request.json["descripcion"]
                             , valor_unitario=request.json["valor_unitario"]
                             , unidad_medida=request.json["unidad_medida"]
                             , cantidad_stock=request.json["cantidad_stock"]
                             , categoria=request.json["categoria"])
        producto_repetido =  Productos.traer_producto_por_descripcion(producto_almacenar.descripcion)
        if producto_repetido:
            return jsonify({ 'error': 'La descripción no se puede repetir.' }), 400                                    
        try:
            Productos.crear_producto(producto_almacenar)
            return jsonify({ 'success': 'Producto creado correctamente.' }), 201 
        except:            
            return jsonify({ 'error': 'Error al almacenar el producto.' }), 400 

