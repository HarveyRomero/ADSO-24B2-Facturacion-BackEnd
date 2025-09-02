from flask import request, jsonify
from flask_controller import FlaskController
from src.models.categorias import Categorias
from src.app import app
from src.schemas.categorias_schema import categorias_schema, categoria_schema
import re

class CategoriasController(FlaskController):

    @app.route('/api/v1/categorias', methods=['GET'])
    def lista_categorias():
        try:
            categorias = Categorias.traer_categorias()
            return categorias_schema.dump(categorias)
        except:
            return jsonify({ 'error': 'Error de conexión a la base de datos.' }), 400 
        
    @app.route('/api/v1/categorias/<id>', methods=['GET'])
    def categoria_por_id(id):
        try:
            categoria = Categorias.traer_categoria_por_id(id)
            return categoria_schema.dump(categoria)
        except:
            return jsonify({ 'error': 'Error de conexión a la base de datos.' }), 400   

    @app.route('/api/v1/categorias', methods=['POST'])
    def crear_categoria():        
        categoria_almacenar = Categorias(nombre_categoria=request.json["nombre_categoria"])
                               
        try:
            Categorias.crear_categoria(categoria_almacenar)
            return jsonify({ 'success': 'Categoria creado correctamente.' }), 201 
        except:            
            return jsonify({ 'error': 'Error al almacenar la categoria.' }), 400 