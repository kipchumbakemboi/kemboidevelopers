from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

@api_bp.route('/projects')
@jwt_required()
def projects():
    return jsonify({"message": "API working", "projects": []})

@api_bp.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "Kemboi Developers API"})
