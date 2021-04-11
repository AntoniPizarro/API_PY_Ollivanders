from flask import jsonify, g
from services.db_engine import get_bd
from repository.items import Guilded_rose

def update_quality():
    db = get_bd()
    