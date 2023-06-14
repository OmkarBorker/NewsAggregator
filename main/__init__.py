import psycopg2
from flask import Flask
from flask_cors import CORS

DB_URL = 'postgres://postgres:Omkarborker1@db.jjdoiyhcuilwxtdkpbml.supabase.co:6543/postgres'

def create_db_connection():
    conn = psycopg2.connect(DB_URL)
    return conn


def create_app():
    app = Flask(__name__)
    
    from main import main_bp
    from data import data_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(data_bp)
    
    conn = create_db_connection()
    app.config['DB_CONNECTION'] = conn
    
    return app

