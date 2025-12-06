from flask import Blueprint, jsonify
from app.services.collection_service import CollectionService

api_bp = Blueprint('api', __name__)
collection_service = CollectionService()


@api_bp.route('/version', methods=['GET'])
def get_version():
    return jsonify(collection_service.get_version()), 200


@api_bp.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(collection_service.get_locations()), 200